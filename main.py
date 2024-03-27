'''A basic text analysis program that reads a text file and counts the number of words and letters in the text file.'''

# Count the number of words and letters in a text file
def count_words(text: str) -> int:
    words = text.split()
    return len(words)

# Helper function to sort the dictionary based on the count
def sort_on(dict: dict) -> int:
    return dict['count']

# Count the number of letters in the text
def count_letters(text: str) -> dict:
    # Create a dictionary to store the count of each letter
    letter_count = {}
    for letter in text.lower(): 
        if letter.isalpha() == False: # Skip non-alphabetic characters
            continue
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
            
    # Sort the dictionary based on the count
    letter_count = [dict(letter=letter, count=count) for letter, count in letter_count.items()]
    letter_count.sort(key=sort_on, reverse=True)
   
    return letter_count

# Main function    
def main():
    # Read the text file
    book = 'frankenstein' # Change the book name to analyze a different book
    with open(f'books/{book}.txt', 'r') as f:
        text = f.read()
        
        # Print the text analysis
        print(f'--- Text Analysis of {book}---')
        print (f'Number of words in the text: {count_words(text)}')
        for letter in count_letters(text):
            print(f"Letter: {letter['letter']} Count: {letter['count']}")

if __name__ == '__main__':
    main()