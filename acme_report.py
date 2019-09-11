from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """
    create a function to randomly generate a list of products from 
    list of nouns and adjectives above
    """
    products = []

    for _ in range(num_products):
        name = ADJECTIVES[randint(0, len(ADJECTIVES)-1)] + \
            ' ' + NOUNS[randint(0, len(NOUNS)-1)]
        price = randint(10, 75)
        weight = randint(10, 75)
        flammability = uniform(0.0, 1)

        prod = Product(name=name, price=price, weight=weight,
                       flammability=flammability)
        products.append(prod)
    return products

def inventory_report(products):
    """
    create report that details specs of random products generated above
    """
    # Make sure parameter passed is actually a list object
    if not isinstance(products, list):
        raise TypeError('`products` - parameter passed must be a list')

    # Get length of products list
    n_prod = len(products)

    # Make sure lists always have the right products
    if n_prod < 1 or (products is None):
        return ValueError("`products` - parameter must be non-empty list.")

    tot_price, tot_wt, tot_flm = 0, 0, 0
    for product in products:
        tot_price += product.price
        tot_wt += product.weight
        tot_flm += product.flammability

    avg_price = tot_price / n_prod
    avg_wt = tot_wt / n_prod
    avg_flm = tot_flm / n_prod

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names:", len(set(products)))
    print("Average price:", avg_price)
    print("Average weight:", avg_wt)
    print("Average flammability:", avg_flm)


if __name__ == '__main__':
    inventory_report(generate_products())