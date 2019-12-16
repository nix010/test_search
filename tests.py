import sys
import unittest
import fixtures
import os
from main import *


class TestMainFunction(unittest.TestCase):

    class_test = ControlCenter

    @classmethod
    def setUpClass(self):
        with open('data_test/users.json', 'w') as f:
            f.write(json.dumps(fixtures.USERS))
        with open('data_test/organizations.json', 'w') as f:
            f.write(json.dumps(fixtures.ORGANIZATIONS))
        with open('data_test/tickets.json', 'w') as f:
            f.write(json.dumps(fixtures.TICKETS))

        with open('data_test/test_users_dammed.json', 'w') as f:
            f.write(json.dumps(fixtures.USERS) + 'xxx')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('data_test/users.json'):
            os.remove("data_test/users.json")
        if os.path.exists('data_test/organizations.json'):
            os.remove("data_test/organizations.json")
        if os.path.exists('data_test/tickets.json'):
            os.remove("data_test/tickets.json")

        if os.path.exists('data_test/test_users_dammed.json'):
            os.remove("data_test/test_users_dammed.json")

    def test_load_data_function_success(self):
        data = load_data_from_file('data_test/users.json')
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['_id'], 44)
        self.assertEqual(data[1]['_id'], 45)

    def test_load_data_function_failed(self):
        self.assertRaises(FileNotFoundError, lambda : load_data_from_file('notexistedfile.json'))
        self.assertRaises(json.decoder.JSONDecodeError, lambda : load_data_from_file('data_test/test_users_dammed.json'))

    def test_search_user_name_found_correct_result(self):
        search = ControlCenter('data_test', should_print=False)
        search.search_for('user', 'name', fixtures.USERS[0]['name'])
        self.assertEqual(len(search.results), 1)
        self.assertEqual(search.results[0]['name'], fixtures.USERS[0]['name'])
        # because that user don't have a organization_id
        self.assertIsNone(search.results[0]['organization_name'])

    def test_search_user_name_found_correct_result_and_map_organization_name(self):
        search = ControlCenter('data_test', should_print=False)
        search.search_for('user', 'name', fixtures.USERS[1]['name'])
        self.assertEqual(len(search.results), 1)
        self.assertEqual(search.results[0]['name'], fixtures.USERS[1]['name'])
        self.assertIsNotNone(search.results[0]['organization_name'])
        self.assertEqual(search.results[0]['organization_name'], fixtures.ORGANIZATIONS[0]['name'])

    def test_search_user_organization_id_found_correct_result_and_map_organization_name(self):
        search = ControlCenter('data_test', should_print=False)
        search.search_for('user', 'organization_id', fixtures.ORGANIZATIONS[0]['_id'])
        self.assertEqual(len(search.results), 1)
        self.assertEqual(search.results[0]['name'], fixtures.USERS[1]['name'])
        self.assertIsNotNone(search.results[0]['organization_name'])
        self.assertEqual(search.results[0]['organization_name'], fixtures.ORGANIZATIONS[0]['name'])

    def test_search_user_tags_found_correct_result_and_map_organization_name(self):
        search = ControlCenter('data_test', should_print=False)
        search.search_for('user', 'tags', 'Hemlock')
        self.assertEqual(len(search.results), 1)
        self.assertEqual(search.results[0]['_id'], 45)

    def test_search_user_on_invalided_col(self):
        search = ControlCenter('data_test', should_print=False)
        search.search_for('user', 'XXXX', 'Hemlock')
        self.assertIsNone(getattr(search, 'results', None))

    def test_search_user_name_empty_result(self):
        search = ControlCenter('data_test', should_print=False)
        search.search_for('user', 'name', 'XXX')
        self.assertIsNone(getattr(search, 'results', None))

    def test_search_organization_name_found_correct_result(self):
        search = ControlCenter('data_test', should_print=False)
        search.search_for('organization', 'name', fixtures.ORGANIZATIONS[0]['name'])
        self.assertEqual(len(search.results), 1)
        self.assertEqual(search.results[0]['name'], fixtures.ORGANIZATIONS[0]['name'])

    def test_search_organization_shared_tickets_found_multiple_result(self):
        search = ControlCenter('data_test', should_print=False)
        search.search_for('organization', 'shared_tickets', 'false')
        self.assertEqual(len(search.results), 2)
        self.assertEqual(search.results[0]['name'], fixtures.ORGANIZATIONS[0]['name'])
        self.assertEqual(search.results[1]['name'], fixtures.ORGANIZATIONS[1]['name'])

    def test_search_organization_shared_tickets_found_one_result(self):
        search = ControlCenter('data_test', should_print=False)
        search.search_for('organization', 'shared_tickets', 'true')
        self.assertEqual(len(search.results), 1)
        self.assertEqual(search.results[0]['name'], fixtures.ORGANIZATIONS[2]['name'])

    def test_search_organization_tags_found_one_result(self):
        search = ControlCenter('data_test', should_print=False)
        search.search_for('organization', 'tags', 'Mclaughlin')
        self.assertEqual(len(search.results), 1)
        self.assertEqual(search.results[0]['_id'], 104)
        self.assertEqual(search.results[0]['users'], ['Harper Sandoval'])
        self.assertEqual(search.results[0]['tickets'], ['A Catastrophe in Korea (North)'])

    def test_search_organization_name_empty_result(self):
        search = ControlCenter('data_test', should_print=False)
        search.search_for('organization', 'name', 'XXX')
        self.assertIsNone(getattr(search, 'results', None))

    def test_search_ticket_return_multiple_result(self):
        search = ControlCenter('data_test', should_print=False)
        search.search_for('ticket', 'type', 'incident')
        self.assertEqual(len(search.results), 2)

        result_ids = [item['_id'] for item in search.results]
        self.assertTrue('436bf9b0-1147-4c0a-8439-6f79833bff5b' in result_ids)
        self.assertTrue('1a227508-9f39-427c-8f57-1b72f3fab87c' in result_ids)

    def test_search_ticket_id_return_correct_data_and_map_correct_data(self):
        search = ControlCenter('data_test', should_print=False)
        search.search_for('ticket', '_id', '436bf9b0-1147-4c0a-8439-6f79833bff5b')
        self.assertEqual(len(search.results), 1)

        self.assertEqual(search.results[0]['submitter_name'], 'John Floyd')
        self.assertEqual(search.results[0]['assignee_name'], 'Harper Sandoval')
        self.assertEqual(search.results[0]['organization_name'], 'Xylar')

if __name__ == '__main__':
    unittest.main()