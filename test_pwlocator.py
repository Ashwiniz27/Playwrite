import time
import re
from playwright.sync_api import Page,expect

#getByAltText
def test(page:Page):
    page.goto("https://wizklub.com/")
    logo = page.get_by_alt_text("IBR launching 13 August at 12 noon")
    expect(logo).to_be_visible()

#getbytext
def test_text(page:Page):
    page.goto("https://wizklub.com/")
    expect(page.get_by_text("Voices That Matter")).to_be_visible()  #full text
    expect(page.get_by_text("Voices")).to_be_visible()   #partial text
    expect(page.get_by_text(re.compile(".*Voices That Matter.*"))).to_be_visible() #regular expression

    #getbyrole
    page.goto("https://forms.cloud.microsoft/pages/responsepage.aspx?id=WzxqFR7ZHkylGRFVvC_2db3q3U8YNhxDnnmpSZW5mddUQlFKRkM3Qk0zTEtZUjBURzhPS1pOTDc5VS4u&route=shorturl")
    page.get_by_label("Email ID").fill("asha@gmail.com")

    #maultiple atribute which have same place holder
    page.get_by_placeholder("Enter your answer").nth(1).fill("ashwini")
    page.wait_for_timeout(5000)