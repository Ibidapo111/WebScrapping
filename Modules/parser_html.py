from bs4 import BeautifulSoup

def parse_html(content):
    """
    Parse the HTML content and return a BeautifulSoup object.
    """
    return BeautifulSoup(content, 'html.parser')
