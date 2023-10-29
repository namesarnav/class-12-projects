import mysql.connector
import time

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="contact"
)

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS book (
        name char(30) primary key,
        address char(100),
        mobile char(15),
        email char(30)
    );
""")


def intro():
    print("=" * 80)
    print("{:^80s}".format("CONTACT"))
    print("{:^80s}".format("BOOK"))
    print("{:^80s}".format("PROJECT"))
    print("{:^80s}".format("MADE BY: PyForSchool.com"))
    print("=" * 80)
    print()
    time.sleep(2)


def create_record():
    name = input("Enter name: ")
    address = input("Enter address: ")
    mobile = input("Enter mobile: ")
    email = input("Enter email: ")
    sql = "INSERT INTO book(name,address,mobile,email) VALUES (%s,%s,%s,%s)"
    record = (name, address, mobile, email)
    cursor.execute(sql, record)
    db.commit()
    print("Record Entered Successfully\n")


def search(name):
    sql = "SELECT * FROM book WHERE name = %s"
    value = (name,)
    cursor.execute(sql, value)
    record = cursor.fetchone()
    if record is None:
        print("No such record exists")
    else:
        print('Name:', record[0])
        print('Address:', record[1])
        print('Mobile:', record[2])
        print('E-mail:', record[3])


def display_all():
    cursor.execute("SELECT * FROM book")
    print('{0:20}{1:30}{2:15}{3:30}'.format('NAME', 'ADDRESS', 'MOBILE NO', 'E-MAIL'))
    for record in cursor:
        print('{0:20}{1:30}{2:15}{3:30}'.format(record[0], record[1], record[2], record[3]))


def delete_record(name):
    sql = "DELETE FROM book WHERE name = %s"
    value = (name,)
    cursor.execute(sql, value)
    db.commit()
    if cursor.rowcount == 0:
        print("Record not found")
    else:
        print("Record deleted successfully")


def modify_record(name):
    sql = "SELECT * FROM book WHERE name = %s"
    value = (name,)
    cursor.execute(sql, value)
    record = cursor.fetchone()
    if record is None:
        print("No such record exists")
    else:
        while True:
            print("\nPress the option you want to edit: ")
            print("1. Name")
            print("2. Address")
            print("3. Mobile")
            print("4. BACK")
            print()
            ch = int(input("Select Your Option (1-4): "))
            if ch == 1:
                new_name = input("Enter new name: ")
                sql = "UPDATE book SET name = %s WHERE name = %s"
                values = (new_name, name)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "record updated successfully")
            elif ch == 2:
                new_address = input("Enter new address: ")
                sql = "UPDATE book SET address = %s WHERE name = %s"
                values = (new_address, name)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "record updated successfully")
            elif ch == 3:
                new_mobile = input("Enter new mobile : ")
                sql = "UPDATE book SET mobile = %s WHERE name = %s"
                values = (new_mobile, name)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "record updated successfully")
            elif ch == 4:
                break
            else:
                print("Invalid choice !!!\n")


def main():
    intro()
    while True:
        print("\nMAIN MENU ")
        print("1. ADD NEW RECORD")
        print("2. SEARCH RECORD")
        print("3. DISPLAY ALL RECORDS")
        print("4. DELETE RECORD")
        print("5. MODIFY RECORD")
        print("6. EXIT")
        print()
        ch = int(input("Select Your Option (1-6): "))
        print()
        if ch == 1:
            print("ADD NEW RECORD")
            create_record()
        elif ch == 2:
            print("SEARCH RECORD BY NAME")
            name = input("Enter name: ")
            search(name)
        elif ch == 3:
            print("DISPLAY ALL RECORDS")
            display_all()
        elif ch == 4:
            print("DELETE RECORD")
            name = input("Enter name: ")
            delete_record(name)
        elif ch == 5:
            print("MODIFY RECORD")
            name = input("Enter name: ")
            modify_record(name)
        elif ch == 6:
            print("Thanks for using Contact Book")
            db.close()
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()