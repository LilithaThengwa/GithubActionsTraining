import sys
import os

# To resolve module not found error. sys.path is a list that containes directories where the interpreter looks for modules to import.
# Because 'app' is located in src, python needs to know where to find 'app'. But since 'app' isn't in the current directory, can't be found unless the path is included.
# Must be above imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app.service.book_service import BookService
from app.repository.book_repository import BookRepository

# fixtures are a way to define reusable components or dependencies that can be injected into test functions.
@pytest.fixture
def mock_repo(mocker):
    return mocker.Mock(spec=BookRepository)

@pytest.fixture
def book_service(mock_repo):
    # Initialise book_service indtace and inject the mock repository into the service
    service = BookService()
    service.repository = mock_repo
    return service

def test_create_book(book_service, mock_repo):
    book = {"id": 1, "title": "Test Book", "author": "Test Author"}
    existing_books = [{"id": 1, "title": "Existing Book", "author": "Author A"}]

    mock_repo.get_all.return_value = existing_books
    mock_repo.create.return_value = book  # Arrange

    result = book_service.create_book(book)  # Act

    mock_repo.create.assert_called_once_with(book)  # Assert (interaction)
    assert result == book  # Assert (correct return value)

def test_get_book(book_service, mock_repo):
    book = {"id": 1, "title": "Test Book", "author": "Test Author"}
    mock_repo.get.return_value = book 

    result = book_service.get_book(1)  

    mock_repo.get.assert_called_once_with(1) 
    assert result == book 

def test_update_book(book_service, mock_repo):
    updated_book = {"id": 1, "title": "Updated Book", "author": "Updated Author"}
    mock_repo.update.return_value = updated_book  

    result = book_service.update_book(1, updated_book)  

    mock_repo.update.assert_called_once_with(1, updated_book)
    assert result == updated_book 

def test_delete_book(book_service, mock_repo):
    mock_repo.delete.return_value = True  

    result = book_service.delete_book(1)

    mock_repo.delete.assert_called_once_with(1)
    assert result is True 

def test_get_all_books(book_service, mock_repo):
    books = [
        {"id": 1, "title": "Test Book", "author": "Test Author"},
        {"id": 2, "title": "Another Book", "author": "Another Author"}
    ]
    mock_repo.get_all.return_value = books 

    result = book_service.get_all_books() 

    mock_repo.get_all.assert_called_once() 
    assert result == books 

# Arrange, Act, and Assert:

# Arrange: Set up the conditions for the test, including any necessary mock return values.
# Act: Call the method being tested.
# Assert: Verify that the expected outcomes occur, including checking interactions with the mocked repository.