import unittest
from nm2_parser import NM2Parser

class TestNM2Parser(unittest.TestCase):

    def test_init(self):
        parser = NM2Parser('filename')
        self.assertEqual('filename', parser.infile_name)

if __name__ == '__main__':
    unittest.main()