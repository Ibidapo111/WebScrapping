def display_links(links):
    """
    Display the outbound links in a readable format.
    """
    if links:
        print("\nOutbound links found:")
        for link in links:
            print(link)
    else:
        print("\nNo outbound links found.")
