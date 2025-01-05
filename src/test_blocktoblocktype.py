import unittest

from blocktoblocktype import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_header(self):
       test_header = ["#### test", "# test", "###### test"]
       for test in test_header:
           self.assertEqual(block_to_block_type(test), "heading")
    def test_not_header(self):
        test_notheader = ["####### test", "##test", "test ##"] 
        for test in test_notheader:
            self.assertNotEqual(block_to_block_type(test), "heading")
    def test_code(self):
        test_code = [codetest1, codetest2]
        for test in test_code:
            self.assertEqual(block_to_block_type(test), "code")
    def test_not_code(self):
        test_notcode = [codetest3, codetest4]
        for test in test_notcode:
            self.assertNotEqual(block_to_block_type(test), "code")
    def test_quoteblock(self):
        test_quoteblock = [quotetest1, quotetest2, quotetest3]
        for test in test_quoteblock:
            self.assertEqual(block_to_block_type(test), "quote")
    def test_not_quoteblock(self):
        self.assertNotEqual(block_to_block_type(quotetest4), "quote")
    def test_unordered_list(self):
        test_ul = [ultest1, ultest2]
        for test in test_ul:
            self.assertEqual(block_to_block_type(test), "unordered_list")
    def test_ordered_list(self):
        test_ol = [oltest1, oltest2]
        for test in test_ol:
            self.assertEqual(block_to_block_type(test), "ordered_list")
    def test_not_ordered_list(self):
        self.assertNotEqual(block_to_block_type(oltest3), "ordered_list")
        
        



codetest1 = "```this is code```"
codetest2 = """```
this
is
also
code
```"""
codetest3 = "```this is not code"
codetest4 = "``this is also not code```"
quotetest1 = "> this is a quoteblock"
quotetest2 = ">this is also a quoteblock"
quotetest3 = """>as
>is
>this"""
quotetest4 = """> but
this>
>isn't"""
ultest1 = """* I really
* hate writing
* in raw html"""
ultest2 = """* I really
- hate writing
- in raw html"""
oltest1 = """1. This is
2. an ordered
3. list"""
oltest2 = "1. This is an ordered list"
oltest3 = """1. this is not
3. an ordered list"""


if __name__ == "__main__":
    unittest.main()