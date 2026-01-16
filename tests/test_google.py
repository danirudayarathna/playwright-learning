import re
# "re" is stand for regex (used in title check when testing)

from playwright.sync_api import expect
# "expect" gives smart test assertions like "page should have this title"

def test_google_search(page):
    # page.wait_for_timeout(3000)
    page.goto("https://www.google.com/ncr")

# If google shows cookies popup. this command will automatically push accept all button and if the message is not found it will skip with a message
    try:
        page.get_by_role("button", name="Accept all").click(timeout=5000)
    except:
        print("No Popup to accept")

# Type something on a search bar

    page.get_by_role("combobox", name="Search").fill("Playwright Python")
    page.keyboard.press("Enter")

    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))
