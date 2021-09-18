
# If we have a bunch of functions that we want to run
# all at once using a single object, it might make sense
# to create a class. Let's call this one 'BookParser'.
class BookParser():
    """Parses text files (books)."""

    # Of course we need our __init__ definition...
    # Let's have it kickstart our parse with 'check_missing()'
    def __init__(self, book_file):
        """Instantiates book instances."""

        self.book = book_file
        self.title = ""
        self.words = ""
        self.lines = ""
        self.herstory = ""
        self.check_missing()


    def check_missing(self):
        """Checks if book is missing."""
        
        try:

            with open(self.book, encoding='utf-8') as f:
                contents = f.read()
        # This exception will print a message if the file isn't found.
        except FileNotFoundError:
            print(f"{self.book} is missing...")

        # If the file is found, lets give it a proper title.
        # We'll save the title to our instance's attributes for later use.
        else:
            if self.book == 'Crash_Course_2\Alice1.txt':
                self.title = "Alice's Adventures in Wonderland"
            elif self.book == 'Crash_Course_2\Alice2.txt':
                self.title = "Through the Looking Glass"
            elif self.book == 'Crash_Course_2\Anne1.txt':
                self.title = "Anne of Green Gables"
            elif self.book == 'Crash_Course_2\Anne2.txt':
                self.title = "Anne of Avonlea"            

            # Once the proper title is copied, we're off to the next method!
            self.count_words()


    def count_words(self):
        """Counts approx. total words in book."""
        
        with open(self.book, encoding='utf-8') as f:
            contents = f.read()
            words = contents.split()
            self.words = len(words)
            print(f"{self.title} has approx. {self.words} words.")
 
        self.count_lines()
    

    def count_lines(self):
        """Counts approx. total lines in book."""

        with open(self.book, encoding='utf-8') as f:
            contents = f.read()
            lines = contents.count('\n')
            self.lines = lines
            print(f"{self.title} has approx. {self.lines} lines.")

        self.count_her()

    def count_her(self):
        """Counts approx. total times the word 'her' is written in book."""

        with open(self.book, encoding='utf-8') as f:
            contents = f.read()
            her = contents.count(' her ')
            self.herstory = her
            print(f"{self.title} has approx. {self.herstory} occurences of the word 'her'.")        
