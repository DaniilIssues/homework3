database = []
database_filename = "data.txt"


def add():
    global database
    data = input("Input data:")
    database.append(data)


def print_data():
    global database

    if len(database) == 0:
        print("No data")

    for i in database:
        print(i)


def save():
    global database_filename
    global database
    with open(database_filename, "w") as f:
        f.write(",".join(database))


def load():
    global database_filename
    global database
    with open(database_filename, "r") as f:
        database = f.read().split(",")


def print_menu(menu):
    for i, m in enumerate(menu, start=1):
        print(f"{i}. {m}")


def get_command(menu):
    command = int(input("Input commmand: "))

    if 1 <= command <= len(menu):
        return command
    else:
        return -1


def delete():
    global database
    if len(database) == 0:
        print("No data")

    for i in database:
        database.remove(i)


def calculate():
    global database
    if len(database) == 0:
        print("No data")
    i = sum(database)

    print(i)


menu = ["Add", "Print","Calculate sum", "Save", "Load", "Delete", "Exit"]
commands = [add, print_data, calculate, save, load, delete, exit]

while True:
    print_menu(menu)
    command = get_command(menu)

    if command == -1:
        print("Wrong command!")
        continue

    commands[command - 1]()

