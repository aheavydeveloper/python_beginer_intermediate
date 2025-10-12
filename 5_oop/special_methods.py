

class Book:
    def __init__(self, aauthor , title, pages=100):
        self.aauthor = aauthor
        self.title = title
        self.pages=pages

    def __str__(self):
        return f"{self.title} by {self.aauthor}"
    def __len__(self):
        return self.pages



hustel_hub = Book('janmejaya', "hustle hub")
print(hustel_hub)
print(len(hustel_hub))
