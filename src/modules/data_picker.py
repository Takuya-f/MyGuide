import xmltodict
import urllib.request
import pprint


def get_ch_info():
	with urllib.request.urlopen('http://cal.syoboi.jp/chinfo.xml') as res:
		raw_xml = res.read()
		raw_ch_dict = xmltodict.parse(raw_xml)
		ch_dict = raw_ch_dict['rss']['channel']['item']
		for ch in ch_dict:
				print(ch)
			break
	
get_ch_info()
