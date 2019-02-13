from google import google
import urllib.request
import requests
import shutil


URL = 'https://legendei.com/'


class DownloadBot:

    def get_url(self, search_param):
        results = google.search(search_param, 1)
        for res in results:
            print(res.link)
            if URL in str(res.link):
                print('found a match for {} in: {}'.format(search_param, URL))
                return res.link

        raise Exception('Nothing found :(')

    def get_page_html(self, url):
        print('accessing {}'.format(url))
        page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        request = urllib.request.urlopen(page)
        encoded_html = request.read()
        decoded_html = encoded_html.decode('utf8')
        print('page downloaded')
        return str(decoded_html)

    def get_download_innerlink(self, html):
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

    def get_download_link(self, search_param):
        url = self.get_url(search_param)
        html = self.get_page_html(url)
        print('getting download link')
        link = url + self.get_download_innerlink(html)
        print('download link builded: ' + link)
        return link

    def download_file(self, url):
        print('Beginning file download...')

        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open("sub.zip", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

        print('download file finished')

    def start(self, search_param):
        dl_link = self.get_download_link(search_param)
        self.download_file(dl_link)
