# Web Crawler

This project is a simple web crawler that extracts URLs from a given website's sitemap and can be customized to download specific types of files, such as PDFs.

## Project Overview

The web crawler performs the following tasks:
- Downloads a sitemap from a specified URL.
- Parses the sitemap to extract links.
- Checks if the links are valid.
- Downloads PDF files found in the links.
- Recursively crawls the webpages linked from the sitemap.

## Installation

To set up this project, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. **Install the required Python packages**:

   Ensure you have Python 3 installed. You can then install the required packages using pip:

   ```bash
   pip install requests beautifulsoup4
   ```

3. **Set up the project**:

   Make sure the following Python files are in the project directory:
   - `downloading_web_page.py` – Contains the `Download` class used for downloading web pages.
   - `global_var.py` – Contains global variables such as `SITEMAP` and `BASE_URL`.
   - `store_to_pdf.py` – Contains the `Store_pdfs` function used for saving PDFs.

## Configuration

Before running the crawler, configure the following in `global_var.py`:

- `SITEMAP`: URL of the sitemap to start crawling.
- `BASE_URL`: Base URL of the website being crawled.

Example `global_var.py`:

```python
SITEMAP = "https://example.com/sitemap.xml"
BASE_URL = "https://example.com/"
```

## Usage

To start the web crawler, run the `crawl_sitemap` function with the sitemap URL:

```python
from global_var import SITEMAP
from your_crawler_script import crawl_sitemap

crawl_sitemap(SITEMAP)
```

Make sure to replace `your_crawler_script` with the name of the Python file where your `crawl_sitemap` function is defined.

## Notes

- The crawler avoids infinite loops by keeping track of visited links in the `VISITED_LINKS` list.
- It skips links that contain "javascript" or "#".
- The crawler can be modified to download other types of files by adjusting the file type checks in the `crawl_sitemap` function.

## Contributing

Feel free to submit issues or pull requests to improve the functionality of the web crawler. Contributions are welcome!

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
