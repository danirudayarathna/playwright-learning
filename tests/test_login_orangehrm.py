from playwright.sync_api import Page, expect

def test_exmaple(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("Username" )