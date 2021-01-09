# Author: Matthew Snow
# Date: January 8, 2021
# Description:

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
    def __init__(self, name, ID, premium_member):
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
        self._customers = {}
        self._new_member = []
        self._new_cart = {}
        self._second_cart = []
    def add_product(self, products):
        """ Takes a Product object and adds it to the inventory"""
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
            if ID in person:
                return person[0]
            else:
                return None

    def product_search(self, search):
        """
        Takes a search string and returns a sorted (in lexicographic order) list of ID codes for every
        product in the inventory whose title or description contains the search string

        """
        product_list = []
        for item in self._products:
                if search in (self._products[item]):
                    product_list.append(item)
                    product_list.sort()
        return product_list


    def add_product_to_member_cart(self, product_id, customer_id):
        """
         Takes a Product ID and a Customer ID (in that order).  If the product isn't found in
         the inventory, return "product ID not found"
        """

        if product_id in self._products and customer_id in self._customers and Product.get_quantity_available != 0:
            for person in self._new_member:
                if customer_id == Customer.get_ID(person):
                    self._new_cart[customer_id] = product_id
                    print(self._new_cart)
        elif product_id not in self._products:
            return "product ID not found"
        elif product_id in self._products and customer_id not in self._customers:
            return "member ID not found"

    def check_out_member(self, customer_id):

        """
        Takes a Customer ID.  If the ID doesn't match a member of the Store, raise an **InvalidCheckoutError**
        """
        for person in self._new_member:
            if customer_id == Customer.get_ID(person):
                print('found')

        #else:
            #raise Exception("InvalidCheckoutError")

p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
c1 = Customer("Yinsheng", "QWF", False)
p2 = Product("999", "The Vow", "We are one", 44, 3)
c2 = Customer("Matt", "MES", True)
p3 = Product("111", "Cake", "Birthday Cake", 1, 8)
p4 = Product("222", "Snickers", "Big Snickers", 2, 4)
p5 = Product("333", "GUM", "BubleGUM", 33, 2)


myStore = Store()
myStore.add_product(p1)
myStore.add_product(p2)
myStore.add_member(c1)
myStore.add_member(c2)
myStore.add_product(p3)
myStore.add_product(p4)
myStore.add_product(p5)
myStore.add_product_to_member_cart("999","MES")
myStore.add_product_to_member_cart("999","QWF")
myStore.add_product_to_member_cart("111","MES")
#myStore.add_product_to_member_cart("222","MES")
#(myStore.add_product_to_member_cart("889","MES"))
#print(myStore.check_out_member('MES'))