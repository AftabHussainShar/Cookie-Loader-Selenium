import pickle
from selenium import webdriver

def load_cookies_from_file(file_path):
    with open(file_path, 'rb') as f:
        cookies = pickle.load(f)
    return cookies

def init_driver():
    driver = webdriver.Chrome()
    return driver

def load_cookies(driver, cookies):
    driver.get('https://www.linkedin.com') 
    for cookie in cookies:
        driver.add_cookie(cookie)
        
def browse_with_cookies(cookie_file_path):
    driver = init_driver()
    cookies = load_cookies_from_file(cookie_file_path)
    load_cookies(driver, cookies)
    driver.get('https://www.linkedin.com/feed')  

    # driver.quit()

cookie_file_path = 'cookies.pkl'  
browse_with_cookies(cookie_file_path)