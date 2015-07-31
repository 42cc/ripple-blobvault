import sys
import requests
import hashlib

checksum = 'b77b8fea7d5e05e6c7ed7c83dc6b9ddd'
blob_id = 'a02ffd556169ab78b77a137ab76b732006b50bf139c4082828411d5d113a7619'

url = ''
port = ''
for line in open('config.js', 'r').readlines():
    if 'exports.url = ' in line:
        url = line[line.find('"') + 1: line.rfind('"')]
    if 'exports.port = ' in line:
        port = line[line.find('=') + 2: line.rfind(';')]

if not url:
    sys.exit('Url not specified or set incorrectly')

if not port:
    sys.exit('Port not specified or set incorrectly')

blob_api_url = '%s:%s/v1/blob/%s' % (url, port, blob_id)

response = requests.get(blob_api_url)
r_text = response.text

assert checksum == hashlib.md5(r_text).hexdigest(), \
    'Blob checksum does not match'
