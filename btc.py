import urllib.request
import notify2
import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
while True:
	notify2.init('BTC Price')
	page='https://www.coingecko.com/en/price_charts/bitcoin/inr'
	req = Request(page, headers={'User-Agent': 'Mozilla/5.0'})
	coin_page=urlopen(req)

	soup = BeautifulSoup(coin_page, 'html.parser')

	btc=soup.find_all('tbody')

	btc1=btc[2].find_all('td')





     


#print(btc1[3].text)
#print(btc1[5].text)
	if(float(btc1[3].text)>float(btc1[5].text)):
		a=((float(btc1[3].text)-float(btc1[5].text))/float(btc1[3].text))*100
		a=round(a,2)
		t="Rise of "+str(a)+"%"
		n = notify2.Notification('Percentage Change in BTC Price', t,icon='/media/himanshu/New Volume/project/webscarpe/btcimg(1).png')


	elif(float(btc1[3].text)<=float(btc1[5].text)):
		a=((float(btc1[5].text)-float(btc1[3].text))/float(btc1[5].text))*100
		a=round(a,2)
		t="Fall of "+str(a)+"%"
		n = notify2.Notification('Percentage Change in BTC Price', t,icon='/media/himanshu/New Volume/project/webscarpe/btcimg(1).png')
	n.show()
	time.sleep(30)







	   







#n = notify2.Notification('foo00', btc1[3].text,btc1[5].text)

