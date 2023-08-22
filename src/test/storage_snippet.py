
import unittest
from dataclasses import asdict
from ..code_snippet import CodeSnippet, NULL_CODE_SNIPPET
from ..snippet_storage import SnippetStorage


class TestSnippetStorage(unittest.TestCase):

    def setUp(self):
        self.storage = SnippetStorage({})

        self.snippet_1 = CodeSnippet(
            file_path='/path/to/file',
            file_name='file.py',
            code_snippet_type='function',
            code_snippet_identifier='my_function',
            code_snippet_implementation='def my_function(): pass'
        )

        self.snippet_2 = CodeSnippet(
            file_path='/path/to/other/file',
            file_name='other_file.py',
            code_snippet_type='class',
            code_snippet_identifier='MyClass',
            code_snippet_implementation='class MyClass: pass'
        )

    def test_singleton(self):
        storage2 = SnippetStorage({})
        self.assertEqual(id(self.storage), id(storage2), 'SnippetStorage should be a singleton')

    def test_add_code_snippet(self):
        self.assertTrue(self.storage.add_code_snippet(self.snippet_1), 'Should be able to add a new snippet')
        self.assertIn(hash(self.snippet_1), self.storage.storage, 'New snippet should be in the storage')

    def test_do_not_add_null_code_snippet(self):
        self.assertFalse(self.storage.add_code_snippet(NULL_CODE_SNIPPET), 'Should not be able to add a null snippet')

    def test_do_not_add_duplicate_code_snippet(self):
        self.storage.add_code_snippet(self.snippet_1)
        self.assertFalse(self.storage.add_code_snippet(self.snippet_1), 'Should not be able to add a duplicate snippet')

    def test_get_code_snippet(self):
        self.storage.add_code_snippet(self.snippet_1)
        retrieved_snippet = self.storage.get_code_snippet(self.snippet_1)
        self.assertEqual(asdict(self.snippet_1), asdict(retrieved_snippet), 'Retrieved snippet should match the original one')

    def test_update_existing_code_snippet(self):
        self.storage.add_code_snippet(self.snippet_1)
        updated_snippet = CodeSnippet(
            file_path=self.snippet_1.file_path,
            file_name=self.snippet_1.file_name,
            code_snippet_type=self.snippet_1.code_snippet_type,
            code_snippet_identifier=self.snippet_1.code_snippet_identifier,
            code_snippet_implementation='def my_function(): return 1'
        )
        self.assertTrue(self.storage.update_code_snippet(updated_snippet), 'Should be able to update an existing snippet')
        retrieved_snippet = self.storage.get_code_snippet(updated_snippet)
        self.assertEqual(asdict(updated_snippet), asdict(retrieved_snippet), 'Retrieved snippet should match the updated one')

    def test_do_not_update_non_existing_code_snippet(self):
        self.assertFalse(self.storage.update_code_snippet(self.snippet_2), 'Should not be able to update a non-existing snippet')

if __name__ == '__main__':
    unittest.main() 