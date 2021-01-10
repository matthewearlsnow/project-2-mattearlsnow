# Author: Matthew Snow
# Date: January 8, 2021
# Description: This program is a shopping center checkout program! The player will add items
# to the store and create customers, then add certain items to the customer's carts. When they
# are ready, they can checkout and get the total price for the items in the cart

class InvalidCheckoutError(Exception):
    pass

class Product:
    """Initializes the product's data members"""
    def __init__(self, ID, title, description, price, quantity_available):
        self._ID = ID
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_product_id(self):
        """Returns ID"""
        return self._ID

    def get_title(self):
        """Returns title"""
        return self._title

    def get_description(self):
        """Returns description"""
        return self._description

    def get_price(self):
        """Returns price"""
        return self._price

    def get_quantity_available(self):
        """Returns quantity available"""
        return self._quantity_available

    def decrease_quanity(self):
        """Decreases quantity available by 1"""
        self._quantity_available -= 1


class Customer:
    """Initializes customer's name and ID"""
    def __init__(self, name, ID, premium_member=False):
        self._name = name
        self._ID = ID
        self._premium_member = premium_member
        self._customer_cart = []

    def get_customer_cart(self):
        """Returns Customer's cart"""
        return self._customer_cart

    def get_name(self):
        """Returns customer's name"""
        return self._name

    def get_ID(self):
        """Returns customer's ID"""
        return self._ID

    def is_premium_member(self):
        """Returns if customer is premium member or not"""
        return self._premium_member

    def add_product_to_cart(self, ID):
        """Takes a product ID code and adds it to the Customer's cart"""
        self._customer_cart.append(ID)

    def empty_cart(self):
        """ Empties the Customer's cart"""
        self._customer_cart = [self._customer_cart.remove(item) for item in self._customer_cart]



class Store:
    """Initializes the store"""
    def __init__(self):
        self._products = {}
        self._test_products = []
        self._customers = {}
        self._new_member = []
        self._new_cart = {}
        self._second_cart = set()

    def add_product(self, products):
        """ Takes a Product object and adds it to the inventory"""
        self._test_products.append(products)
        self.new_list = []
        self.new_list.append(products.get_product_id())
        self.new_list.append(products.get_title())
        self.new_list.append(products.get_description())
        self.new_list.append(products.get_price())
        self.new_list.append(products.get_quantity_available())
        self._products[self.new_list[0]] = self.new_list[1:]

    def add_member(self, customer):
        """Takes a Customer object and adds it to the membership"""
        self._new_member.append(customer)
        new_customer = []
        new_customer.append(customer.get_name())
        new_customer.append(customer.get_ID())
        new_customer.append(customer.is_premium_member())
        self._customers[new_customer[1]] = new_customer[0::2]


    def get_product_from_id(self, ID):
        """
        Takes a Product ID and returns the Product with the matching ID.
        If no matching ID is found in the inventory, it returns
        the special value None
        """
        for item in self._products:
            if str(ID) == item:
                return self._products[item]
        else:
            return None

    def get_member_from_id(self, ID):
        """Takes a Customer ID and returns the Customer with the matching ID"""
        for person in self._customers:
            if ID == person:
                return self._customers[ID][0]
        else:
            return None

    def product_search(self, search):
        """
        Takes a search string and returns a sorted (in lexicographic order) list of ID codes for every
        product in the inventory whose title or description contains the search string
        """
        product_list = []
        search = search.lower()

        for item in self._products:
            description = self._products[item][1].lower()
            title = self._products[item][0].lower()
            if search in description:
                product_list.append(item)
            elif search in title:
                product_list.append(item)
            product_list.sort()
        return product_list


    def add_product_to_member_cart(self, product_id, customer_id):
        """Takes a Product ID and a Customer ID (in that order) and adds products to customer's cart"""
        if product_id in self._products and customer_id in self._customers and Product.get_quantity_available != 0:
            for customer in self._new_member:
                customer_check = Customer.get_ID(customer)
                if customer_check == customer_id:
                    customer.add_product_to_cart(product_id)
        elif product_id not in self._products:
            return "product ID not found"
        elif product_id in self._products and customer_id not in self._customers:
            return "member ID not found"



    def check_out_member(self, customer_id):
        """
        Takes a Customer ID.  If the ID doesn't match a member of the Store, raise an **InvalidCheckoutError**
        Otherwise, will return the value of all the itmes in the cart
        """

        check_out = []
        total = 0
        if customer_id not in self._customers:
            raise InvalidCheckoutError
        if customer_id in self._customers:
            for person in self._new_member:
                if customer_id == Customer.get_ID(person):
                    test = Customer.get_customer_cart(person)
                    for item in test:
                        if item in self._products:
                            check_out.append(self._products[item][-2])
                    for amount in check_out:
                        total += amount
                    return total


p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
c1 = Customer("Matt", "MES", True)
p2 = Product("111", "Cake", "Big Cake", 6, 6)
c2 = Customer("Tim", "TJS", True)
p3 = Product("222", "STUFF", "Big CAKES", 7, 6)
myStore = Store()
myStore.add_product(p1)
myStore.add_member(c1)
myStore.add_product(p2)
myStore.add_member(c2)
myStore.add_product(p3)
myStore.add_product_to_member_cart("889", "MES")
myStore.add_product_to_member_cart("111", "MES")
myStore.add_product_to_member_cart("222", "TJS")



def main():
    try:
        print(myStore.check_out_member('TJS'))
    except InvalidCheckoutError:
        print(" **InvalidCheckoutError** ")

if __name__ == "__main__":
    main()