import os, time, csv
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


load_dotenv()
UserName = os.getenv('USERNAME')
PassWrd = os.getenv('PASSWORD')

def login(driver):
    loglink = "https://www.instagram.com/accounts/login/"
    username = UserName
    password = PassWrd

    driver.get(loglink)
    driver.implicitly_wait(3)

    usernameh = driver.find_element(By.NAME, 'username')
    usernameh.send_keys(username)

    passwordh = driver.find_element(By.NAME, 'password')
    passwordh.send_keys(password)

    driver.implicitly_wait(3)
    passwordh.send_keys(Keys.ENTER)
    time.sleep(5)

def get_post_links(driver, profile_url):
    driver.get(profile_url)
    time.sleep(5)

    # Scroll down to load all posts
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = bs(driver.page_source, 'html.parser')
    links = soup.find_all('a')
    post_links = [link['href'] for link in links if '/p/' in link['href']]
    return [post_link[3:-1] for post_link in post_links]

driver = webdriver.Chrome()
login(driver)

profile_url = 'https://www.instagram.com/d1anaa_t/'  # replace with the profile you want
post_links = get_post_links(driver, profile_url)
with open('post_links.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for link in post_links:
        writer.writerow([link])


def PostComments(driver, postlink):
    # Open the Instagram post
    post_url = f'https://www.instagram.com/p/{postlink}/'
    driver.get(post_url)
    time.sleep(5)
    # Parse the loaded page
    soup = bs(driver.page_source, 'html.parser')

    # Find all comments
    comments_span = soup.find_all('span', class_='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj')
    comments = [comment.text for comment in comments_span]

    return comments


def WriteComments(comment_list, output_filename):
    with open(output_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Comment'])

        for postlink, comments in comment_list:
            for comment in comments:
                writer.writerow([comment])

def FullComments(driver, filename):
    comment_list = []

    with open(filename, 'r') as f:
        post_links = [line.strip() for line in f]

    for postlink in post_links:
        comments = PostComments(driver, postlink)
        comment_list.append((postlink, comments))

    return comment_list

if __name__ == "__main__":
    driver = webdriver.Chrome()
    login(driver)

    profile_url = 'https://www.instagram.com/d1anaa_t/'
    post_links = get_post_links(driver, profile_url)
    with open('post_links.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for link in post_links:
            writer.writerow([link])

    comment_list = FullComments(driver, 'post_links.csv')
    WriteComments(comment_list, 'comments.csv')