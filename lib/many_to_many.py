class Author:    
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        """The name attribute"""
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str:
            self._name = name

    def contracts(self):
        # print(self.name)
        # print([contract.author for contract in Contract.all])
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self ])

    def __repr__(self) -> str:
        return f"<Author {self.name}>"


class Book:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        """The title attribute"""
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str:
            self._title = title

    def contracts(self):
        # print(self.name)
        # print([contract.author for contract in Contract.all])
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]

    def __repr__(self) -> str:
        return f"<Book {self.title}>"


class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all.append(self)

    @property
    def author(self):
        """The author attribute"""
        return self._author
    
    @author.setter
    def author(self, author):
        if type(author) == Author:
            self._author = author
        else:
            raise Exception("Author must be an author")
    
    @property
    def book(self):
        """The book attribute"""
        return self._book
    
    @book.setter
    def book(self, book):
        if type(book) == Book:
            self._book = book
        else:
            raise Exception("Book must be a book")
        
    @property
    def date(self):
        """The date attribute"""
        return self._date
    
    @date.setter
    def date(self, date):
        if type(date) == str:
            self._date = date
        else:
            raise Exception("Date must be a string")
        
    @property
    def royalties(self):
        """The royalties attribute"""
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if type(royalties) == int:
            self._royalties = royalties
        else:
            raise Exception("Royalties must be an integer")
        
    def __repr__(self) -> str:
        return f"<Contract {self.author} - {self.book} - {self.date} - {self.royalties}"
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if date == contract.date]


if __name__ == "__main__":
    joe = Author("Joe")
    book = Book("Joe's Book")
    contract = Contract(joe, book, "1/12/2024", 1)

    mary = Author("Mary")
    book2 = Book("Frankenstein")
    contract = Contract(mary, book2, "1/12/2023", 2)
    
    joe.contracts()
    # print(contract.all)