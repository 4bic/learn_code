import urllib2

def download(url, user_agent='dcloud', num_retries):
    # catch these exceptions:
    print 'Downloading: ', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print "Download Error : ", e.reason
        html = None
        # retries the 5xx errors
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code <= 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries-1)

    return html

if __name__ == '__main__':
    url = 'http://httpstat.us/500'
    num_retries = 5
    # url= 'http://supplier.treasury.go.ke/site/tenders.go/index.php/public/tenders'
    download(url, num_retries)
