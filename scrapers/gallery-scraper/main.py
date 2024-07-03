import os
import time
import requests
from bs4 import BeautifulSoup

# Constants
BASE_URL_PAGES = "https://www.base.url/with/page/"
BASE_URL_IMAGES = "https://www.base.url"
IMAGE_DIR = "folder_name"
START_PAGE = 1
END_PAGE = 146


# Functions
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def download_image(image_url, save_dir):
    response = requests.get(image_url)
    if response.status_code == 200:
        filename = os.path.join(save_dir, image_url.split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {image_url}")


def get_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        print(f"Failed to get soup for url: {url}")
        return None


def scrape_image_links(section_soup, current_base_url):
    image_links = []
    hyperlinks = section_soup.find_all('a')
    for link in hyperlinks:
        print(f"{current_base_url}{link['href']}")
        image_page_soup = get_soup(f"{current_base_url}{link['href']}")
        if image_page_soup:
            gallery_target = image_page_soup.find('div', class_='gallery')
            if gallery_target:
                images = gallery_target.find_all('a')
                for img in images:
                    if img and img.get('href'):
                        image_links.append(f"{BASE_URL_IMAGES}{img['href']}")
    return image_links


def scrape_gallery_page(page_number):
    url = f"{BASE_URL_PAGES}{page_number}"
    soup = get_soup(url)
    if soup:
        section_sorted = soup.find('div', class_='row')
        if section_sorted:
            image_links = scrape_image_links(section_sorted, BASE_URL_IMAGES)
            for image_url in image_links:
                download_image(image_url, IMAGE_DIR)
                time.sleep(1)


def scrape_range(start_page, end_page):
    for page in range(start_page, end_page + 1):
        scrape_gallery_page(page)
        print(f"Finished scraping page {page}")
        time.sleep(1)


def main():
    create_directory(IMAGE_DIR)

    scrape_range(START_PAGE, END_PAGE)


if __name__ == "__main__":
    main()
