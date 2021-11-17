import cafe_data
def get_command():
    checker = False
    while checker != True:

        command = input("Enter command: \nquit\nlist cafes\ndrop\nload tables\n>")

        commands = ["quit", "list cafes", "drop", "load tables"]
        if command.lower() in commands:
            checker = True
        else:
            print("Invalid command")
    return command
def display_table(dspy):
    pass