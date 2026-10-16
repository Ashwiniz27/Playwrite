import pytest
from playwright.sync_api import Page
def test(page: Page):
    #tagid
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input#small-searchterms").fill("Phones")
    page.wait_for_timeout(1000)

    #tagclass
    page.goto("https://www.youtube.com/")
    page.locator("input.ytSearchboxComponentInput").fill("cartoon")
    page.wait_for_timeout(1000)

    #tagattribute
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input[name=q]").fill("Dresses")
    page.wait_for_timeout(1000)
