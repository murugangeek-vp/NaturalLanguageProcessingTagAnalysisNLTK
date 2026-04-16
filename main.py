import re
from html.parser import HTMLParser

import requests
import nltk
from nltk.corpus import stopwords
from nltk import FreqDist
import matplotlib.pyplot as plt
from nltk.text import Text


class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_parts = []

    def handle_data(self, data):
        self.text_parts.append(data)

    def get_text(self):
        return " ".join(self.text_parts)


def extract_text_from_html(html: str) -> str:
    parser = HTMLTextExtractor()
    parser.feed(html)
    return re.sub(r"\s+", " ", parser.get_text()).strip()


def fetch_and_clean_wiki_text(url: str) -> list[str]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    raw_html = response.text

    page_text = extract_text_from_html(raw_html)

    nltk.download("stopwords", quiet=True)

    tokens = re.findall(r"[A-Za-z]+", page_text)
    stop_words = set(stopwords.words("english"))

    words = [token.lower() for token in tokens]
    filtered_words = [word for word in words if word not in stop_words]

    return filtered_words


def main():
    wiki_url = "https://en.wikipedia.org/wiki/Tata_Group"
    filtered_tokens = fetch_and_clean_wiki_text(wiki_url)

    print(f"Fetched: {wiki_url}")
    print(f"Filtered token count: {len(filtered_tokens)}")
    print("Sample filtered tokens:", filtered_tokens[:50])


    clean_token=FreqDist(filtered_tokens)
    clean_token.plot(20, cumulative=False)
    plt.show()
    clean_token.tabulate(10)

    # 2. Convert to nltk.Text
    text = Text(clean_token)

    # 3. Plot specific words
    text.dispersion_plot(["tata", "parser", "india"])
    plt.show()


if __name__ == "__main__":
    main()
