from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import urllib
import time

fname = "drlin_parsed_table.txt"
try:
    fhandle = open(fname)#open html table to be parsed
except:
    print('File cannot be opened:',fname)
#pub_list1 = list()
pub_list2 = list()
inp = fhandle.read()
#print('No.of.chars in this file is: ', len(inp))
pub_list1 = inp.split('|')
for item in pub_list1:
    if(item in '0123456789' or item == ' ' or item == '|'):#if row item starts with a number, its not a publication. So, skip it.
        continue
    item = item.strip()
    pub_list2.append(item)

pub_list2 = filter(lambda s: not str(s).isdigit(), pub_list2)
    
#print(pub_list2)
#print('There are ',len(pub_list2), 'items in the list')
url_count = 0
url_init = "http://ieeexplore.ieee.org/search/searchresult.jsp"

def getDownloadUrl(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    pdf_url = soup.find_all('frame')[1]
    pdf_split = pdf_url['src'].split('?')
    pdf_download_url = pdf_split[0]
    return pdf_download_url

def getUrlFromText(s):
    url_init = "http://ieeexplore.ieee.org/search/searchresult.jsp?"
    params = {'newsearch':'true', 'queryText':s}
    url = url_init + urllib.urlencode(params)
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(18)
    try:
        mylink = driver.find_element_by_class_name('icon-pdf')
        next_url = mylink.get_attribute("href")
        print(next_url)
        #pdf_url = getDownloadUrl(next_url)
        r = requests.get(next_url)
        data = r.text
        soup = BeautifulSoup(data)
        pdf_url = soup.find_all('frame')[1]
        pdf_split = pdf_url['src'].split('?')
        pdf_download_url = pdf_split[0]
    except Exception as e:
        print("could not find url for text {s}".format(s=s))
        driver.close()
        return None
    driver.close()
    return pdf_download_url
    #driver.get(pdf_url)
    #wget -i /Users/lakshmi/Documents/drlin_website_work/lakshmi_work/pdf_files/abcd.pdf publications_list.txt
        #print('PDF not found')
def removePunctuation(str):
    for ch in ",.\n: '()":
        if ch in str:
            str = (str.replace(ch, "_"))
    return (str)

def writeToFile(pub,url):
    with open('wget.txt', 'a') as wget_handler:
        wget_handler.write("wget -O pdf_files/" + "{}".format(pub) + ".pdf" + " " + "{}\n".format(url))
    

results = []
failed_results = []
for i in pub_list2:
    print("search text -->", i)
    search_text = i
    output = getUrlFromText(i)
    if output is None:
        failed_results.append(i)
    else:
        #print "output for text {t} = ({o})".format(t=i, o=output)
        wget_file_name = removePunctuation(i)
        print('Pub after removing punctuation: ', wget_file_name)
        results.append(output)
        writeToFile(wget_file_name,output)
    print("#" * 20)
    

with open('my_results.txt', 'w') as f:
    f.write(str(results))
with open('failed_results.txt', 'w') as failed_files:
    failed_files.write(str(failed_results))
    
with open('pdf_url_list.txt', 'w') as file_handler:
    for url in results: 
        file_handler.write("{}\n".format(url))

    

    
    
    
        