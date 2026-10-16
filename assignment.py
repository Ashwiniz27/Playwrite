import pytest
from playwright.sync_api import Page,expect

def test_password(page:Page):
    page.goto("https://www.saucedemo.com/")
    password = page.locator("#password")
    password.fill("secret_sauce")
    expect(password).to_have_value("secret_sauce")

def test_login(page:Page):
    page.goto("https://www.saucedemo.com/")
    login = page.locator(".submit-button")
    expect(login).to_be_enabled()

def test_title(page:Page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")

def test_url(page:Page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_url("https://www.saucedemo.com/")