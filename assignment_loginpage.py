from playwright.sync_api import Page,expect
def test_loginpage(page:Page):
    page.goto("https://wizklub.com/cognito/login/?redirect_url=/dashboard/home/")
    page.get_by_label("Phone Number / Email / Username").fill("ashwini")
    page.get_by_placeholder("Enter your password").fill("Ash@2727")
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="VERIFY AND PROCEED").click(force=True)
    expect(page).to_have_url("https://wizklub.com/dashboard/home/")


