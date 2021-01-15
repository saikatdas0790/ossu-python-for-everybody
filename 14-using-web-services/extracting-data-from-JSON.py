import json
import urllib.request
import urllib.parse
import urllib.error
import ssl

# url = "http://py4e-data.dr-chuck.net/comments_42.json"
url = "http://py4e-data.dr-chuck.net/comments_1129229.json"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(url, context=ctx).read()

info = json.loads(data)
print('User count:', len(info["comments"]))

result = sum(map(lambda x: int(x["count"]), info["comments"]))

print(result)
