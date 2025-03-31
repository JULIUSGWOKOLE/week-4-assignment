# assignment
# Week 4, Assignment: File Processing
# Purpose: Write a program that reads the content of a file, converts it to uppercase, and writes it to a new file.

def file_processor():
    # Get input filename with error handling
    while True:
        input_file = input("Enter the input filename: ")
        try:
            with open(input_file, 'r') as file:
                content = file.read()
            break  # Exit loop if file read successfully
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found. Please try again.")
        except PermissionError:
            print(f"Error: No permission to read '{input_file}'. Try another file.")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")

    # Process content (example: convert to uppercase)
    modified_content = content.upper()

    # Get output filename with validation
    while True:
        output_file = input("Enter the output filename: ")
        if output_file.strip() == "":
            print("Output filename cannot be empty!")
            continue
        if output_file == input_file:
            print("Output file must be different from input file!")
            continue
        try:
            with open(output_file, 'x') as file:  # 'x' mode prevents overwriting
                file.write(modified_content)
            print(f"Success! Modified content written to {output_file}")
            break
        except FileExistsError:
            print(f"Error: File '{output_file}' already exists. Choose another name.")
        except PermissionError:
            print(f"Error: Cannot write to '{output_file}'. Try another location.")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    print("=== File Modification Program ===")
    file_processor()