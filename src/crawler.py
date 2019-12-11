"""
Called from server.py program
crawls the specified links
grabs the raw data and outlinks from each link
checks the relevancy of each page
removes bad outlinks from list
formats data to coincide with DDS and LA standards

py:module:: crawler
:synopsis: Crawls webpages and filters results
"""
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from reppy.robots import Robots

def relevancy_check(link):
    """
    py:function:: relevancy_check(link)
    check if the page is relevant to RPI
    :param link: link from crawler_process()
    :type link: string of a url
    :returns True, False
    """
    check = False
    try:
        page = requests.get(link)
    except requests.exceptions.SSLError:
        print("SSL Error")
    except:
        print("Error")
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.prettify()
    if "RPI" in data:
        check = True
    if "Rensselaer Polytechnic Institute" in data:
        check = True
    if "Rensselaer" in data:
        check = True
    if "rpi" in data:
        check = True
    return check

def strip_url(url):
    """
    py:function:: strip_url(url)
    make sure that the url ends with a /
    to create valid links
    :param url: unformated url from outlink_check()
    :type url: string of url
    :returns stripped: formated string of url
    """
    stripped = ""
    copy = False
    for char in reversed(url):
        if copy:
            stripped += char
        if char == '/':
            copy = True
    stripped = stripped[len(stripped)::-1]
    return stripped

def outlink_check(out_links):
    """
    py:function:: outlink_check(out_links)
    check if each outlink is valid
    :param out_links: input list from format_output()
    :type out_links: list of outlink strings
    :returns out_links: list of valid outlink strings
    """
    for key in out_links:
        for link in out_links[key]:
            if link is None:
                continue
            if("http" in link or "https" in link):
                try:
                    response = requests.get(link)
                except requests.exceptions.SSLError:
                    print("SSL Error")
                    continue
                except:
                    continue
                if response.status_code != 200:
                    out_links[key].remove(link)
            elif '/' in link:
                out_links[key].remove(link)
                if link[0] != '/':
                    link = '/' + link
                stripped_link = strip_url(key)
                stripped_link += link
                out_links[key].append(stripped_link)
            else:
                out_links[key].remove(link)
    return out_links

def format_output(raw_data, out_links, time):
    """
    py:function:: format_output(raw_data, out_links, time)
    Formats dictionaries to format specified by DDS and LA
    :param raw_data: Dictionary of raw data matched with url
    :param out_links: Dictionary of list of out_links matched with url
    :param time: datetime object of crawled time
    :type raw_data: key is url data is string of raw html data from url
    :type out_links: key is url data us list of outlinks from url
    :type time: time crawled as datetime object
    :returns raw_data_ret: formated dic including url, raw data, crawled time, recrawl time
    :returns out_links_ret: formated dic including urls, corresponding list of outlinks
    """
    out_links_final = outlink_check(out_links)
    out_links_ret = {}
    raw_data_final = raw_data
    for key in out_links_final:
        out_links_ret[key] = {"links": out_links_final[key], "status_code" : 200}
    raw_data_ret = {}
    for key in raw_data:
        raw_data_ret[key] = {"url" : key,
                             "body" : raw_data[key],
                             "crawledDateTime" : time,
                             "recrawlDateTime" : time}
    return out_links_ret, raw_data_final

def robots_check(link):
    """
    py:function:: robots_check(link)
    Checks if webpage is allowed to be crawled
    :param link: link from crawler_process
    :type link: string containing the url
    :returns allow: true if allowed, false if not
    """
    robots = None
    allow = True
    url = Robots.robots_url(link)
    if 'http' in url:
        try:
            robots = Robots.fetch(url)
        except requests.exceptions.SSLError:
            print("SSLError")
            allow = False
        except:
            allow = False
    if not robots is None:
        allow = robots.allowed(link, 'agent')
    return allow

def crawler_process(links):
    """
    py:function:: crawler_process(links)
    Crawls each page and grabs raw html and outlinks
    :param links: list of links from server.py
    :type links: list of strings containing each url
    :returns result from format_output:
             raw_data_ret: formated dict including url, raw data, crawled time, recrawl time
             out_links_ret: formated dict including urls, corresponding list of outlinks
    """
    raw_data = {}
    out_links = {}
    for link in links:
        if len(links) > 0:
            specific_page_out_links = []
            try:
                page = requests.get(link)
            except requests.exceptions.SSLError:
                print("SSL Error")
                continue
            except:
                continue
            soup = BeautifulSoup(page.content, "html.parser")
            if relevancy_check(link) and robots_check(link):
                raw_data[link] = soup.prettify()
                for out_link in soup.find_all('a'):
                    specific_page_out_links.append(out_link.get('href'))
                out_links[link] = specific_page_out_links
            now = datetime.now()
            print("Crawling page " + link + " completed at " + now.strftime("%I:%M:%S %p"))
    return format_output(raw_data, out_links, datetime.now())
