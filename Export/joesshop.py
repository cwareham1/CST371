import re

def regex(html):
    # regex
    rawlist = re.findall(
        r"<p>([a-zA-Z\s\u2019\u002D\(\)\u20130-9]*).*?<strong>.*?([0-9]{1,2}\.[0-9]{2}.{0,5}).*?</strong>(?:.*?([0-9]{1,2}\.[0-9]{2})*.*?)*</p>"
        ,html)

    return rawlist
    
    