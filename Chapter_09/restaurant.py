class Restaurant:
    """
    Restaurants are represented by their: 
      - name
      - cuisin type

    """

    def __init__(self, restaurant_name, cuisineType):
        self.name = restaurant_name
        self.cuisineType = cuisineType.lower()
        self.number_served = 0

    def describe_restaurant(self):
        text1 = f"Restaurant's name: {self.name}."
        text2 = f"The restaurant {self.name} serves {self.cuisineType}."
        print(10 * "---")
        print(text1)
        print(text2)
        print(10 * "---")

    def open_restaurant(self):
        print()
        print(10 * "---")
        text = f"{self.name} is open now."
        print(text)
        print(10 * "---")

    def set_number_server(self, cumtomers_served):
        self.number_served = cumtomers_served
