def read_and_modify_file(input_filename, output_filename):
    try:
        # Read the content of the input file
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"File '{input_filename}' has been successfully read and modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read or written.")

# Ask the user for the input and output filenames
input_filename = input("Enter the name of the file to read: ")
output_filename = input("Enter the name of the file to write the modified content to: ")

# Call the function to read and modify the file
read_and_modify_file(input_filename, output_filename)
