import pytest
from playwright.sync_api import Page,expect

def test_css_selectors(page:Page):
    page.goto("https://www.saucedemo.com/")
    #find user name by ID
    username = page.locator("#user-name")
    expect(username).to_be_visible()

    #find password by Id
    password = page.locator("#password")
    expect(password).to_be_visible()

    #fine login button
    login = page.locator(".submit-button")
    expect(login).to_be_visible()

    username.fill("standard_user")
    password.fill("secret_sauce")
    login.click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")



