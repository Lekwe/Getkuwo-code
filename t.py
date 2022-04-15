import requests
import headers

url = "http://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=music&httpsStatus=1&reqId=c3ca9201-4da8-11ec-bf5f-6321ab9e6552".format(
            197789527)
req = requests.get(url=url, headers=headers.headers).text
pe1 = req.split('"')[15]

