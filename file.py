import sys


def main():
    # Check if the file name argument is provided
    if len(sys.argv) < 2:
        print("Error: Missing file name argument.")
        sys.exit(1)

    # Get the file name from the command-line argument
    file_name = sys.argv[1]

    try:
        # Open the file for reading
        with open(file_name, 'r') as file:
            line_number = 1  # To keep track of line numbers
            # Read each line from the file
            for line in file:
                line = line.strip()  # Remove any leading/trailing whitespace
                values = line.split()  # Split the line into a list of values

                # Try to convert the two values to floats and sum them
                try:
                    if len(values) != 2:
                        print(f"Error on line {line_number}: Expected two values, got {len(values)}")
                    else:
                        # Convert the values to float and calculate their sum
                        num1 = float(values[0])
                        num2 = float(values[1])
                        print(f"Line {line_number} sum: {num1 + num2}")
                except ValueError:
                    # Handle the case where one of the values cannot be converted to float
                    print(f"Error on line {line_number}: Non-numeric value")

                line_number += 1  # Move to the next line

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        sys.exit(1)


# Call the main function to execute the program
if __name__ == "__main__":
    main()
