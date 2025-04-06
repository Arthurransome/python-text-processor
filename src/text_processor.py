import sys

def read_file(file_path):
    """Read text from a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def process_text(text):
    """Process the text (count words, convert to uppercase)."""
    if not text:
        return None
    
    # Count words
    word_count = len(text.split())
    
    # Convert to uppercase
    uppercase_text = text.upper()
    
    return {
        "original_text": text,
        "word_count": word_count,
        "uppercase_text": uppercase_text
    }

def write_results(results, output_file):
    """Write the processed results to a file."""
    if not results:
       return False
    
    try:
        with open(output_file, 'w') as file:
            file.write(f"Original Text:\n{results['original_text']}\n\n")
            file.write(f"Word Count: {results['word_count']}\n\n")
            file.write(f"Uppercase Text:\n{results['uppercase_text']}\n")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

def main():
    """Main function to interact with the user or process with default arguments."""

    # If no command-line arguments are passed, go interactive
    if len(sys.argv) == 1:
        input_file = input("Enter the name of the input file (e.g., input.txt): ")
        output_file = input("Enter the name of the output file (e.g., output.txt): ")

        text = read_file(input_file)
        if text is None:
            return

        print("\nCurrent content of the input file:\n")
        print(text)

        choice = input("\nDo you want to edit the contents of the input file? (y/n): ").strip().lower()
        if choice == 'y':
            new_text = input("\nEnter new text for the input file:\n")
            try:
                with open(input_file, 'w') as f:
                    f.write(new_text)
                text = new_text
            except Exception as e:
                print(f"Error updating file: {e}")
                return

    else:
        # Non-interactive mode for GitHub Actions
        input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
        output_file = sys.argv[2] if len(sys.argv) > 2 else "output.txt"
        text = read_file(input_file)
        if text is None:
            print("\nProcessing failed: Could not read input file.")
            return

    results = process_text(text)
    if results:
        success = write_results(results, output_file)
        if success:
            print(f"\n Processing complete. Results written to '{output_file}'")
            return True

    print("\n Processing failed.")
    return False

if __name__ == "__main__":
    main()