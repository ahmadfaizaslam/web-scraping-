from requests_html import HTMLSession


class My_request_test:
    def test_requst(link):

        url = link
        s = HTMLSession()
        r = s.get(url)
        r.html.render(sleep=1)
        for x in range(20):
            try:
                articles = r.html.xpath(
                    f'///*[@id="main"]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/p[{x}]', first=True).text
                x = x + 1
                return articles
            except:
                continue


My_request_test.test_requst(
    'https://www.nst.com.my/news/nation/2021/05/689760/man-held-possessing-rm192000-worth-cough-mixture')
