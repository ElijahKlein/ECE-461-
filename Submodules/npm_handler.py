""" Name: Eric Chen 
    Date of Last Edit: 2/11/2023
    
    Purpose: Handles fetching github link from npm addresses

    Details: Retrieves HTML from link and uses regex to search for github link on the page. 
    
"""

import urllib.request as url
import re

def npm2git(url_input):
    webUrl = url.urlopen(url_input)

    if(webUrl.getcode() == 200):
        html_cont = webUrl.read().decode("utf-8")
        r1 = r'<span id="repository-link">(.*?)<\/span>'
        try:
            reg_out = re.search(r1, html_cont)
            return ("https://" + reg_out.group(1))
        except:
            raise Exception("Valid github link not found, please ensure npm project is correct")

    else:
        raise Exception("npm url not able to connect, please etry again later or enter valid url")


def main(): #Originally test code, pls no judge
    webUrl = url.urlopen("https://www.npmjs.com/package/express")

    print ("result code: " + str(webUrl.getcode()))
    html_cont = webUrl.read().decode("utf-8")

    # with open("test_html.txt", "wb+") as f:
    #     f.write(html_cont)

    r1 = r'<span id="repository-link">(.*?)<\/span>'

    reg_out = re.search(r1, html_cont)
    print("https://"+reg_out.group(1))


if __name__ == "__main__":
    main()
