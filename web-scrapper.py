# scraps a website
from urllib2 import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.goforevent.com/jntua_pixel18/cse_dashboard.php'

# opening the connection
uclient = ureq(my_url)
pagehtml = uclient.read()
uclient.close()

# html parser
page_soup= soup(pagehtml, 'html.parser')

# grabs all products
rows = page_soup.select('tr')
file = open('sample.txt', 'w')
sum = 0
for i in range(1,len(rows)):
  rows_i = rows[i].select('td')
  # file.write(rows_i[2].text +" "+ rows_i[3].text + "\n")
  sum = sum + float(rows_i[3].text)
file.write(str(sum))
file.close();