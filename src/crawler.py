# DDS is the middle man 
# crawl like normal get urls and send to DDS


###########################Crawler Shell##############################
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime


# ===============
# Crawler Process
# =============== 


# for each link
#	robots: 
#	relevancy check on link 
#		relevency check on page 
#			get outlinks
#				pink outlinks to see which ones are up 
#				add valid links 
#			get data 

# This methods purpose is to use robot.parser or another plugin in order
# To more easily grab the permissions from the robots.txt file and crawl 
# In an unbiased and non intrusional way 
# def getRobots():


# this method will first check the relevancy of the link itself first and if it passes the relevancy check then 
# It will move to check the relevancy of the contents of the page on a basic level. 
def RelevancyCheck():
    return 0


# Permission Process Function
# ===========================
# Function to check the root directory for crawling Permissions
# -------------------------------------------------------------

# =============== ============= ===========  ========== =========
# Requirements    Inputs        Changes      Outputs    Throws 
# =============== ============= ===========  ========== =========
# None            List of links Hash Table   None       None
# =============== ============= ===========  ========== =========

# This function prematurly precosses each robots.txt file and stores them in 
# a hashtable with the key being the doc ID for the website and the value bing
# the rules of crawling for that website. 
# urllib.robotparser

def Permissions():
    return 0


# case check for email.
def StripURL(URL):
    stripped = ""
    copy = False
    for c in reversed(URL):
        if copy == True:
            stripped += c
        if c == '/':
            copy = True

    stripped = stripped[len(stripped)::-1]
    return stripped


def OutlinkCheck(OutLinks):
    for key in OutLinks:
        for link in OutLinks[key]:
            if link == None:
                continue
            if ("http" in link or "https" in link):
                try:
                    response = requests.get(link)
                except requests.exceptions.SSLError:
                    print("SSL Error")
                    continue
                except:
                    continue
                if response.status_code != 200:
                    # print("REMOVED: ", link)
                    OutLinks[key].remove(link)

            elif '/' in link:
                OutLinks[key].remove(link)

                if (link[0] != '/'):
                    link = '/' + link

                stripped_link = StripURL(key)
                stripped_link += link
                OutLinks[key].append(stripped_link)

            else:
                OutLinks[key].remove(link)

    return OutLinks


def FormatOutput(RawData, OutLinks, Time):
    OutLinksFinal = OutlinkCheck(OutLinks)
    OutLinksRet = {}
    RawDataFinal = RawData
    for key in OutLinksFinal:
        OutLinksRet[key] = {"links": OutLinksFinal[key], "status_code": 200}

    RawDataRet = {}
    for key in RawData:
        RawDataRet[key] = {"url": key, "body": RawData[key], "crawledDateTime": Time, "recrawlDateTime": Time}

    return OutLinksRet, RawDataFinal


# Crawling Process Function
# ===========================
# Function to crawl each website by each permission
# -------------------------------------------------------------

# ====================     =============     ========== ==============================
# Requirements             Inputs            Outputs    Throws
# ====================     =============     ========== ==============================
# Valid List of Links      List of links     None       Error if link no longer exists
# ====================     =============.    ========== ==============================


# This function crawls each page by the robots.txt permissions from the root
# directory. It grabs the raw text data from the website. It then grabs the
# outlinks from the websites and calls the Document Data Sore's API with the
# crawl time, raw text, and website link

def CrawlerProcess(links):
    RawData = {}
    OutLinks = {}
    for link in links:
        if (len(links) > 0):
            SpecificPageOutLinks = []
            try:
                page = requests.get(link)
            except requests.exceptions.SSLError:
                print("SSL Error")
                continue
            except:
                continue
            soup = BeautifulSoup(page.content, "html.parser")
            RawData[link] = soup.prettify()

            for OutLink in soup.find_all('a'):
                SpecificPageOutLinks.append(OutLink.get('href'))

            OutLinks[link] = SpecificPageOutLinks

            now = datetime.now()
            print("Crawling page " + link + " completed at " + now.strftime("%I:%M:%S %p"))

    return FormatOutput(RawData, OutLinks, datetime.now())

# debugging Purposes
# def main(links):
#	links = ["http://cs.rpi.edu/~goldsd/index.php", "https://science.rpi.edu/computer-science", "https://www.rpi.edu"]
#	links = ["https://www.rpi.edu"]
#	Crawler(links)

# links = ["http://cs.rpi.edu/~goldsd/index.php", "https://science.rpi.edu/computer-science", "https://www.rpi.edu"]
# main(links)


######################################################################