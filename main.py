if __name__ == "__main__":
    import cafe_data
    import user_interface
    cafe_data.create_database()
    cafe_data.load_cafe_data()
    done = False
    while done != True:
        command1 = user_interface.get_command()
        if command1.lower() == "quit":
            done = True
        if command1.lower() == "list cafes":
            cafe_data.get_stores()