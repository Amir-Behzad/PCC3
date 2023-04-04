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


class Admin(User):
    """
    A simple attempt to model Admins.
    """

    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()
