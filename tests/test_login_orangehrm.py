from playwright.sync_api import Page, expect

def test_exmaple(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    page.locator("xpath=//aside[@class='oxd-sidepanel']//li[1]").click()
    assert page.title() == "OrangeHRM"

