from typing import List

class Gift:
    """A gift wish a child has."""
    def __init__(self, name: str, price: float):
        """
        :param name: a simple description of the gift
        :param price: the expected price of the gift
        """
        self.name = name
        self.price = price

    def __repr__(self):
        """
        :return: a string representation of the gift for easier debugging
        """
        return f"Gift(name={self.name!r}, price={self.price!r})"

class Child:
    """A child that send wishes to santa."""
    def __init__(self, name: str, country: str, wishes: List[Gift]):
        """
        :param name: the name of the child
        :param country: the country the child is from (as a country code)
        :param wishes: a list of gift wishes
        """
        self.name = name
        self.country = country
        self.wishes = wishes
    
    def __repr__(self):
        """
        :return: a string representation of the child for easier debugging
        """
        return f"Child(name={self.name!r}, country={self.country!r}, wishes={self.wishes!r})"

# this is an example list of children for you to test your code with
children = [
    Child("Hans", "DE", [
        Gift("Toy Car", 12.44),
        Gift("Bike", 120.0),
        Gift("Board Game", 4.29),
    ]),
    Child("Henno", "DE", [
        Gift("Video Game", 59.00),
        Gift("Bike", 109.99),
    ]),
    Child("Peter", "GB", [
        Gift("Smartphone", 399.89),
    ]),
    Child("John", "US", []),
    Child("Brian", "GB", [
        Gift("Toy Car", 14.41),
        Gift("Board Game", 31.59),
    ]),
]

# define your helper functions here

if __name__ == "__main__":
    pass # your code goes here
