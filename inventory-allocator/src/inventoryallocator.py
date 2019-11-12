class InventoryAllocator:

    # Allocates orders to the given inventory distribution.
    # Assumes first warehouse in the list is the cheapest to ship from.

    def allocator(self, Orders, InventoryDistribution):
        output = []
        for i in range(len(InventoryDistribution.get_inventoryDistribution())):  # Loop through warehouses
            # initialize the allocation
            order_allocation = dict()

            # Create a list containing all the products (keys) found in both the current warehouse inventory and order.
            shared_inventory = set(Orders.get_order().keys()) & set(InventoryDistribution.get_inventoryDistributionIndex(i)['inventory'].keys())

            # Check whether or not ordered products are in the current warehouse
            if len(shared_inventory) > 0:
                for product in shared_inventory:  # Loop through products

                    # Check if the order quantity is a positive value.
                    if Orders.get_order()[product] <= 0:
                        # Delete order if a negative quantity value is assigned
                        del Orders.get_order()[product]

                    # Check if the inventory quantity is a positive value
                    elif InventoryDistribution.get_inventoryDistributionIndex(i)['inventory'][product] <= 0:
                        # Skip to next product
                        pass

                    # Check if there is enough product in current warehouse inventory
                    elif InventoryDistribution.get_inventoryDistributionIndex(i)['inventory'][product] >= Orders.get_order()[product]:
                        # Calculate difference between inventory quantity and order quantity
                        v = InventoryDistribution.get_inventoryDistributionIndex(i)['inventory'][product] - Orders.get_order()[product]

                        # Update warehouse inventory to the calculated value above
                        InventoryDistribution.get_inventoryDistributionIndex(i)['inventory'].update({product:v})

                        # Add the order allocation for current warehouse
                        order_allocation[product] = Orders.get_order()[product]

                        # Delete the order from the order list
                        del Orders.get_order()[product]

                    # If the warehouse cannot fully fulfill the order
                    else:
                        # Calculate difference between inventory quantity and order quantity
                        v = Orders.get_order()[product] - InventoryDistribution.get_inventoryDistributionIndex(i)['inventory'][product]

                        # Add the order allocation for current warehouse
                        order_allocation[product] = InventoryDistribution.get_inventoryDistributionIndex(i)['inventory'][product]

                        # Update the order quantity to the calculated value above
                        Orders.get_order()[product] = v

                        # Update warehouse inventory to 0
                        InventoryDistribution.get_inventoryDistributionIndex(i)['inventory'].update({product:0})

                # Checks to see if any orders were allocated
                if len(order_allocation) == 0:
                    # Skip to next warehouse
                    pass

                # If orders were allocated
                else:
                    # Create current warehouses order
                    output_allocation = {InventoryDistribution.get_inventoryDistributionIndex(i)['name']: order_allocation}
                    # Add the warehouse order to the output list
                    output.append(output_allocation)

        # Check to see if there are any orders unfufilled
        if len(Orders.get_order()) > 0:

            # Display unfufilled orders with output
            return "{}\n\nUnfufilled Order: {}".format(output,Orders.get_order())

        return output


class Orders:

    def __init__(self, order):  # Assigns order
        self.order = order

    def get_order(self):  # Pulls order
        return self.order


class InventoryDistribution:

    def __init__(self, warehouses):  # Assigns Inventory Distribution
        self.warehouses = warehouses

    def get_inventoryDistribution(self):  # Pulls Inventory Distribution
        return self.warehouses

    def get_inventoryDistributionIndex(self,i):  # Pulls specific warehouse from Inventory Distribution list
        return self.warehouses[i]








