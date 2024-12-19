from urllib.parse import urlparse

def is_outbound_link(url):
    """
    Check if the link is an outbound link (i.e., not a Reddit link).
    """
    parsed_url = urlparse(url)
    return parsed_url.netloc not in ['www.reddit.com', 'old.reddit.com', 'reddit.com']
