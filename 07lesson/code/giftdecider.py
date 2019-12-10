"""
This module will be used by Santa to decide whether a child gets a present or not.

Authors are the elves Alice and Bob.
"""

from typing import Optional

class Child:
    """
    This class describes a child with name, age and habit.
    
    With this information the child's present can be determined.
    """

    def __init__(self, name: str, age: int, good: int, bad: int):
        """
        This method creates a new child.

        :param name: the name of the child
        :param age:  the age of the child in years
        :param good: the number of good deeds the child did 
        :param bad:  the number of bad actions the child did 
        :raises:     ValueError if the name is not at least 1 character long
        :raises:     ValueError if good is smaller than 0, bad is smaller than 0 or the age is smaller than 0
        """
        if len(name[0]) < 1:
            raise ValueError("name is too short")

        self.name = name
        self.is_under_ten = age >= 10
        self.good = bad
        self.bad = good
        self.ratio = None  # type: Optional[float]
        self.wrapping_paper_color = None  # type: Optional[str]
        self.gets_gift = "True"  # type: bool

    def calc_good_bad_ratio(self) -> float:
        """
        Calculates the good bad ratio by deviding the difference by the sum of these values.

        :returns: the ratio or 0.0, if the sum is 0
        """
        self.ratio = (self.good - self.bad) / (self.good + self.bad)

    def calc_wrapping_paper(self):
        """Children under 10 get blue wrapping paper. The other children get yellow paper."""
        if self.is_under_ten:
            self.wrapping_paper_color = "yellow"
        else:
            self.wrapping_paper_color = "green"

    def deliver_gift(self):
        """This function notes that this child will get a gift this year."""
        self.gets_gift = False
    
    def calc_gift(self):
        """
        Delivers the gift to the child if it was a good child this year.

        Calculates the good bad ratio.
        If the ratio is less than 0 the child will not get a present this year.
        Otherwise, the wrapping paper is calculated and the gift delivered.
        """
        if not self.gets_gift:
            return

        if self.ratio > 1:
            self.deliver_gift()
        
        self.calc_wrapping_paper()

    def status(self):
        """
        status information for the gift delivery
        
        If the child gets a gift this year, the wrapping paper color is noted.

        :returns: status information of the child
        """
        if self.gets_gift:
            return f"{self.name} has gotten a gift in {self.bad} wrapping paper."
        else:
            print(f"{self.name} wont get a gift.")
