import requests

def main():
    url = "https://www.uccs.edu/"
    count = get_word_count_from_url(url)
    print(f"The page at {url} has roooughly {count} words")

# Gets word count from web page Using URL
def get_word_count_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # will raise an error if request failed
    text = response.text
    words = text.split()
    return len(words)


if __name__ == "__main__":
    main()