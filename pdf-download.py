# downloads a PDF file from the specified URL
import requests
chunk_size = 2000

url = 'http://blahblah.PDF'

r = requests.get(url, stream=True)

with open('output.pdf', 'wb') as fd:
  for chunk in r.iter_content(chunk_size):
    fd.write(chunk)
r.close()