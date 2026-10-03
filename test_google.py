from playwright.sync_api import Page, expect

def test_verifyPageUrl(page:Page):
    page.goto("https://www.google.com")

    myurl = page.url
    print("URL of the application:", myurl)

    expect(page).to_have_url("https://www.google.com/")

def test_verifyTitle(page:Page):
    page.goto("https://www.google.com")
    mytitle = page.title()
    print("Title of the application:", mytitle)
    expect(page).to_have_title("Google")