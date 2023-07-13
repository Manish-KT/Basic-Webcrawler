from downloading_web_page import Download
from global_var import SITEMAP, BASE_URL
from bs4 import BeautifulSoup
from store_to_pdf import Store_pdfs

# to manage the visited links, and avoid the infinite loop
VISITED_LINKS = []


def crawl_sitemap(url):
    # Download the sitemap file
    sitemap = Download(url).text
    soup = BeautifulSoup(sitemap, "html.parser")

    """check if the webpage if valid or not"""
    if soup.find("img", {"src": "Images/404.gif"}):
        print("404 error on link: ", url)
        return 0

    # Extract the sitemap links
    links = soup.find_all("a")

    # Download each link
    for link in links:
        try:
            if link["href"].startswith(BASE_URL):
                link_to_webpage = link["href"]
            else:
                link_to_webpage = BASE_URL + link["href"]

            # print(link_to_webpage)

            # avoid downloading the void pages
            if "javascript" not in link_to_webpage or "#" not in link_to_webpage:
                # taking the pages with pdf and storing them, as their link
                if link_to_webpage.split(".")[-1] == "pdf":
                    Store_pdfs(link_to_webpage)
                    continue
                else:
                    # crawling the webpages of links
                    if link_to_webpage not in VISITED_LINKS:
                        VISITED_LINKS.append(link_to_webpage)
                        crawl_sitemap(link_to_webpage)
                    else:
                        continue
            else:
                return 0

        except Exception as e:
            print("error: ", e, " with the link: ", link)

        # print(VISITED_LINKS)


# print(crawl_sitemap(URL))
crawl_sitemap(SITEMAP)
