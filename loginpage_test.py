from playwright.sync_api import Page,expect

def test_login(page:Page):
    page.goto("https://www.saucedemo.com/")
    username = page.locator("#user-name")
    password = page.locator("#password")
    username.fill("standard_user")
    password.fill("secret_sauce")
    login = page.locator("#login-button")
    login.click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")