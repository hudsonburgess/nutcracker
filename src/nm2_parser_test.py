import unittest
from nm2_parser import NM2Parser
import tempfile

class TestNM2Parser(unittest.TestCase):

    def test_init(self):
        test_file = tempfile.NamedTemporaryFile()
        parser = NM2Parser(test_file)
        self.assertEqual(parser.infile, test_file)

if __name__ == '__main__':
    unittest.main()