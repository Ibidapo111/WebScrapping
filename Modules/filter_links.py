from .is_outbound import is_outbound_link

def filter_outbound_links(links):
    """
    Filter and return only the outbound links from the list of all links.
    """
    outbound_links = [link['href'] for link in links if is_outbound_link(link['href'])]
    return outbound_links
