import os
import sys
import unittest
#from models import db, Book
from create_db import db, Book, Author, Publisher

class DBTestCases(unittest.TestCase):
    def test_book_insert_1(self):
        s = Book(title = "How to wear a Top Hat", id = '2123424', author = 'Abraham Lincoln',isbn = '123445567889', pubDate = '10-10-1865', publisher = 'Sam Adams Inc.', imageURL = 'www.wewonthecivilwar.com')
        db.session.add(s)
        db.session.commit()


        r = db.session.query(Book).filter_by(id = '2123424').one()
        self.assertEqual(str(r.id), '2123424')
        self.assertEqual(str(r.author), 'Abraham Lincoln')
        self.assertEqual(str(r.isbn), '123445567889')
        self.assertEqual(str(r.pubDate), '10-10-1865')
        self.assertEqual(str(r.publisher), 'Sam Adams Inc.')
        self.assertEqual(str(r.imageURL), 'www.wewonthecivilwar.com')

        db.session.query(Book).filter_by(id = '2123424').delete()
        db.session.commit()

    def test_book_insert_2(self):
        s = Book(title = "Cizzle in the Hizzle", id = '452342', author = 'Snoop Dogg',isbn = '377377488', pubDate = '10-10-1995', publisher = 'Lion House', imageURL = 'www.dooggg.com')
        db.session.add(s)
        db.session.commit()


        r = db.session.query(Book).filter_by(id = '452342').one()
        self.assertEqual(str(r.id), '452342')
        self.assertEqual(str(r.author), 'Snoop Dogg')
        self.assertEqual(str(r.isbn), '377377488')
        self.assertEqual(str(r.pubDate), '10-10-1995')
        self.assertEqual(str(r.publisher), 'Lion House')
        self.assertEqual(str(r.imageURL), 'www.dooggg.com')

        db.session.query(Book).filter_by(id = '452342').delete()
        db.session.commit()    
    
    def test_book_insert_3(self):
        s = Book(title = "Amazon", id = '17724', author = 'Jeff Bezos',isbn = '45567889', pubDate = '10-10-2005', publisher = 'Amazon', imageURL = 'www.amazon.com')
        db.session.add(s)
        db.session.commit()


        r = db.session.query(Book).filter_by(id = '17724').one()
        self.assertEqual(str(r.id), '17724')
        self.assertEqual(str(r.author), 'Jeff Bezos')
        self.assertEqual(str(r.isbn), '45567889')
        self.assertEqual(str(r.pubDate), '10-10-2005')
        self.assertEqual(str(r.publisher), 'Amazon')
        self.assertEqual(str(r.imageURL), 'www.amazon.com')

        db.session.query(Book).filter_by(id = '17724').delete()
        db.session.commit()

    def test_author_insert_1(self):
        s = Author(name = 'R.Kelly', id = '2224442', imageURL = 'www.golden.com', website = 'www.golden.com', education= 'I believe I can fly', nationality='USA', almaMater= '')
        db.session.add(s)
        db.session.commit()


        r = db.session.query(Author).filter_by(id = '2224442').one()
        self.assertEqual(str(r.id), '2224442')
        self.assertEqual(str(r.imageURL), 'www.golden.com')
        self.assertEqual(str(r.website), 'www.golden.com')
        self.assertEqual(str(r.education), 'I believe I can fly')
        self.assertEqual(str(r.nationality), 'USA')
        self.assertEqual(str(r.almaMater), '')

        db.session.query(Author).filter_by(id = '2224442').delete()
        db.session.commit()

    def test_author_insert_2(self):
        s = Author(name = 'Snoop Dogg', id = '420420', imageURL = 'www.doge.com', website = 'www.doge.com', education= 'The streets', nationality='USA', almaMater= 'UT Austin')
        db.session.add(s)
        db.session.commit()


        r = db.session.query(Author).filter_by(id = '420420').one()
        self.assertEqual(str(r.id), '420420')
        self.assertEqual(str(r.imageURL), 'www.doge.com')
        self.assertEqual(str(r.website), 'www.doge.com')
        self.assertEqual(str(r.education), 'The streets')
        self.assertEqual(str(r.nationality), 'USA')
        self.assertEqual(str(r.almaMater), 'UT Austin')

        db.session.query(Author).filter_by(id = '420420').delete()
        db.session.commit()

    def test_author_insert_3(self):
        s = Author(name = 'Trevor Noah', id = '19872', imageURL = 'www.dailyshow.com', website = '', education= 'Talking', nationality='South African', almaMater= 'Princeton')
        db.session.add(s)
        db.session.commit()


        r = db.session.query(Author).filter_by(id = '19872').one()
        self.assertEqual(str(r.id), '19872')
        self.assertEqual(str(r.imageURL), 'www.dailyshow.com')
        self.assertEqual(str(r.website), '')
        self.assertEqual(str(r.education), 'Talking')
        self.assertEqual(str(r.nationality), 'South African')
        self.assertEqual(str(r.almaMater), 'Princeton')

        db.session.query(Author).filter_by(id = '19872').delete()
        db.session.commit()

    def test_publisher_insert_1(self):
        s = Publisher(name = 'AppleJacks', id = '99989', imageURL = 'www.cereals.com',website= 'www.cereals.com', location= 'Manhattan', founding='USA', parentCompany='Kellogs')
        db.session.add(s)
        db.session.commit()


        r = db.session.query(Publisher).filter_by(id = '99989').one()
        self.assertEqual(str(r.id), '99989')
        self.assertEqual(str(r.imageURL), 'www.cereals.com')
        self.assertEqual(str(r.website), 'www.cereals.com')
        self.assertEqual(str(r.location), 'Manhattan')
        self.assertEqual(str(r.founding), 'USA')
        self.assertEqual(str(r.parentCompany), 'Kellogs')
    
    def test_publisher_insert_2(self):
        s = Publisher(name = 'Test2', id = '1200009', imageURL = '',website= 'www.test.com', location= 'Antartica', founding='USA', parentCompany='Amazon')
        db.session.add(s)
        db.session.commit()


        r = db.session.query(Publisher).filter_by(id = '1200009').one()
        self.assertEqual(str(r.id), '1200009')
        self.assertEqual(str(r.imageURL), '')
        self.assertEqual(str(r.website), 'www.test.com')
        self.assertEqual(str(r.location), 'Antartica')
        self.assertEqual(str(r.founding), 'USA')
        self.assertEqual(str(r.parentCompany), 'Amazon')

    def test_publisher_insert_3(self):
        s = Publisher(name = 'Leprechauns Inc', id = '44444444', imageURL = 'www.lucky.com',website= 'www.fourleaf.com', location= 'End of the rainbow', founding='Ireland', parentCompany='Gold')
        db.session.add(s)
        db.session.commit()


        r = db.session.query(Publisher).filter_by(id = '44444444').one()
        self.assertEqual(str(r.id), '44444444')
        self.assertEqual(str(r.imageURL), 'www.lucky.com')
        self.assertEqual(str(r.website), 'www.fourleaf.com')
        self.assertEqual(str(r.location), 'End of the rainbow')
        self.assertEqual(str(r.founding), 'Ireland')
        self.assertEqual(str(r.parentCompany), 'Gold')
db.session.query(Publisher).filter_by(id = '44444444').delete()
db.session.commit()


if __name__ == '__main__':
    unittest.main()
