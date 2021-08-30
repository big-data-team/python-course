from __future__ import annotations

from typing import Dict, List


class InvertedIndex:
    def query(self, words: List[str]) -> List[int]:
        """Return the list of relevant documents for the given query"""
        pass

    def dump(self, filepath: str) -> None:
        pass

    @classmethod
    def load(cls, filepath: str) -> InvertedIndex:
        pass


def load_documents(filepath: str) -> Dict[int, str]:
    pass


def build_inverted_index(documents: Dict[int, str]) -> InvertedIndex:
    pass


def main():
    documents = load_documents("/path/to/dataset")
    inverted_index = build_inverted_index(documents)
    inverted_index.dump("/path/to/inverted.index")
    inverted_index = InvertedIndex.load("/path/to/inverted.index")
    document_ids = inverted_index.query(["two", "words"])


if __name__ == "__main__":
    main()
