
### Reddit Outbound Link Scraper

This project is a modular Python-based web scraper designed to extract outbound links (links pointing to external websites) from a given Reddit URL, such as a subreddit or a specific post.

## Features

- **Modular Design**: Each functionality is encapsulated in its own module for better readability and reusability.
- **BeautifulSoup for HTML Parsing**: Efficiently parses the Reddit HTML content to extract links.
- **User-Friendly Output**: Filters and displays only outbound links.
- **Error Handling**: Gracefully handles network errors and invalid inputs.

## Project Structure

```
webscraping/
│
├── modules/
│   ├── __init__.py               # Makes the modules folder a package
│   ├── get_content.py            # Fetches the page content
│   ├── parse_html.py             # Parses HTML content using BeautifulSoup
│   ├── extract_links.py          # Extracts all links from the parsed HTML
│   ├── filter_links.py           # Filters and returns only outbound links
│   ├── is_outbound.py            # Checks if a link is outbound
│   └── display_links.py          # Displays the extracted links
│
└── main.py                       # Main script to orchestrate the scraping process
```

## Requirements

- Python 3.7 or higher
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ibidapo111/WebScrapping.git
   cd WebScrapping
   ```

2. **Install Dependencies**:
   Use `pip` to install the required libraries:
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

1. **Run the Script**:
   Execute the main script:
   ```bash
   python main.py
   ```

## Modules Overview

### `get_content.py`
Fetches the page content using an HTTP GET request.

### `parse_html.py`
Parses the HTML content and creates a BeautifulSoup object.

### `extract_links.py`
Extracts all anchor tags (`<a>`) with `href` attributes.

### `filter_links.py`
Filters the extracted links to include only outbound links (links not pointing to Reddit).

### `is_outbound.py`
Determines if a URL is an outbound link.

### `display_links.py`
Displays the list of outbound links in a readable format.



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.



---

Happy scraping!
```

