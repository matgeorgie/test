Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Media:
  def __init__(self, title, creator, publish_year, genre):
    self.title = title
    self.creator = creator
    self.publish_year = publish_year
    self.genre = genre

  def display(self):
    print("Title: ", self.title)
    print("Creator: ", self.creator)
    print("Publish Year: ", self.publish_year)
    print("Genre: ", self.genre)
  
  def search(self, keyword):
    if keyword in self.creator or keyword in self.genre:
      print("Found: ", self.title)
    else:
      print("Not found.")

class Book(Media):
...   def __init__(self, title, author, publish_year, genre, page_count):
...     super().__init__(title, author, publish_year, genre)
...     self.page_count = page_count
... 
...   def display(self):
...     super().display()
...     print("Page Count: ", self.page_count)
... 
... class Magazine(Media):
...   def __init__(self, title, publisher, publish_year, genre, issue_number):
...     super().__init__(title, publisher, publish_year, genre)
...     self.issue_number = issue_number
...   
...   def display(self):
...     super().display()
...     print("Issue Number: ", self.issue_number)
... 
... class AudioBook(Book):
...   def __init__(self, title, author, publish_year, genre, page_count, audio_length):
...     super().__init__(title, author, publish_year, genre, page_count)
...     self.audio_length = audio_length
...   
...   def display(self):
...     super().display()
...     print("Audio Length: ", self.audio_length)
... 
... book1 = Book("Harry Potter", "J. K. Rowling", 2020, "Fiction", 300)
... book1.display()
... book1.search("J. K. Rowling")
... 
... print()
... magazine1 = Magazine("Collge Mate", "Kopab", 2021, "Technology", 1)
... magazine1.display()
... magazine1.search("Technology")
... 
... print()
... audiobook1 = AudioBook("Life of Pi", "Irrfan Khan", 2022, "Fiction", 400, 2.5)
... audiobook1.display()
