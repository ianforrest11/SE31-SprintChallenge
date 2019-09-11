from random import randint

class Product:
    """
    General representation of a product for Acme Corporation
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5, 
                 identifier=randint(1000000,9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """
        calculates the price divided by the weight of a given product, then determines
        level of 'stealability' via string output
        """
        steal_score = self.price / self.weight
        if steal_score < 0.5:
            return('Not so stealable...')
        elif steal_score < 1:
            return('Kinda stealable...')
        else:
            return('Very stealable!')

    def explode(self):
        """
        calculates the flammability times weight of a given product, then determines
        level of explosion via string output
        """
        explode_score = self.price / self.weight
        if explode_score < 10:
            return('...fizzle.')
        elif explode_score < 50:
            return('...boom!')
        else:
            return('...BABOOM!!')

class BoxingGlove(Product):
    """
    Create new BoxingGlove product subclass from Product class
    """
    def __init__(self, name, price=10, weight=10, flammability=0.5, 
                 identifier=randint(1000000,9999999)):
        super().__init__(name = name, price = price, weight = weight,
                         flammability = flammability, identifier = identifier)

    def explode(self):
        """
        update features of explode function for boxing glove product class
        return string value for any value of explode
        """
        return ("...it's a glove" )
    
    def punch(self):
        """
        calculates the punching power of a given boxing glove, then determines
        string output, based on weight of product
        """
        if self.weight < 5:
            return('That tickles.')
        elif self.weight < 15:
            return('Hey that hurt!')
        else:
            return('OUCH!')


# Of course, Acme doesn't just sell generic products - it sells all sorts of
# special specific things!

# Make a subclass of `Product` named `BoxingGlove` that does the following:

# - Change the default `weight` to 10 (but leave other defaults unchanged)
# - Override the `explode` method to always return "...it's a glove."
# - Add a `punch` method that returns "That tickles." if the weight is below 5,
#   "Hey that hurt!" if the weight is greater or equal to 5 but less than 15, and
#   "OUCH!" otherwise
  
# Example test run:

# ```python
# >>> from acme import BoxingGlove
# >>> glove = BoxingGlove('Punchy the Third')
# >>> glove.price
# 10
# >>> glove.weight
# 10
# >>> glove.punch()
# 'Hey that hurt!'
# >>> glove.explode()
# "...it's a glove."
# ```