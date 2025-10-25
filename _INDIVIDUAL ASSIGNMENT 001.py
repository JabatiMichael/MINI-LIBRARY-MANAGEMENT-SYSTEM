books = {
    "123456": {
        "title": "Python Basics",
        "author": "John Doe",
        "genre": "Non-Fiction",
        "total_copies": 5
    }
}
members = [
    {
        "member_id": "M001",
        "name": "Alice Smith",
        "email": "alice@example.com",
        "borrowed_books": ["123456"]
    }
]
GENRES = ("Fiction", "Non-Fiction", "Sci-Fi")
# CREATING: adding new book
def add_book(isbn, title, author, genre, total_copies):
    """Add a book to the catalog. Returns True if successful, False if ISBN exists or genre is invalid."""
    if isbn in books or genre not in GENRES:
        return False
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies
    }
    return True

def add_member(member_id, name, email):
    """Add a new member. Returns True if successful, False if member_id exists."""
    for member in members:
        if member["member_id"] == member_id:
            return False
    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    return True
# READING
def search_books(query, by="title"):
    """Search books by title or author. Returns list of matching books."""
    query = query.lower()
    results = []
    for book in books.values():
        if query in book[by].lower():
            results.append(book)
    return results
# UPDATING
def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    #Update book details. Returns True if successful.
    if isbn not in books:
        return False
    if genre and genre not in GENRES:
        return False
    if title:
        books[isbn]["title"] = title
    if author:
        books[isbn]["author"] = author
    if genre:
        books[isbn]["genre"] = genre
    if total_copies is not None:
        books[isbn]["total_copies"] = total_copies
    return True

def update_member(member_id, name=None, email=None):
    #Update member details. Returns True if successful.
    for member in members:
        if member["member_id"] == member_id:
            if name:
                member["name"] = name
            if email:
                member["email"] = email
            return True
    return False
# DELETING
def delete_book(isbn):
    #Delete a book if no copies are borrowed. Returns True if successful.
    if isbn not in books:
        return False
    for member in members:
        if isbn in member["borrowed_books"]:
            return False
    del books[isbn]
    return True
# DELETE FUNCTIONALITY

def delete_member(member_id):
    #Delete a member if they have no borrowed books. Returns True if successful.
    for member in members:
        if member["member_id"] == member_id and not member["borrowed_books"]:
            members.remove(member)
            return True
    return False
#  BORROW / RETURN
def borrow_book(isbn, member_id):
    #Borrow a book. Returns True if successful.
    if isbn not in books or books[isbn]["total_copies"] <= 0:
        return False
    for member in members:
        if member["member_id"] == member_id:
            if len(member["borrowed_books"]) >= 3:
                return False
            member["borrowed_books"].append(isbn)
            books[isbn]["total_copies"] -= 1
            return True
    return False

def return_book(isbn, member_id):
    # Return a book. Returns True if successful.
    for member in members:
        if member["member_id"] == member_id and isbn in member["borrowed_books"]:
            member["borrowed_books"].remove(isbn)
            books[isbn]["total_copies"] += 1
            return True
    return False
# UNIT TEST
assert add_book("000001", "Learn Python", "Jane Doe", "Non-Fiction", 3) == True
assert add_member("M002", "Bob", "bob@example.com") == True
assert borrow_book("000001", "M002") == True
assert borrow_book("000001", "M002") == True
assert borrow_book("000001", "M002") == True
assert borrow_book("000001", "M002") == False  # Exceeds limit
assert return_book("000001", "M002") == True
assert delete_member("M002") == False  # Still has borrowed books
# DEMO SCRIPT
def demo():
    print("Initializing Library System...")
    global GENRES
    GENRES = ("Fiction", "Non-Fiction", "Sci-Fi")

    add_book("111", "Book A", "Author A", "Fiction", 2)
    add_book("222", "Book B", "Author B", "Sci-Fi", 1)
    add_member("M001", "Alice", "alice@example.com")
    add_member("M002", "Bob", "bob@example.com")

    print("Books:", books)
    print("Members:", members)

    borrow_book("111", "M001")
    print("After borrowing Book A:", books, members)

    return_book("111", "M001")
    print("After returning Book A:", books, members)

if __name__ == "__main__":
    demo()
