#!/usr/bin/env python3

# Created By: Val Ijaola
# Date: November 5, 2023
# This program asks the user to enter three numbers,
# it then tells them which number is the smallest.


def main():
    print("Input 3 numbers, and I will tell you the smallest one.\n")
    # Input - getting first number
    first_num_str = input("What's your first number.\n")
    try:
        first_num_flt = float(first_num_str)
        # Input - getting second number
        second_num_str = input("What's your second number.\n")
        try:
            second_num_flt = float(second_num_str)
            # Input - getting third number
            third_num_str = input("What's your third number.\n")
            try:
                third_num_flt = float(third_num_str)
                # process - checking which number(s) is the smallest.
                if first_num_flt < second_num_flt and first_num_flt < third_num_flt:
                    # Output- Display result (smallest number)
                    print(f"{first_num_flt} is the smallest number.")
                elif second_num_flt < first_num_flt and second_num_flt < third_num_flt:
                    print(f"{second_num_flt} is the smallest number.")
                elif third_num_flt < first_num_flt and third_num_flt < second_num_flt:
                    print(f"{third_num_flt} is the smallest number.")
                else:
                    if (
                        first_num_flt == second_num_flt
                        and first_num_flt == third_num_flt
                    ):
                        print("All numbers are the same.")
                    elif (
                        first_num_flt == second_num_flt
                        and first_num_flt < third_num_flt
                    ):
                        print(f"{first_num_flt} is the smallest number.")
                    elif (
                        first_num_flt == third_num_flt
                        and first_num_flt < second_num_flt
                    ):
                        print(f"{first_num_flt} is the smallest number.")
                    else:
                        print(f"{second_num_flt} is the smallest number.")
            except ValueError:
                print(f"{third_num_str} is not a number.")
        except ValueError:
            print(f"{second_num_str} is not a number.")
    except ValueError:
        print(f"{first_num_str} is not a number.")
    finally:
        print("Thanks for using this program.")


if __name__ == "__main__":
    main()
