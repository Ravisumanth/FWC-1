import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
url = "https://www.bt.com/"
driver.get(url)
time.sleep(3)
try:
    # Wait for the Cookie pop-up to appear (if it exists) and close it
    cookie_popup = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"Accept all cookies")))

    cookie_popup.click()
    mobile_menu = driver.find_element(By.LINK_TEXT, "<span class="">Mobile</span>")
    ActionChains(driver).move_to_element(mobile_menu).perform()

    mobile_phones = driver.find_element(By.LINK_TEXT,"https://www.bt.com/products/mobile/phones/")
    mobile_phones.click()
    banners = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH,'//*[@id="__next"]/div/div[4]/div')))
    assert len(banners) >= 3
    view_sim_only_deals = driver.find_element(By.LINK_TEXT, "View SIM only deals")
    driver.execute_script("arguments[0].scrollIntoView();", view_sim_only_deals)
    view_sim_only_deals.click()
    expected_title = "Enjoy 30% off and double data"
    WebDriverWait(driver, 10).until(
        EC.title_contains(expected_title))

    offer_details_element = driver.find_element(By.CLASS_NAME, "simo-card-ee_text_container__30ltg")

    offer_details_text = offer_details_element.text

    expected_text = "30% off and double data, was 125GB 250GB Essential plan, was £27 £18.90 per month"
    
    assert expected_text in offer_details_text, f"'{expected_text}' not found in offer details"


finally:
    driver.quit()
