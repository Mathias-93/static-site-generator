import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_uneq(self):
        node = TextNode("Shouldn't be equal!", TextType.BOLD)
        node2 = TextNode("Definitely not!", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_different_text_type(self):
        node = TextNode("Heyoo", TextType.BOLD)
        node2 = TextNode("Heyoo", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_url(self):
        node = TextNode("Heyoo", TextType.BOLD, "www.hello.com")
        node2 = TextNode("Heyoo", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_url_again(self):
        node = TextNode("Heyoo", TextType.BOLD, "www.hello.com")
        node2 = TextNode("Heyoo", TextType.BOLD, "www.hello.com")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()