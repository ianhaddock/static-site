# test_generate_html.py

import unittest
import os
import shutil

from generate_html import (
    extract_title
    )

test_directory  = 'unittest'

class TestGenerateHTMl(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        """ setup test files """
        os.mkdir(test_directory)

        with open(os.path.join(test_directory, 'test_title_success.md'), "w") as file:
            file.write(f'\n\n# H1 Title\n\nThis is para text\n\n')

        with open(os.path.join(test_directory, 'test_title_fail.md'), "w") as file:
            file.write(f'\n\n### H3 not H1 title\n\nThis is para text\n\n')

        with open(os.path.join(test_directory, 'test_title_buried.md'), "w") as file:
            file.write(f'para text in front of only header\n\n# H1 Title\n\nThis is more para text\n\n')


    @classmethod
    def tearDownClass(cls):
        """ remove test files """

        if os.path.isdir(test_directory):
            shutil.rmtree(test_directory)


    def test_extract_title_match(self):
        self.assertEqual(
            extract_title(f'\n\n# H1 Title\n\nThis is para text\n\n'),
            "H1 Title"
            )


    def test_extract_title_buried_match(self):
        self.assertEqual(
            extract_title(f'para text in front of only header\n\n# H1 Title\n\nThis is more para text\n\n'),
            "H1 Title"
            )


    def test_extract_title_fail(self):
        with self.assertRaises(Exception) as exception:
            extract_title(f'\n\n### H3 not H1 title\n\nThis is para text\n\n')

        #  self.assertEqual(exception.value, 'No H1 Header found')


if __name__ == "__main__":
    unittest.main()
