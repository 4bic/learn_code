import urllib2 as ur
import re
def download(url, num_retries): #
    # catch these exceptions:
    print 'Downloading: ', url
    user_agent='dcloud'
    headers = {'User-agent': user_agent}
    request = ur.Request(url, headers=headers)
    try:
        html = ur.urlopen(url).read()
    except ur.URLError as e:
        print "Download Error : ", e.reason
        html = None
        # retries the 5xx errors
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code <= 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries-1)

    return html

# Sitemap crawler
def crawl_sitemap(url):
    # download sitemap file
    sitemap = download(url, num_retries)
    # extract links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)

# crawl links
def link_crawler(seed_url, link_regex):
    #  Crawl from the given seed URL following links matched by link_regex
    crawl_queue = [seed_url]

    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        # filter for links matching regular expression
        for links in get_links(html):
            if re.match(link_regex, link):
                crawl_queue.append(link)

def get_links(html):
    # return list of links available
    # extract all links from webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',
                    re.IGNORECASE)
    # list links from webpage
    return webpage_regex.findall(html)



if __name__ == '__main__':
    # url = 'http://httpstat.us/500'
    num_retries = 5
    # url= 'http://supplier.treasury.go.ke/site/tenders.go/index.php'
    url = 'http://supplier.treasury.go.ke/site/tenders.go/index.php/public/'
    link_regex = url/tenders/
    download(url, num_retries)
    crawl_sitemap(url)
    link_crawler(seed_url, link_regex)
