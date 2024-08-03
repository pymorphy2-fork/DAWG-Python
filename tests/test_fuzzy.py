import dawg_python

from .utils import data_path, words100k

words = words100k()
dawg = dawg_python.Dictionary.load(data_path("large", "int_dawg.dawg"))


class TestDictionary:
    def test_contains(self):
        for word in words:
            assert dawg.contains(word.encode("utf8"))

    def test_find(self):
        for word in words:
            assert dawg.find(word.encode("utf8")) == len(word)
