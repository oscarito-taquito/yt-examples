class CoExtract:

    def __init__(self, url):
        self.url = url

    def extract(self):
        url = self.url.split('/')[2]
        return url


url1 = "https://amazon.com/?id=BX12345"
url2 = "https://google.com/?id=main"

cleanUrl = CoExtract(url1)
print(cleanUrl.extract())

cleanUrl = CoExtract(url2)
print(cleanUrl.extract())

