def extract_links(soup):
    """
    Extract all anchor tags with href attributes from the BeautifulSoup object.
    """
    return soup.find_all('a', href=True)
