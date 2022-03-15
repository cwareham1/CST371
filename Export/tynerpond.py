import re

#regex
def regex(html):
    rawlist = re.findall(
        r"<a.*?<h4 class=\"title\">(.*?)</h4>.*?<span class=\"price\".*?((?:[0-9]{1,2}\.[0-9]{2}).*?)</span>.*?</a>"
        , html)

    #make temp lists
    prodlist = []
    prices = []
    savings = []
    for i in rawlist:
        prodlist.append(i[0])
        prices.append(i[1])
        savings.append(None)

    #clean product names
    for i in range(len(prodlist)):
        prodlist[i]  = re.search(r"[a-zA-Z\s\u2019\~\/\,\$\.\%\u002D\(\)\u20130-9]*", prodlist[i]).group(0)

    #clean prices and savings
    for i in range(len(prices)):
        numlist = re.findall(r"([0-9]{1,2}\.[0-9]{2}\.{0,5}).*?([0-9]{1,2}\.[0-9]{2}\.{0,5})*?", prices[i])
        prices[i] = numlist[0]
        if len(numlist) == 2:
            savings[i] = numlist[1]
    return prodlist, prices, savings