from supply_chain import WarehouseDatabase, RouteDatabase, Warehouse, Route
import os
import time

def menu():
    c = ''
    while c not in ['1','2','3','4','5','6','7','8','9','Q','q']:
        print()
        print('   PLEASE SELECT CODE FROM MENU  ')
        print('+-------------------------------+')
        print('| 1- Add Warehouse              |')
        print('| 2- Edit Warehouse             |')
        print('| 3- Remove Warehouse           |')
        print('| 4- Add Route                  |')
        print('| 5- Edit Delivery Cost         |')
        print('| 6- Delete Route               |')
        print('| 7- Find optimal route         |')
        print('| 8- Display Warehouses         |')
        print('| 9- Display Network            |')
        print('| Q- Quit                       |')
        print('+-------------------------------+')
        c = input('Your selection: ')
        os.system("cls")
    return c

if __name__ == "__main__":
    # Variables
    warehouse_file = "./data/warehouse_database.csv"
    route_file = "./data/route_database.csv"
    origin_id = destination_id = 0
    c = ''
    db = WarehouseDatabase()
    rdb = RouteDatabase()
    db.load_from_csv(warehouse_file)
    rdb.load_from_csv(route_file)
    # Main code
    print('WELCOME TO WAREHOUSE MANAGER 1.0')
    while c != 'Q' and c != 'q':
        c = menu()
        while c == '1':
            item = Warehouse()
            item.input_data()
            if not db.check_warehouse(item.item_name):
                db.add_warehouse(item)
                print('Successfully!')
                time.sleep(1)
                os.system('cls')
                break
            else:
                print('This warehouse already exists')
                print('Please change your Warehouse name or edit Warehouse')
                Warehouse.next_id -= 1
                time.sleep(2)
                os.system('cls')
        if c == '2':
            if not db.edit_item():
                print("Try editing again or return to main menu.")
                time.sleep(2)
            os.system('cls')
            rdb.apply_warehouse_edit(db.name_old, db.name_new)
        if c == '3':
            db.show_item()
            print()
            item_name = input("Enter the Warehouse name that you want to remove: ")
            if db.remove_item(item_name):
                rdb.apply_warehouse_remove(db.name_old)
                Warehouse.next_id -= 1
            else:
                print("Warehouse not found.")
            time.sleep(2)  
            os.system('cls')
        if c == '4':
            item = Route()
            try:
                item.input_data()
                if not rdb.check_route(item.origin, item.destination):
                    rdb.add_route(item)
                    print("Route added successfully!")
                    time.sleep(2)  # Give user time to read the success message.
                else:
                    print("This route already exists or there is an issue with the warehouse names.")
                    time.sleep(2)  # Give user time to read the error message.
            except ValueError as e:
                print(f"Invalid input: {e}")
                time.sleep(2)  # Give user time to read the error message.
            except Exception as e:
                print(f"An error occurred: {e}")
                time.sleep(2)  # Give user time to read the error message.
            os.system('cls')

        if c == '5':
            if not rdb.edit_route():  # No need to pass None here, function needs no arguments
                print("No changes were made. Try again or return to main menu.")
                time.sleep(2)
            os.system('cls')

        if c == '6':
            rdb.remove_item()
            os.system('cls')
        if c == '7':
            start_name = input("Enter the name of the starting warehouse: ")
            end_name = input("Enter the name of the destination warehouse: ")
            cost, path = rdb.find_optimal_route(start_name, end_name)
            if isinstance(cost, str):
                print(cost)
            else:
                print(f"The optimal path cost is {cost}")
                print(f"The optimal path is: {' -> '.join(path)}")
            input('Press Enter to continue..')
            os.system('cls')
        if c == '8':
            db.show_item()
            print()
            input('Done Reading? Press Enter to continue..')
            os.system('cls')
        if c == '9':
            rdb.show_item()
            print()
            input('Done Reading? Press Enter to continue..')
            os.system('cls')
        db.save_to_csv(warehouse_file)
        rdb.save_to_csv(route_file)
