def Store_pdfs(url):
    with open("website_pdfs_link.txt", "r+") as f:
        all_links = f.readlines()
        if url not in all_links:
            f.write(url + "\n")
            print("link added to file: ", url)

        # after writing all links to the file, we need to remove duplicate links
        all_links = set(f.readlines())
        f.seek(0)
        f.truncate(0)
        f.writelines(list(all_links))

