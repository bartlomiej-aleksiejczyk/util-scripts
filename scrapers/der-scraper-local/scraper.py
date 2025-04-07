import os
import re
from urllib.parse import urlparse

import requests

from bs4 import BeautifulSoup



def fetch_and_parse(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the webpage: HTTP {response.status_code}")
        return

    netloc = urlparse(response.url).netloc

    soup = BeautifulSoup(response.text, "html.parser")

    title = (
        soup.find("meta", property="og:title")["content"]
        if soup.find("meta", property="og:title")
        else "No Title"
    )
    description = (
        soup.find("meta", property="og:description")["content"]
        if soup.find("meta", property="og:description")
        else "No Description"
    )
    extended_lead = (
        soup.find(attrs={"class": "extendedLeadCommentary"}).contents[0].text
        if soup.find(attrs={"class": "extendedLeadCommentary"})
        else "No Extended Lead"
    )

    def select_paragraphs(tag):
        return tag.has_attr("data-scroll") and "paragraph_" in tag["data-scroll"]

    paragraphs = soup.find_all(select_paragraphs)
    paragraphs_text = [paragraph.text for paragraph in paragraphs]

    return title, description, extended_lead, paragraphs_text, netloc


def write_to_markdown(filename, title, description, extended_lead, paragraphs):
    output_dir = "./download"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"# {title}\n\n")
        file.write(f"**Description-Lead:** {description}\n\n")
        file.write(f"**Extended Lead:** {extended_lead}\n\n")
        file.write("---\n\n")
        for paragraph in paragraphs:
            file.write(f"{paragraph}\n\n")


def to_filename_friendly(s, max_length=255):
    s = s.lower()
    s = re.sub(r"[\s\W-]+", "-", s)
    s = re.sub(r"-+", "-", s)
    s = s.strip("-")
    s = re.sub(r"^\d+", "", s)

    if len(s) > max_length:
        s = s[:max_length].rstrip("-_")

    return s


url = os.environ["URL"]

title, description, extended_lead, paragraphs, netloc = fetch_and_parse(url)

markdown_file = to_filename_friendly(f"{netloc}_{title}") + ".md"
write_to_markdown(markdown_file, title, description, extended_lead, paragraphs)
print(f"Data written to {markdown_file}")
