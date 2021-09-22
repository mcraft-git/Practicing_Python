
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
            # The 'read()' method returns a specified number of bytes from the file
            # (with the default being '-1', or the full file),
            # and copies them to our variable "contents".
            contents = f.read()
            # The 'split()' method separates a string into parts whereever it finds a space,
            # then stores all of those parts in a list, and copies that list to "words".
            words = contents.split()
            # The len() method counts the list items, and we save this number to 'self.words'.
            # In this way we have an approximation of how many words are written in the text.
            self.words = len(words)
            print(f"{self.title} has approx. {self.words} words.")
 
        self.count_lines()
    

    def count_lines(self):
        """Counts approx. total lines in book."""

        with open(self.book, encoding='utf-8') as f:
            contents = f.read()
            # The 'count()' method iterates over the file, counting all 
            # occurences of the argument that is passed to it.
            # Here we look for the number of newlines in the file.
            lines = contents.count('\n')
            self.lines = lines
            print(f"{self.title} has approx. {self.lines} lines.")

        self.count_her()

    def count_her(self):
        """Counts approx. total times the word 'her' is written in book."""

        with open(self.book, encoding='utf-8') as f:
            contents = f.read()
            # Without the space characters on either side of the word "her",
            # count() would include any word containing those three consecutive letters,
            # such as "there" or "where".
            her = contents.count(' her ')
            self.herstory = her
            print(f"{self.title} has {self.herstory} occurences of the word 'her'.")        
