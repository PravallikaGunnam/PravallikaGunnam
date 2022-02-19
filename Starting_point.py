import all_operations as ao

#program starting point
def main():
    try:
        #my_sql=mysqlOperations(dbname)
        db = ao.BasicSqlOperation()
        while True:
            operation = int(input("Choose the db operation you want to perform..\n --Press 1 for create table\n --Press 2 for inserting the value \n --Press 3 for deleting the value\n --Press 4 for updating the value\n --press 5 to show all data\n"))
            if operation == 1:
                db.create_table()
            elif operation == 2:
                db.inserting_into_table()
            elif operation == 3:
                db.deleting_from_table()
            elif operation == 4:
                db.update_into_table()
            elif operation == 5:
                db.show_data_form_table()
            else:
                print("Invalid Section!!!")
            choice=input("Do you want to continue with new operation y/n")
            if choice.upper() == "Y" or choice == "y":
                continue
            else:
                break
    except Exception as ex:
        print(ex)

# run the program
if __name__ == "__main__":
    main()