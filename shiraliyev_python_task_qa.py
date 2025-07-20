# Project Name: Shiraliyev_Python_Task
# This code solves the algorithm part of the Andersen QA Automation Trainee task.
# It interactively takes values from the user and prints results according to the given conditions.
# It also includes a function to check the correctness of a bracket sequence.

def check_number_condition():
    """
    Prompts the user to enter an integer.
    If the number is greater than 7, it prints 'Hello'.
    Asks again on invalid input.
    """
    while True:
        try:
            num_input = input("Please enter a number (e.g., 10): ")
            number = int(num_input)
            if number > 7:
                print("Hello")
            else:
                print(f"The number you entered ({number}) is not greater than 7.")
            break
        except ValueError:
            print("Error: Invalid input! Please enter an integer.")

def check_name_condition():
    """
    Prompts the user to enter a name.
    If the name matches 'John', it prints 'Hello, John', otherwise it prints 'There is no such name'.
    """
    name_input = input("Please enter a name (e.g., Elshan): ")
    if name_input == "John":
        print("Hello, John")
    else:
        print("There is no such name")

def filter_multiples_of_3_from_array():
    """
    Prompts the user to enter a numeric array (numbers separated by commas).
    Prints only the elements of the array that are multiples of 3.
    Asks again on invalid input.
    """
    while True:
        array_str_input = input("Please enter a numeric array (separate numbers with commas, e.g., 1,3,5,6,9,10): ")
        try:
            # Converts the entered string into a list of integers.
            # strip() removes whitespace around each element.
            numeric_array = [int(item.strip()) for item in array_str_input.split(',')]
            
            multiples_of_3 = []
            for element in numeric_array:
                if element % 3 == 0:
                    multiples_of_3.append(element)
            
            if multiples_of_3:
                print("Array elements divisible by 3:", multiples_of_3)
            else:
                print("No elements divisible by 3 found in the array.")
            break
        except ValueError:
            print("Error: Invalid array format! Please enter numbers separated by commas.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def check_brackets(sequence):
    """
    Checks if the given bracket sequence is correct.
    Can be used for syntactic validation in QA.
    """
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    
    for char in sequence:
        if char in mapping.values(): # If it's an opening bracket
            stack.append(char)
        elif char in mapping.keys(): # If it's a closing bracket
            if not stack or mapping[char] != stack.pop():
                return False # If stack is empty or no matching bracket
    
    return not stack # If stack is empty, all brackets are correctly closed

def main():
    """
    Main execution function of the program.
    Calls all task parts sequentially.
    """
    print("--- Number Condition Check ---")
    check_number_condition()
    
    print("\n--- Name Condition Check ---")
    check_name_condition()
    
    print("\n--- Filtering Multiples of 3 from Array ---")
    filter_multiples_of_3_from_array()
    
    print("\n--- Bracket Sequence Check ---")
    seq = "[((())()(())]]"
    is_valid = check_brackets(seq)
    print(f"Bracket sequence '{seq}' is {'correct' if is_valid else 'not correct'}.")

    if not is_valid:
        # Explanation regarding the correction of the bracket sequence.
        print("To make it correct, the last ']' bracket must be removed. Correct example: [((())()(()))]")

if __name__ == "__main__":
    main()
