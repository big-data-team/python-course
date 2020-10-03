class InvertedIndex:
    def query(self, words: list) -> list:
        """Return the list of relevant documents for the given query"""
        pass

    def dump(self, filepath: str):
        pass

    @classmethod
    def load(cls, filepath: str):
        pass


def load_documents(filepath: str):
    pass


def build_inverted_index(documents):
    pass


def main():
    documents = load_documents("/path/to/dataset")
    inverted_index = build_inverted_index(documents)
    inverted_index.dump("/path/to/inverted.index")
    inverted_index = InvertedIndex.load("/path/to/inverted.index")
    document_ids = inverted_index.query(["two", "words"])


if __name__ == "__main__":
    main()

