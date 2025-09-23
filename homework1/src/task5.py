# List of favorite books which i definitely have read all of
books = [
    ("1984", "George Orwell"),
    ("To Kill a Mockingbird", "Harper Lee"),
    ("The Hobbit", "J.R.R. Tolkien"),
    ("Pride and Prejudice", "Jane Austen"),
    ("The Catcher in the Rye", "J.D. Salinger"),
]

# Slice to get the first three books
first_three_books = books[:3]

# dictionary to represent definitely real student "database"
students = {
    "Jake": "S001",
    "Josh": "S002",
    "Tanner": "S003",
    "Bob": "S004",
}

def main():
    print("First three books: ", first_three_books)
    print("Student database: ", students)

if __name__ == "__main__":
    main()
