from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


'''Doesn't work'''
def like_all_posts(browser, profile_url):
    browser.get(profile_url)
    print('Arrived on https://www.instagram.com/maxdnv/')
    sleep(5)

    # Scroll down to load more posts (you may need to adjust the number of scrolls based on the account)
    scrolls = 3
    for _ in range(scrolls):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(0.1)
    sleep(1)

    # Find all the post links
    post_links = browser.find_elements(By.XPATH, '//a[contains(@href, "/p/")]')

    # Extract the URLs from the post links
    post_urls = [link.get_attribute('href') for link in post_links]

    for url in post_urls:
        print("Going on this url : " + url)
        browser.get(url)
        sleep(5)

        print('Clicking on the like button')
        like_button = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[3]/div[1]/div[1]/span[1]/div')
        like_button.click()
        print('Like button clicked')
        sleep(1)


def login(browser, username, password):
    print('Going to instagram')
    browser.get('https://www.instagram.com/')
    print('Arrived on instagram')
    sleep(3)

    print('Clicking on the cookie button')
    cookie_button = browser.find_element(By.CLASS_NAME, '_a9--')
    cookie_button.click()
    print('Cookie button clicked')
    sleep(3)

    print('Filling the username field')
    username_field = browser.find_element(By.NAME, 'username')
    username_field.send_keys(username)
    print('Username field filled')
    sleep(2)

    print('Filling the password field')
    password_field = browser.find_element(By.NAME, 'password')
    password_field.send_keys(password)
    print('Password field filled')
    sleep(2)

    print('Clicking on the login button')
    login_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()
    print('Login button clicked')
    sleep(10)


def deconnection(browser):
    print('Clicking on the profile button')
    profile_button = browser.find_element(By.XPATH, "//span[text()='Profil']")
    profile_button.click()
    print('Profile button clicked')
    sleep(2)

    print('Clicking on the settings button')
    # settings_button = browser.find_element(By.XPATH, '//svg[@aria-label="Options"]')
    settings_button = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]')
    settings_button.click()
    print('Settings button clicked')
    sleep(2)

    print('Clicking on the deconnection button')
    deconnection_button = browser.find_element(By.XPATH, '//button[text()="Déconnexion"]')
    deconnection_button.click()
    print('Deconnection button clicked')
    sleep(2)

    print('Refreshing the page')
    browser.refresh()
    print('Page refreshed')
    sleep(5)

    print('Clicking on the Instagram button')
    instagram_button = browser.find_element(By.XPATH, '//svg[@aria-label="Instagram"]')
    instagram_button.click()
    print('Instagram button clicked')
    sleep(5)


def main():
    username = 'USERNAME'
    password = 'PASSWORD'
    profil_url = 'PROFIL_URL'

    # Open the browser in private mode
    options = Options()
    options.add_argument("--private-window")  # Add the argument to open in private mode
    print('Opening browser')
    browser = webdriver.Firefox(options=options)
    print('Browser opened')

    login(browser, username, password)

    like_all_posts(browser, profil_url)

    # deconnection(browser)

if __name__ == '__main__':
    main()
