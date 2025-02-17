import unittest
from task_2 import *

class TestUserFunctions(unittest.TestCase):
    
    def test_average_age(self):
        test_users = [('Marcin', 20, 'Szczecin'),('Józef', 40, 'Warszawa')]

        results = get_average_age(test_users)

        self.assertEqual(results, 30)
        
    def test_average_age_empty_list(self):
        test_users = []

        results = get_average_age(test_users)

        self.assertEqual(results, 0)
    
    
    def test_unique_cities(self):
        test_users = [('Marcin', 20, 'Szczecin'),('Józef', 40, 'Warszawa'),('Maciek', 40, 'Warszawa')]

        unique = get_unique_cities(test_users)

        self.assertTrue('Szczecin' in unique)
        self.assertTrue('Warszawa' in unique)
        self.assertFalse('Sopot' in unique)
        self.assertEqual(unique.count('Warszawa'), 1)

    def test_unique_cities_empty_list(self):
        test_users = []

        unique = get_unique_cities(test_users)

        self.assertEqual(unique, [])
    
    def test_sort_by_age(self):
        test_users = [('Marcin', 20, 'Szczecin'),('Józef', 40, 'Warszawa'),('Maciek', 41, 'Warszawa')]
        
        sorted_users = get_sorted_by_age(test_users)

        self.assertEqual(sorted_users[0][1], 20)  
        self.assertEqual(sorted_users[-1][1], 41) 
    
    def test_sort_by_age_empty_list(self):
        test_users = []
        
        sorted_users = get_sorted_by_age(test_users)

        self.assertEqual(sorted_users, [])  
    
    def test_user_exists(self):
        testUsers = [('Janek', 20, 'Szczecin'),('Krystian', 40, 'Warszawa')]

        is_janek_exist = is_user_in_list(testUsers, 'Janek')
        is_krystian_exist = is_user_in_list(testUsers, 'Krystian')
        is_mariusz_exist = is_user_in_list(testUsers, 'Mariusz')

        self.assertTrue(is_janek_exist)
        self.assertTrue(is_krystian_exist)
        self.assertFalse(is_mariusz_exist)

    def test_user_exists_empty_list(self):
        testUsers = []
        
        is_janek_exist = is_user_in_list(testUsers, 'Janek')

        self.assertFalse(is_janek_exist)
    
    
    def test_filter_users_by_age_and_city_one_user(self):
        testUsers = [('Janek', 20, 'Warszawa'),('Krystian', 40, 'Warszawa')]
        filtered_users = get_filtered_users_by_age_and_city(testUsers, 39, 'Warszawa')
        self.assertEqual(len(filtered_users), 1)
        self.assertEqual(filtered_users[0][0], 'Krystian')

    def test_filter_users_by_age_and_city_more_users(self):
        testUsers = [('Janek', 50, 'Warszawa'),('Krystian', 40, 'Warszawa')]
        filtered_users = get_filtered_users_by_age_and_city(testUsers, 39, 'Warszawa')
        self.assertEqual(len(filtered_users), 2)

    def test_filter_users_by_age_and_city_empty_list(self):
        testUsers = []
        filtered_users = get_filtered_users_by_age_and_city(testUsers, 39, 'Warszawa')
        self.assertEqual(len(filtered_users), 0)

if __name__ == "__main__":
    unittest.main()