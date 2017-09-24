import unittest
from nm2_parser import NM2Parser
import tempfile

class TestNM2Parser(unittest.TestCase):

    def setUp(self):
        self.testfile = tempfile.TemporaryFile()
        self.parser = NM2Parser(self.testfile)

    def test_init(self):
        self.assertEqual(self.parser.infile, self.testfile)

    def test_is_header_label(self):
        self.assertTrue(self.parser.is_header_label('# hello'))
        self.assertFalse(self.parser.is_header_label('###'))
        self.assertFalse(self.parser.is_header_label('hello'))

    def test_is_delimiter(self):
        self.assertTrue(self.parser.is_delimiter('###'))
        self.assertFalse(self.parser.is_delimiter('# hello'))
        self.assertFalse(self.parser.is_delimiter('hello'))

    def test_is_data(self):
        self.assertTrue(self.parser.is_data('key : value'))
        self.assertFalse(self.parser.is_data('hello'))
        self.assertFalse(self.parser.is_data('###'))
        self.assertFalse(self.parser.is_data('# key : value'))

    def test_add_key(self):
        test_dict = {}
        line = 'key : value'
        self.parser.add_key(test_dict, line)
        self.assertEqual(test_dict, { 'key': 'value' })

if __name__ == '__main__':
    unittest.main()