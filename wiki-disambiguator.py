from expertai.client import ExpertAiClient
import requests
from requests import utils
import sys
import webbrowser
import os

eai = ExpertAiClient()

def insertLink(text,wikipediaLink,start,end):
	increased_length = len('<a href="'+wikipediaLink+'">''</a>')
	text = text[:start] + '<a href="'+wikipediaLink+'">'+text[start:end]+'</a>' +text[end:]
	return text, increased_length

def getWikipediaCode(wikidata_id, lang, debug=False): ## SOURCE:https://stackoverflow.com/questions/37079989/how-to-get-wikipedia-page-from-wikidata-id
	url = (
        'https://www.wikidata.org/w/api.php'
        '?action=wbgetentities'
        '&props=sitelinks/urls'
        f'&ids={wikidata_id}'
        '&format=json')
	json_response = requests.get(url).json()
	if debug: print(wikidata_id, url, json_response) 

	entities = json_response.get('entities')    
	if entities:
		entity = entities.get(wikidata_id)
		if entity:
			sitelinks = entity.get('sitelinks')
			if sitelinks:
				if lang:
					# filter only the specified language
					sitelink = sitelinks.get(f'{lang}wiki')
					if sitelink:
						wiki_url = sitelink.get('url')
						if wiki_url:
							return requests.utils.unquote(wiki_url)
				else:
					# return all of the urls
					wiki_urls = {}
					for key, sitelink in sitelinks.items():
						wiki_url = sitelink.get('url')
						if wiki_url:
							wiki_urls[key] = requests.utils.unquote(wiki_url)
					return wiki_urls
	return None   

def searchWikimedia(syncon, knowledge):
	for knowledge_item in knowledge:
		if(knowledge_item['syncon']==syncon and 'properties' in knowledge_item):
			properties = knowledge_item['properties']
			for propertie in properties:
				if(propertie['type']=='WikiDataId'):
					return propertie['value']
	return None

def disambiguate_wiki(text, language='en'):
	lenght_to_increase = 0
	response = eai.specific_resource_analysis(body={"document": {"text": text}}, params={'language': language, 'resource': 'disambiguation'})
	response_json = response.json
	data = response_json['data']
	tokens = data['tokens']
	knowledge = data['knowledge']
	for token in tokens:
		if 'syncon' in token:
			wikimediaCode = searchWikimedia(token['syncon'], knowledge)
			if(wikimediaCode!=None):
				wikipediaLink = getWikipediaCode(wikimediaCode, language)
				if(wikipediaLink!=None):
					start = token['start'] + lenght_to_increase
					end = token['end'] + lenght_to_increase
					text,increased_length = insertLink(text,wikipediaLink,start,end)
					lenght_to_increase+= increased_length
	return text

def main(argv):
	disambiguated_wiki = disambiguate_wiki(argv[0],language=argv[1])
	file = open("output.html", "w")
	file.write("<!DOCTYPE html>\n<html>\n<body>"+disambiguated_wiki+"\n</body>\n</html>")
	file.close()
	cwd = os.getcwd()
	url = 'file://'+cwd+'/output.html'
	webbrowser.open(url, new=2)  # open in new tab

if __name__ == "__main__":
   main(sys.argv[1:])