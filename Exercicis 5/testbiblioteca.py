import unittest
import biblioteca

class TestBiblioteca(unittest.TestCase):

    def setUp(self):
        # Limpia la biblioteca antes de cada test
        biblioteca.biblioteca.clear()

    def test_add_book(self):
        biblioteca.add_book("Title1", "Author1", "2001")
        self.assertEqual(len(biblioteca.biblioteca), 1)
        biblioteca.add_book("Title2", "Author2", "2002")
        self.assertEqual(len(biblioteca.biblioteca), 2)
        biblioteca.add_book("Title3", "Author3", "2003")
        self.assertEqual(len(biblioteca.biblioteca), 3)
        

    def test_search_book(self):
        biblioteca.add_book("Title1", "Author1", "2001")
        self.assertEqual(biblioteca.search_book("Title1"), "Title1 - Author1 - 2001")
        self.assertEqual(biblioteca.search_book("Title2"), "Book not found")

    def test_delete_book(self):
        biblioteca.add_book("Title1", "Author1", "2001")
        self.assertEqual(biblioteca.delete_book("Title1"), "Book deleted")
        

    def test_list_books(self):
        biblioteca.add_book("Title1", "Author1", "2001")
        biblioteca.add_book("Title2", "Author2", "2002")
        biblioteca.add_book("Title3", "Author3", "2003")
        self.assertEqual(biblioteca.list_books(), "Title1 - Author1 - 2001\nTitle2 - Author2 - 2002\nTitle3 - Author3 - 2003\n")

if __name__ == "__main__":
    unittest.main()
