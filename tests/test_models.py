"""
    Test Models
"""
from tests.base  import BaseTestCase

from app import db

from app.models import *

class TestUserModel(BaseTestCase):
    """ test user model """
    def test_create(self):
        """ test adding user to database """
        user = User(username="jennie",
                    identity_id="123456",
                    name="Kim Jennie",
                    msisdn="081212341234",
                    email="jennie@bp.com",
                   )
        user.set_password("password")

        db.session.add(user)
        db.session.commit()

        # make sure the record is added
        self.assertTrue(user.id)

class TestCategoryModel(BaseTestCase):
    """ test category model """
    def test_create(self):
        """ test adding user to database """
        category = Category(name="some categoryh")

        db.session.add(category)
        db.session.commit()

        # make sure the record is added
        self.assertTrue(category.id)

class TestBookModel(BaseTestCase):
    """ test book model """
    def test_create(self):
        """ test adding book to database """
        book = Book(
            isbn="12316546465464644",
            title="some awesome book title",
            year=1998,
            price=50000,
        )

        db.session.add(book)
        db.session.commit()

        # make sure the record is added
        self.assertTrue(book.id)

    def test_book_categories(self):
        """ test joined relationship between book and category"""

        # add category
        horror = Category(name="horror")
        db.session.add(horror)

        thriller = Category(name="thriller")
        db.session.add(thriller)
        db.session.commit()

        # add publisher
        publisher = Publisher(name="some publisher")
        db.session.add(publisher)
        db.session.commit()

        # add author
        author = Author(first_name="Kelvin", last_name="Desman")
        author2 = Author(first_name="Jessica", last_name="Jung")
        db.session.add(author)
        db.session.add(author2)
        db.session.commit()

        # add book
        book = Book(
            isbn="12316546465464644",
            title="some awesome book title",
            year=1998,
            price=50000,
            publisher_id=publisher.id
        )

        db.session.add(book)

        # add book
        book2 = Book(
            isbn="12312312313213213131131312313",
            title="more awesome book title",
            year=2000,
            price=51000,
            publisher_id=publisher.id
        )

        db.session.add(book2)

        # add author here
        book.authors.append(author)
        book.authors.append(author2)
        book2.authors.append(author2)

        # add book categories here
        book.categories.append(horror)
        book.categories.append(thriller)
        book2.categories.append(horror)
        db.session.commit()

        # try look up by authors
        result = Book.query.filter(Book.authors.any(first_name="some author")).all()
        self.assertEqual(len(result), 0)

        result = Book.query.filter(Book.authors.any(first_name="Kelvin")).all()
        self.assertEqual(len(result), 1)

        result = Book.query.filter(Book.authors.any(last_name="Jung")).all()
        self.assertEqual(len(result), 2)

        # try look up by categories
        result = Book.query.filter(Book.categories.any(name="horror")).all()
        self.assertEqual(len(result), 2)

        result = Book.query.filter(Book.categories.any(name="thriller")).all()
        self.assertEqual(len(result), 1)

        # try look up by publisher
        result = Publisher.query.filter_by(name="some publisher").first()
        self.assertEqual(len(result.books), 2)

class TestIssuedLicense(BaseTestCase):
    """ test issued license model """
    def test_issue_licnese(self):
        """ test issue a license to a system """
        # dummy user
        user = User(username="jennie",
                    identity_id="123456",
                    name="Kim Jennie",
                    msisdn="081212341234",
                    email="jennie@bp.com",
                   )
        user.set_password("password")

        db.session.add(user)
        db.session.commit()

        # make sure the record is added
        self.assertTrue(user.id)

        # dummy license
        prci_license = License(
            name="Transactional License",
            description="some trnasactional description",
        )
        db.session.add(prci_license)
        db.session.commit()

        # dummy license
        blank_license = License(
            name="Blank License",
            description="some blank description",
        )
        db.session.add(blank_license)
        db.session.commit()

        # issue license here
        issue_license = IssuedLicense(
            user_id=user.id,
            license_id=prci_license.id
        )
        db.session.add(issue_license)
        db.session.commit()

        issue_license2 = IssuedLicense(
            user_id=user.id,
            license_id=blank_license.id
        )
        db.session.add(issue_license2)
        db.session.commit()

class TestCopyrightCase(BaseTestCase):
    """ test issued license model """
    def test_add_copyright(self):
        """ test issue a license to a system """
        # dummy user
        user = User(username="jennie",
                    identity_id="123456",
                    name="Kim Jennie",
                    msisdn="081212341234",
                    email="jennie@bp.com",
                   )
        user.set_password("password")

        db.session.add(user)
        db.session.commit()

        # make sure the record is added
        self.assertTrue(user.id)

        # dummy license
        blank_license = License(
            name="Blank License",
            description="some blank description",
        )
        db.session.add(blank_license)
        db.session.commit()

        issue_license2 = IssuedLicense(
            user_id=user.id,
            license_id=blank_license.id
        )
        db.session.add(issue_license2)
        db.session.commit()

        # add book
        book = Book(
            isbn="12316546465464644",
            title="some awesome book title",
            year=1998,
            price=50000,
        )

        db.session.add(book)
        db.session.commit()

        # make sure the record is added
        self.assertTrue(book.id)

        # add copyright
        copyright = Copyright(
            quantity=1,
            price=10000,
            book_id=book.id,
            issued_license_id=issue_license2.id
        )
        db.session.add(copyright)
        db.session.commit()

        invoice = Invoice(
            percentage=0.1,
            total_amount=1000,
            copyright_id=copyright.id
        )
        db.session.add(invoice)
        db.session.commit()

        #print(copyright.issued_license)
        print(invoice.copyright)
