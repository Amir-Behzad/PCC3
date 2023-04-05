"""
Privileges as a seperate class.
"""

class Privileges:
  """
  Privileges of the Admin 
  """
  def __init__(self):
    pass
    self.privileges = [
      "can add post",
      "can delete post",
      "can ban user",
      'can reset passwords',
      'can moderate discussions',
      'can suspend accounts',
    ]

  def show_privileges(self):
    print("Admins have these privileges:\n")
    for item in self.privileges:
      print(item)