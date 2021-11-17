import cafe_data
def get_command():
    checker = False
    while checker != True:

        command = input("Choose a command: \n quit \n list cafes\n>")

        commands = ["quit", "list cafes"]
        if command.lower() in commands:
            checker = True
        else:
            print("Invalid command")
    return command
def display_table(dspy):
    pass