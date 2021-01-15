import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# url = "http://py4e-data.dr-chuck.net/comments_42.xml"
url = "http://py4e-data.dr-chuck.net/comments_1129228.xml"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(data)

counts = tree.findall('.//count')

result = sum(map(lambda x: int(x.text), counts))

print(result)
