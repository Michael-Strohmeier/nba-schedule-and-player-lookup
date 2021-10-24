import urllib.request
from bs4 import BeautifulSoup


def url_to_soup(url: str) -> BeautifulSoup:
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'cookie': 'visid_incap_1712983=Dfo+CVLdTCSzMHcIXEgPSb1y7l0AAAAAQUIPAAAAAAAetg/EHDkFJUigbIo4eaK4; incap_ses_532_1712983=dFrgDpkdqkYCF1u+mQxiB71y7l0AAAAAksMc42V5CJx6OdUZdeHflA==; has_js=1; _ga=GA1.2.626207180.1575908117; _gid=GA1.2.512657448.1575908117; __utma=158387685.626207180.1575908117.1575908117.1575908117.1; __utmc=158387685; __utmz=158387685.1575908117.1.1.utmcsr=(direct)^|utmccn=(direct)^|utmcmd=(none); __utmt=1; __utmt_b=1; _aeaid=5e12b9d6-0171-4fde-8ccf-1bba809a1bb2; aeatstartmessage=true; __utmb=158387685.4.10.1575908117',
        }

    url_request = urllib.request.Request(url, data=None, headers=headers)
    url_response = urllib.request.urlopen(url_request)
    soup = BeautifulSoup(url_response, "html.parser", from_encoding="iso-8859-1")

    return soup
