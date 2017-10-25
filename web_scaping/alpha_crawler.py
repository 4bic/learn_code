import urllib2

def download(url):
    # catch these exceptions:
    print 'Downloading: ', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print "Download Error : ", e.reason
        html = None

    return html

if __name__ == '__main__':
    url= 'http://supplier.treasury.go.ke/site/tenders.go/index.php/public/tenders'
    download(url)
