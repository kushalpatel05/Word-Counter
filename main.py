def count_words_in_file(filename):
    try:
        # Open the file and read its content
        with open(filename, 'r') as file:
            content = file.read()
        
        # Split the content into words
        words = content.split()
        
        # Count the words
        word_count = len(words)
        
        print(f"The file '{filename}' contains {word_count} words.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    filename = input("Enter the filename: ")
    count_words_in_file(filename)
    
