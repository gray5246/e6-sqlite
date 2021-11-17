if __name__ == "__main__":
    import cafe_data
    import user_interface
    cafe_data.create_database()

    done = False
    while done != True:
        command1 = user_interface.get_command()
        if command1.lower() == "quit":
            done = True
        if command1.lower() == "list cafes":
            cafe_data.get_stores()
        if command1.lower() == "drop":
            cafe_data.destroyer(input("Table to demolish:"))
        if command1.lower() == "load tables":
            cafe_data.load_cafe_data()
