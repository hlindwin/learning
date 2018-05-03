import unittest
from classes import Employee

class TestEmployeeClass(unittest.TestCase):
    """Tests the employee class"""
    
    def setUp(self):  # this has to be capital U: setUp vs setup
        """
        create employees so I don't have do this each time
        """
        self.my_employee = Employee('Derel','Merel',80000)
        self.salary = 80000
        self.name = 'Derel'
        self.last_name = 'Merel'
        
    def test_first_name(self):
        """Test that the first name worked"""
        self.assertEqual(self.my_employee.first_name, self.name)

unittest.main()