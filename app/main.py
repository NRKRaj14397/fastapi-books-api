from fastapi import Body,FastAPI

app = FastAPI() #app initialization

BOOKS = [
     {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "category": "Programming"},
     {"title": "Clean Code", "author": "Robert C. Martin", "category": "Programming"},
     {"title": "Atomic Habits", "author": "James Clear", "category": "Self-Help"},
     {"title": "Deep Work", "author": "Cal Newport", "category": "Productivity"},
     {"title": "The Lean Startup", "author": "Eric Ries", "category": "Business"},
     {"title": "The Lean Company", "author": "Eric Ries", "category": "Productivity"}
]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get('/books/{book_title}')
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        
    return {"message":"Book not found!"}

@app.get("/books/")
async def read_book_by_category(category: str):
    filtered_books = []

    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            filtered_books.append(book)
    
    if len(filtered_books):
        return filtered_books
    else:
        return {'message':f'No book found in {category} category'}
    
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author:str, category:str):
    book_returns = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            book_returns.append(book)

    if len(book_returns):
        return book_returns
    else:
        return {'message':'No matching book found!'}

@app.get("/books/author/{author_name}")
async def get_books_by_author_name(author_name:str):
    returned_book = []
    for book in BOOKS:
        if book.get('author').casefold() == author_name.casefold():
            returned_book.append(book)
    
    if len(returned_book):
        return returned_book
    else:
        return {'message':f'No book found for author:{author_name}'}


@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_bbok(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book_by_title(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break