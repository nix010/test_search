import json
import sys
from pprint import pprint


def load_data_from_file(file_name):
    with open(file_name, 'r') as f:
        return json.loads(f.read())


def index_id_data(data):
    return {item['_id']: item for item in data}


def process_value(value):
    if isinstance(value, list):
        return value
    return [value]


def index_type_name(type_name):
    return f'_{type_name.upper()}_INDEX'


def format_output(results):
    pprint(results)
    print(f'Have {len(results)} results matched')


class ControlCenter(object):

    _SKIP_INDEX_FIELD = ['_id']
    search_type = None

    ready = False

    def __init__(self, data_dir='data', should_print=True):
        self._data_dir = data_dir
        self._should_print = should_print
        self.ready = self._load_data()
        self._prepare_data()

    def cli_interface(self):
        types = {
            '1': 'user',
            '2': 'ticket',
            '3': 'organization',
        }
        while 1:
            print('1. Users')
            print('2. Ticket')
            print('3. Organization')
            type_name = input('Input type to search as a number or type "exit" to close: ').strip()
            if type_name == 'exit':
                sys.exit(0)
            type_name = types.get(type_name)
            if not type_name:
                print('Select invalided value. Try again')
                continue

            fields = self._get_field_column(type_name)
            field = input('Input the field to search: ').strip()
            if not fields.get(field):
                print('Select invalided value. Try again')
                continue

            value = input('Input the value to search: ').strip()
            self.search_for(type_name, field, value)
            print('==================')
            if input('Search again ?(y/n): ').strip() == 'n':
                return

    def _load_data(self):
        try:
            self.users = load_data_from_file(f'{self._data_dir}/users.json')
            self.organizations = load_data_from_file(f'{self._data_dir}/organizations.json')
            self.tickets = load_data_from_file(f'{self._data_dir}/tickets.json')
            return True
        except FileNotFoundError as e:
            print(f'Data file not found. {e.filename}.')
        except json.decoder.JSONDecodeError:
            print('Data files format is a incorrect JSON.')
        return False

    def _prepare_data(self):
        if not self.ready:
            return
        self._gather_columns_info(self.users, 'user')
        self._gather_columns_info(self.organizations, 'organization')
        self._gather_columns_info(self.tickets, 'ticket')

        self._build_inverted_index(self.users, 'user')
        self._build_inverted_index(self.organizations, 'organization')
        self._build_inverted_index(self.tickets, 'ticket')

        self.users = index_id_data(self.users)
        self.organizations = index_id_data(self.organizations)
        self.tickets = index_id_data(self.tickets)

    def _build_inverted_index(self, json_data, type_name):
        index_name = index_type_name(type_name)
        setattr(self, index_name, {})
        for item in json_data:
            for key, value in item.items():
                if key in self._SKIP_INDEX_FIELD:
                    continue
                if key not in getattr(self, index_name):
                    getattr(self, index_name)[key] = {}

                for val in process_value(value):
                    if val not in getattr(self, index_name)[key]:
                        getattr(self, index_name)[key][val] = set()
                    getattr(self, index_name)[key][val].add(item['_id'])

    def search_for(self, type_name, field, value):
        index = getattr(self, index_type_name(type_name))
        if field != '_id':
            parsed_value = self._parse_input(type_name, field, value)
            result_ids = index.get(field, {}).get(parsed_value)
        else:
            result_ids = [value]

        if not result_ids:
            return self._format_output_empty(type_name, field, value)
        mapper_function = getattr(self, f'_output_{type_name}_mapper')
        self.results = [mapper_function(idx) for idx in result_ids]
        if self._should_print:
            format_output(self.results)

    def _get_field_column(self, type_name):
        return getattr(self, f'{type_name.upper()}_COLUMN')

    def _parse_input(self, type_name, field, value):
        col = self._get_field_column(type_name)
        type_name = col.get(field)
        if not type_name:
            return None
        if type_name == list:
            return value
        if type_name == bool:
            return value == 'true' or value == 'True'

        return type_name(value)

    def _output_user_mapper(self, idx):
        item = self.users[idx]
        organization_name = self.organizations.get(item.get('organization_id'), {}).get('name')
        return {
            **item,
            'organization_name': organization_name
        }

    def _output_ticket_mapper(self, idx):
        item = self.tickets[idx]
        organization_name = self.organizations.get(item.get('organization_id'), {}).get('name')
        submitter_name = self.users.get(item.get('submitter_id'), {}).get('name')
        assignee_name = self.users.get(item.get('assignee_id'), {}).get('name')

        return {
            **item,
            'submitter_name': submitter_name,
            'assignee_name': assignee_name,
            'organization_name': organization_name,
        }

    def _output_organization_mapper(self, idx):
        organization = self.organizations[idx]
        tickets = getattr(self, index_type_name('ticket')).get('organization_id', {}).get(idx)
        tickets = [self.tickets[item]['subject'] for item in tickets] if tickets else []

        users = getattr(self, index_type_name('user')).get('organization_id', {}).get(idx)
        users = [self.users[item]['name'] for item in users] if users else []
        return {
            **organization,
            'tickets': tickets,
            'users': users,
        }


    def _format_output_empty(self, type, field, value):
        if self._should_print:
            print(f'No results found for "{type}" with "{field}" value of "{value}"')

    def _gather_columns_info(self, data, data_type):
        col = {}
        for item in data:
            col = {key: type(value) for key, value in item.items()}
            col.update(col)
        setattr(self, f'{data_type.upper()}_COLUMN', col)


if __name__ == '__main__':
    program = ControlCenter()
    if program.ready:
        program.cli_interface()
