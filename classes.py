""" how to use this

import classes
from classes import User
classes.User.__doc__ # returns doctext



"""

class Restaurant():
    """ a class for restaurants"""
    def __init__(self, name, food_type):
        self.name = name
        self.cuisine = food_type
        self.number_served = 0
        
    def describe_rest(self):
        """prints the info about the restaurant"""
        print('The name of the restaurant is '+ self.name.title())
        print('The type of food is ' + self.cuisine)
    
    def open_restaurant(self):
        """Let's people know the restaurant is open for business"""
        print(self.name + ' is open for business!!!')
        
    def set_number_served(self, n):
        """set the number served"""
        self.number_served = n
        
    def increment_number_served(self,n):
        """increment the number served"""
        self.number_served += n
        

class User():
    """info for each user"""
    def __init__(self,name,number_1_issue_currently):
        self.name = name
        self.passion = number_1_issue_currently
    
    def describe_user(self):
        print('Your name is ' + self.name)
        print('Your number one issue currently is ' + self.passion)
    
    def greet_user(self):
        print('Hello ' + self.name)


class Employee():
    
    def __init__(self,first_name,last_name,annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        
    def give_raise(self,annual_amount='5000'):
        self.annual_salary += annual_amount

employee = Employee('Derel','Merel',80000)
print(employee.first_name + ' ' + employee.last_name.title() + ' makes ' + str(employee.annual_salary))