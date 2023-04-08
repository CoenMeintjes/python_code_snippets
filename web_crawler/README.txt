README for web crawler code

This Python code is a basic web crawler which extracts links from HTML pages and follows them recursively. The program uses the BeautifulSoup library to parse the HTML and retrieve all the anchor tags, and the SQLite database to store the URLs, HTML content, and links between pages.

The program starts by creating the 'Pages', 'Links', and 'Webs' tables in the SQLite database, if they don't already exist. It then prompts the user to enter a starting URL or uses a default URL ('https://python-data.dr-chuck.net/') if no URL is entered. It inserts the starting URL into the 'Pages' table and commits the change.

The program retrieves URLs from the 'Pages' table one by one and parses the HTML content. It ignores non-text/html pages and pages that return a status code other than 200. It then extracts all the anchor tags from the page and inserts the links into the 'Pages' table if they belong to any of the 'Webs' in the database. It also inserts the links into the 'Links' table.

The program continues this process until it has retrieved a specified number of pages or until there are no more unretrieved pages in the 'Pages' table. The user can specify the number of pages to retrieve or exit the program by pressing Enter without entering a value.

If the program is stopped before completing its crawl, it can be restarted by running the program again. If the 'spider.sqlite' file is deleted, the program will start a fresh crawl.