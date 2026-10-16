import pytest
from playwright.sync_api import Page,expect
@pytest.fixture

def website(page:Page):
    page.goto("https://www.saucedemo.com/")
    return page

def test_website(website:Page):
    #check username feild
    expect(
        website.get_by_placeholder("Username")
    ).to_be_visible()
    website.wait_for_timeout(1000)
    #check password feild
    expect(
        website.get_by_placeholder("Password")
    ).to_be_visible()

