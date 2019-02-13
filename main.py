from google import google
import urllib.request
import requests
import shutil


URL = 'https://legendei.com/'


def get_url(search_param):
    results = google.search(search_param, 1)
    for res in results:
        print(res.link)
        if URL in str(res.link):
            print('found a match for {} in: {}'.format(search_param, URL))
            return res.link

    raise Exception('Nothing found :(')


def get_page_html(url):
    print('accessing {}'.format(url))
    page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    request = urllib.request.urlopen(page)
    encoded_html = request.read()
    decoded_html = encoded_html.decode('utf8')
    print('page downloaded')
    return str(decoded_html)


def get_download_innerlink(html):
    print('getting inner download link')
    start_index = html.find('dld5')
    inner_link = ''
    for i in range(start_index, len(html)):
        if html[i] != '"':
            inner_link += html[i]
        else:
            break
    print('inner link found: ' + inner_link)
    return inner_link


def get_download_link(search_param):
    url = get_url(search_param)
    html = get_page_html(url)
    print('getting download link')
    link = url + get_download_innerlink(html)
    print('download link builded: ' + link)
    return link


def download_file(url):
    print('Beginning file download...')

    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open("sub.zip", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

    print('download file finished')


if __name__ == '__main__':
    # exemple
    dl_link = get_download_link('The.Simpsons.S30E13.WEB.x264-TBS-TBS-TBS')
    download_file(dl_link)
