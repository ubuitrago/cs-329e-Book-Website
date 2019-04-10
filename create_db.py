# beginning of create_db.py
import json
from models import app, db, Book, Author, Publisher

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

def create_books():
    book = load_json('books.json')

    for oneBook in book['books']:
        title = oneBook['title']
        isbn = oneBook.get('isbn')
        imageURL = oneBook.get('image_url')
        pubDate = oneBook.get('publication_date')
        id = oneBook['id']
        publisher = oneBook['publishers'][0]['name']
        author = oneBook['authors'][0]['name']
        pubID = oneBook['publishers'][0]['id']
        authorID = oneBook['authors'][0]['id']
        
        newBook = Book(title = title, id = id, author = author, isbn = isbn, pubDate = pubDate, publisher = publisher, imageURL = imageURL, pubID=pubID,authorID=authorID )
        
        # After I create the book, I can then add it to my session. 
        db.session.add(newBook)
        # commit the session to my DB.
        db.session.commit()
        
def create_authors():
    author = load_json('author.json')

    for oneAuthor in author['authors']:
        name = oneAuthor['name']
        id = oneAuthor['id']
        yearOfBirth = oneAuthor.get('born')
        nationality = oneAuthor.get('nationality')
        almaMater = oneAuthor.get('alma_mater')
        education = oneAuthor.get('education')
        imageURL= oneAuthor.get('image_url')
        website = oneAuthor.get('wikipedia_url')
        
        newAuthor = Author(name = name, id = id,yearOfBirth=yearOfBirth, imageURL = imageURL, website = website, education= education, nationality=nationality, almaMater= almaMater)
        
        # After I create the book, I can then add it to my session. 
        db.session.add(newAuthor)
        # commit the session to my DB.
        db.session.commit()



def create_publishers():
    publisher = load_json('publishers.json')

    for onePublisher in publisher['publishers_data']:
        name = onePublisher['name']
        id = onePublisher['id']
        location = onePublisher.get('location')
        founding = onePublisher.get('founded')
        parentCompany = onePublisher.get('parent_company')
        website = onePublisher.get('website')
        imageURL= onePublisher.get('image_url')
        
        newPublisher = Publisher(name = name, id = id, imageURL = imageURL, website=website, location=location,founding=founding, parentCompany=parentCompany)
        
        # After I create the book, I can then add it to my session. 
        db.session.add(newPublisher)
        # commit the session to my DB.
        db.session.commit()

create_books()
create_publishers()
create_authors()
# end of create_db.py
