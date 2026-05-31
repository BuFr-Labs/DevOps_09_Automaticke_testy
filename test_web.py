import unittest
import requests

class TestWebAvailability(unittest.TestCase):
    def test_page_contains_string(self):
        # sem hodim bud svoji ECS url z minula nebo zalozni web (napr. seznam)
        url = "https://www.seznam.cz"
        
        # timeout je dulezity, at pipeline nezakysne, kdyz je web mrtvej
        response = requests.get(url, timeout=10)
        
        # kontrola, ze web vubec zije (status 200)
        self.assertEqual(response.status_code, 200, f"Web vratil error kod {response.status_code}")
        
        # overeni konkretniho textu na strance (podle zadani lektora napr. 'Firmy')
        search_string = "Firmy"
        
        # pokud string v HTML neni, test hodi error a python vrati exit code 1
        self.assertIn(search_string, response.text, f"Retezec '{search_string}' nenalezen v HTML!")

if __name__ == "__main__":
    unittest.main()