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


if __name__ == '__main__':
    # url = 'http://httpstat.us/500'
    num_retries = 5
    # url= 'http://supplier.treasury.go.ke/site/tenders.go/index.php'
    url = 'http://supplier.treasury.go.ke/site/tenders.go/index.php/public/tenders/cat:1'
    download(url, num_retries)
    crawl_sitemap(url)
