# for downloading a image from a specific URL
# import urllib.request # for python 3.x
import urllib # for python 2.x

url = 'http://blahblah'

# for Python 2.x
urllib.urlretrieve(url, "output.png")

# for Python 3.x
# urllib.request.urlretrieve(url, "output.png")