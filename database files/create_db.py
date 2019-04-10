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

    for oneBook in book['Books']:
        title = oneBook['title']
        id = oneBook['id']
        isbn = oneBook['isbn']
        imageURL = oneBook['image_url']
        pubDate = oneBook['publication_date']
        author = oneBook['authors']['name']
		
        newBook = Book(title = title, id = id)
        
        # After I create the book, I can then add it to my session. 
        db.session.add(newBook)
        # commit the session to my DB.
        db.session.commit()
		
def create_authors():
    author = load_json('author.json')

    for oneAuthor in author['Authors']:
        name = oneAuthor['name']
        id = oneAuthor['id']
        education = oneAuthor['education']
        nationality = oneAuthor['nationality']
        almaMater = oneAuthor['alma_mater']
        education = oneAuthor['education']
        imageURL= oneAuthor['image_url']
        
        newAuthor = Author(name = name, id = id, imageURL = imageURL, website=website, education= education, nationality=nationality, almaMater= almaMater)
        
        # After I create the book, I can then add it to my session. 
        db.session.add(newBook)
        # commit the session to my DB.
        db.session.commit()



def create_publishers():
    publisher = load_json('publishers.json')

    for onePublisher in publisher['publishers_data']:
        name = onePublisher['name']
        id = onePublisher['id']
        location = onePublisher['location']
        founding = onePublisher['founded']
        parentCompany = onePublisher['parent_company']
        website = onePublisher['website']
        imageURL= onePublisher['image_url']
        
        newPublisher = Publisher(name = name, id = id, imageURL = imageURL, website=website, location=location,founding=founding, parentCompany=parentCompany)
        
        # After I create the book, I can then add it to my session. 
        db.session.add(newBook)
        # commit the session to my DB.
        db.session.commit()


create_books()
create_publishers()
create_authors()
# end of create_db.py
