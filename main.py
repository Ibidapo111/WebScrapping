from modules.get_content import get_page_content
from modules.parse_html import parse_html
from modules.extract_links import extract_links
from modules.filter_links import filter_outbound_links
from modules.display_links import display_links

def scrape_outbound_links(reddit_url):
    """
    Scrape outbound links from a given Reddit URL (subreddit or post).
    """
    content = get_page_content(reddit_url)
    if content is None:
        return []

    soup = parse_html(content)
    links = extract_links(soup)
    outbound_links = filter_outbound_links(links)
    return outbound_links

if __name__ == "__main__":
    reddit_url = input("Enter the Reddit URL to scrape: ")
    outbound_links = scrape_outbound_links(reddit_url)
    display_links(outbound_links)
