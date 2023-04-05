"""
This module contains Privileges
"""



class User:
  """
  A simple attempt to model a user
  """
  def __init__(self, first_name, last_name, age, gender):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.gender = gender

  def describe_user(self):
    text1 = f"My name is {self.first_name} {self.last_name}."
    text2 = f"I'm {self.age} years old."
    print(text1)
    print(text2)


