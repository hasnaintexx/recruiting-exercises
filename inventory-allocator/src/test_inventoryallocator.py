import unittest
from inventoryallocator import InventoryAllocator, Orders, InventoryDistribution

##########################################
#        INSTRUCTIONS FOR TESTING        #
##########################################

#        run the following code:         #

# $ python test_inventoryallocator.py    #

##########################################


class InventoryAllocatorTest(unittest.TestCase):

    def test_single_order(self):
        print("\nTesting: test_single_order")
        order = Orders({'apple': 3})
        InvDist = InventoryDistribution([{'name': 'owd', 'inventory': {'apple': 10, 'banana': 5, 'orange': 45}}])
        IA = InventoryAllocator()
        expected = [{'owd': {'apple': 3}}]
        self.assertEqual(expected, IA.allocator(order, InvDist))
        print("Passed")

    def test_multiple_orders(self):
        print("\nTesting: test_multiple_orders")
        order = Orders({'apple': 3, 'banana': 3, 'orange': 5})
        InvDist = InventoryDistribution([{'name': 'owd', 'inventory': {'apple': 10, 'banana': 15, 'orange': 45}}])
        IA = InventoryAllocator()
        expected = [{'owd': {'apple': 3, 'banana': 3, 'orange': 5}}]
        self.assertEqual(expected, IA.allocator(order, InvDist))
        print("Passed")

    def test_split_order_across_distribution(self):
        print("\nTesting: test_split_order_across_distribution")
        order = Orders({'apple': 10, 'banana': 10, 'orange': 5})
        InvDist = InventoryDistribution([{'name': 'owd', 'inventory': {'apple': 5, 'banana': 5, 'orange': 10}}, \
                                         {'name': 'dm', 'inventory': {'apple': 5, 'banana': 5, 'orange': 10}}])
        IA = InventoryAllocator()
        expected = [{'owd': {'apple': 5, 'banana': 5, 'orange': 5}}, {'dm':{'apple': 5, 'banana': 5}}]
        self.assertEqual(expected, IA.allocator(order, InvDist))
        print("Passed")

    def test_No_inventory(self):
        print("\nTesting: test_No_inventory")
        order = Orders({'apple': 3})
        InvDist = InventoryDistribution([{'name': 'owd', 'inventory': {'apple': 0, 'banana': 5, 'orange': 45}}])
        IA = InventoryAllocator()
        expected = "{}\n\nUnfufilled Order: {}".format([],{'apple': 3})
        self.assertEqual(expected, IA.allocator(order, InvDist))
        print("Passed")

    def test_Not_enough_inventory(self):
        print("\nTesting: test_Not_enough_inventory")
        order = Orders({'apple': 3})
        InvDist = InventoryDistribution([{'name': 'owd', 'inventory': {'apple': 1, 'banana': 5, 'orange': 45}}])
        IA = InventoryAllocator()
        expected = "{}\n\nUnfufilled Order: {}".format([{'owd': {'apple': 1}}], {'apple': 2})
        self.assertEqual(expected, IA.allocator(order, InvDist))
        print("Passed")

    def test_split_with_not_enough_inventory(self):
        print("\nTesting: test_split_with_not_enough_inventory")
        order = Orders({'apple': 15})
        InvDist = InventoryDistribution([{'name': 'owd', 'inventory': {'apple': 5, 'banana': 5, 'orange': 10}},\
                                         {'name': 'dm', 'inventory': {'apple': 5, 'banana': 5, 'orange': 10}}])
        IA = InventoryAllocator()
        expected = "{}\n\nUnfufilled Order: {}".format([{'owd': {'apple': 5}},\
                                                        {'dm':{'apple': 5}}], {'apple': 5})
        self.assertEqual(expected, IA.allocator(order, InvDist))
        print("Passed")

    def test_negative_inventory(self):
        print("\nTesting: test_negative_inventory")
        order = Orders({'apple': 2})
        InvDist = InventoryDistribution([{'name': 'owd', 'inventory': {'apple': -1, 'banana': 5, 'orange': 10}},\
                                         {'name': 'dm', 'inventory': {'banana': 5, 'orange': 10}}])
        IA = InventoryAllocator()
        expected = "{}\n\nUnfufilled Order: {}".format([], {'apple': 2})
        self.assertEqual(expected, IA.allocator(order, InvDist))
        print("Passed")

    def test_negative_order(self):
        print("\nTesting: test_negative_order")
        order = Orders({'apple': -2})
        InvDist = InventoryDistribution([{'name': 'owd', 'inventory': {'apple': 5, 'banana': 5, 'orange': 10}}])
        IA = InventoryAllocator()
        expected = []
        self.assertEqual(expected, IA.allocator(order, InvDist))
        print("Passed")

    def test_no_order(self):
        print("\nTesting: test_no_order")
        order = Orders({})
        InvDist = InventoryDistribution([{'name': 'owd', 'inventory': {'apple': 5, 'banana': 5, 'orange': 10}}])
        IA = InventoryAllocator()
        expected = []
        self.assertEqual(expected, IA.allocator(order, InvDist))
        print("Passed")

    def test_no_inventory_distribution(self):
        print("\nTesting: test_no_inventory")
        order = Orders({'apple': 2})
        InvDist = InventoryDistribution([])
        IA = InventoryAllocator()
        expected = "{}\n\nUnfufilled Order: {}".format([], {'apple': 2})
        self.assertEqual(expected, IA.allocator(order, InvDist))
        print("Passed")

    def test_no_order_and_inventory_distribution(self):
        print("\nTesting: test_no_inventory")
        order = Orders({})
        InvDist = InventoryDistribution([])
        IA = InventoryAllocator()
        expected = []
        self.assertEqual(expected, IA.allocator(order, InvDist))
        print("Passed")

if __name__ == '__main__':
    print('\n' + '-' * 40)
    print(' Running Tests for InventoryAllocator')
    print('-' * 40, '\n')
    unittest.main()

