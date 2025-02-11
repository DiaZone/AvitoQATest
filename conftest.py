import pytest
from pages.start_page import StartPage


@pytest.fixture
def start_page(page):
    return StartPage(page)
