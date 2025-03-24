# A2. Define the House class with initialization attributes
class House:
    def __init__(self, house_number, street, area, number_of_beds, price):
        self.house_number = house_number
        self.street = street
        self.area = area
        self.number_of_beds = number_of_beds
        self.price = price

    # A3. Method to print all initialization attributes
    def print_attributes(self):
        print(f"House Number: {self.house_number}")
        print(f"Street: {self.street}")
        print(f"Area: {self.area}")
        print(f"Number of Beds: {self.number_of_beds}")
        print(f"Price: {self.price}")

    # A4. Methods to update attributes (1 method per attribute)
    def update_house_number(self, new_house_number):
        if isinstance(new_house_number, int):
            self.house_number = new_house_number
        else:
            print("Error: House number must be an integer.")

    def update_street(self, new_street):
        if isinstance(new_street, str):
            self.street = new_street
        else:
            print("Error: Street name must be a string.")

    def update_area(self, new_area):
        if isinstance(new_area, str):
            self.area = new_area
        else:
            print("Error: Area must be a string.")

    def update_number_of_beds(self, new_number_of_beds):
        if isinstance(new_number_of_beds, int):
            self.number_of_beds = new_number_of_beds
        else:
            print("Error: Number of beds must be an integer.")

    def update_price(self, new_price):
        if isinstance(new_price, float) or isinstance(new_price, int):
            self.price = new_price
        else:
            print("Error: Price must be a float or an integer.")


# A5. Create a child class of House with extra attributes
class LuxuryHouse(House):
    def __init__(self, house_number, street, area, number_of_beds, price, has_pool):
        super().__init__(house_number, street, area, number_of_beds, price)
        self.has_pool = has_pool

    # A6. Method to print all attribute values of the child class
    def print_attributes(self):
        super().print_attributes()
        print(f"Has Pool: {self.has_pool}")

    # A7. Methods to update extra attributes of the child class
    def update_has_pool(self, has_pool):
        if isinstance(has_pool, bool):
            self.has_pool = has_pool
        else:
            print("Error: 'Has pool' attribute must be a boolean value.")


# A8. Create instances for the classes above (tasks A2 and A5)
def main():
    # Create an instance of House
    house1 = House(123, "Oak Street", "Suburbia", 4, 500000)
    house1.print_attributes()

    # Create an instance of LuxuryHouse
    luxury_house1 = LuxuryHouse(456, "Palm Avenue", "Elite District", 6, 1500000, True)
    luxury_house1.print_attributes()

    # A9. Call the methods described in tasks A3 and A6
    print("\nUpdating attributes...")
    house1.update_house_number(456)
    house1.update_street("Maple Road")
    house1.print_attributes()

    print("\nUpdating extra attributes of child class...")
    luxury_house1.update_has_pool(False)
    luxury_house1.print_attributes()

    # A10. Examples of tasks A4 and A7
    print("\nExample of updating attributes (task A4):")
    house1.update_number_of_beds(5)
    house1.update_price(550000)
    house1.print_attributes()

    print("\nExample of updating extra attributes of child class (task A7):")
    luxury_house1.update_has_pool(True)
    luxury_house1.print_attributes()


if __name__ == "__main__":
    main()
