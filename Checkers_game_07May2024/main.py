import checkers

if __name__ == "__main__":
    def game():
        n = int(input("Please a number between 4 and 16 for creating a square board:  \n"))

        # calling build_board function
        new_bd = checkers.build_board(n)
        print("\nGenerated Square board: \n")
        print(new_bd)

        # calling get_count function
        count_bd_items = checkers.get_count(new_bd)
        for key, value in count_bd_items.items():
            print(f"Count of {key}: {value}\n")

        # extended challenges
        # calling pivot function
        pivot_board = checkers.pivot(new_bd)
        print("Pivoted Square Board: \n")
        print(pivot_board)

        # calling change_size function if necessary
        prompt = input("Would you like to change the size of the board? (y/n) \n")
        while prompt != 'n':
            n = int(input("Please a number between 4 and 16 for creating a square board: \n"))
            resized_board = checkers.change_size(new_bd, n)
            print("Resized Square Board: \n")
            print(resized_board)
            prompt = input("Would you like to change the size of the board? (y/n) \n")
        print("Goodbye!")


    game()
