import time


def test_button(browser):

    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(2)
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), "Button exist"
