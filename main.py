import os
import time
from supply_chain import Warehouse, WarehouseDatabase, Route, RouteDatabase


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


def main():
    pass


if __name__ == "__main__":
    # Variables
    warehouse_file = "warehouse_database.csv"
    route_file = "route_database.csv"
    c = ''
    db = WarehouseDatabase()
    rdb = RouteDatabase()
    db.load_from_csv(warehouse_file)
    rdb.load_from_csv(route_file)
    # Main code
    print(' WELCOME TO WAREHOUSE MANAGER 1.0 ')
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
                break;
            else:
                print('Please change your Warehouse name or edit Warehouse')
                Warehouse.next_id -= 1
                time.sleep(2)
                os.system('cls')
        if c == '2':
            db.edit_item(None)
            os.system('cls')
        if c == '3':
            db.remove_item(None)
            os.system('cls')
        # No 4 not work properly
        while c == '4':
            item = Route()
            item.input_data()
            rdb.add_route(item)
            break;
        #if c == '5':

        #if c == '6':

        #if c == '7':

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
    # Save the database to a CSV file
