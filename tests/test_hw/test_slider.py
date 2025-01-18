from pages.slider_page import SliderPage
from selenium.webdriver import Keys



def test_slider(browser):
    slider = SliderPage(browser)

    slider.visit()
    assert slider.slider.exist()
    assert slider.inp.exist()

    while not slider.inp.get_dom_attribute('value') == '50':
        slider.slider.send_keys(Keys.ARROW_RIGHT)