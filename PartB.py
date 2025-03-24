import unittest
from PartA import House, LuxuryHouse 

# B2. Unit test to check if an object is an instance of a class
class TestHouse(unittest.TestCase):

    def test_is_instance_of_house(self):
        test_cases = [
            (House(123, "Oak Street", "Suburbia", 4, 500000), House), 
            (LuxuryHouse(456, "Palm Avenue", "Elite District", 6, 1500000, True), LuxuryHouse) 
        ]
        
        for house, expected_class in test_cases:
            with self.subTest(house=house, expected_class=expected_class):
                self.assertIsInstance(house, expected_class)

    def test_is_not_instance_of_house(self):
        house = LuxuryHouse(456, "Palm Avenue", "Elite District", 6, 1500000, True)
        # Test if LuxuryHouse is NOT an instance of an unrelated class (checking if it's NOT an instance of 'str')
        self.assertNotIsInstance(house, str)  # A check to ensure that house is NOT a string


# B3. Unit test to check if two objects are identical
class TestObjectIdentity(unittest.TestCase):

    def test_objects_are_identical(self):
        house1 = House(123, "Oak Street", "Suburbia", 4, 500000)
        house2 = house1  # house2 points to the same object as house1
        self.assertIs(house1, house2)  # Objects should be identical

    def test_objects_are_not_identical(self):
        house1 = House(123, "Oak Street", "Suburbia", 4, 500000)
        house2 = House(456, "Palm Avenue", "Elite District", 6, 1500000)
        self.assertIsNot(house1, house2)  

# B4. Unit tests for update methods in House class (A4)
class TestHouseUpdates(unittest.TestCase):

    def test_update_methods(self):
        house = House(123, "Oak Street", "Suburbia", 4, 500000)

        update_cases = [
            ('house_number', 456, 456),  # Update house number
            ('street', "Maple Road", "Maple Road"),  # Update street
            ('area', "Downtown", "Downtown"),  # Update area
            ('number_of_beds', 5, 5),  # Update number of beds
            ('price', 550000, 550000)  # Update price
        ]
        
        for attribute, new_value, expected_value in update_cases:
            with self.subTest(attribute=attribute, new_value=new_value, expected_value=expected_value):
                getattr(house, f"update_{attribute}")(new_value)  
                self.assertEqual(getattr(house, attribute), expected_value) 


# B5. Main function to run all the tests
def main():
    # Run all the tests in this file
    unittest.main()

if __name__ == "__main__":
    main()
