"""This file should have our order classes in it."""

import random
import datetime


class AbstractMelonOrder(object):
    """basic class for melon orders"""
    
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = None
        self.tax = None
        self.timestamp = datetime.datetime.now()

    def get_base_price(self):
        """Implement splurge pricing."""
        
        extra_charge = 4
        
        if self.timestamp.weekday() < 5 and (self.timestamp.hour >= 8 and 
                                                self.timestamp.hour <= 11):
            # print "made it to the if statement."
            return random.randint(5,9) + extra_charge
        
        else:
            return random.randint(5,9)



    def get_total(self):
        """Calculate price."""
        base_price = float(self.get_base_price())
        # print "base_price before if xmas", base_price
        # base_price = 5
        if self.species == "Christmas Melon":
            base_price = base_price * 1.5
            # print "base_price in xmas", base_price
        
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty, "USA")
        
        # self.species = species
        # self.qty = qty
        # self.shipped = False
        # self.country_code ="USA"
        self.order_type = "domestic"
        self.tax = 0.08
        

    # def get_total(self):
    #     """Calculate price."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price
    #     return total

    # def mark_shipped(self):
    #     """Set shipped to true."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty, country_code)

        # self.species = species
        # self.qty = qty
        # self.country_code = country_code
        # self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price."""

        flat_rate = 3
        total = super(InternationalMelonOrder,self).get_total()
        if self.qty < 10:
            return total + flat_rate
        
        else:
        # print "im here yo!"
            return total

    # def mark_shipped(self):
    #     """Set shipped to true."""

    #     self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(GovernmentMelonOrder, self).__init__(species, qty, "USA")

        self.passed_inspection = False
        self.tax = 0

    def mark_inspection(self, passed):
        """Update the order after inspection.  Passed variable is boolean type."""

        self.passed_inspection = passed


