"""
This module contains Admin class
"""

from user import User
from privileges import Privileges

class Admin(User):
  """
  A simple attempt to model Admins.
  """
  def __init__(self, first_name, last_name, age, gender):
    super().__init__(first_name, last_name, age, gender)
    self.privileges = Privileges()