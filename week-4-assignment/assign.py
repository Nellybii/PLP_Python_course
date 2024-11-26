def read_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read() 

        modified_content = content.upper()

        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)  

        print(f"File has been successfully modified and saved as {output_filename}")

    except FileNotFoundError:
        print(f"The file {input_filename} was not found.")
    except IOError:
        print(f"Error reading or writing to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def handle_file_errors():
    filename = input("Enter the filename you want to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()  
            print(f"File content:\n{content}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    input_filename = input("Enter the input filename to read: ")
    output_filename = input("Enter the output filename to save modified content: ")
    read_and_write_file(input_filename, output_filename)

    handle_file_errors()

if __name__ == "__main__":
    main()
