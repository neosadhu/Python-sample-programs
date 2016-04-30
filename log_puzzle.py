#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

#####################
#website for the puzzles https://developers.google.com/edu/python/exercises/log-puzzle#part-a---log-file-to-urls

import os
import re
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def url_sort_helper(url):   #sorts out the website from apache log files and puts them in an increasing order.
    check_pattern=re.search('.*/puzzle/\w-(.*).jpg',url)
    animal_pat='.*/a-(\w+)'
    place_pat='.*/p-\w+-(\w+)'

    if '-' in check_pattern.group(1):
        pattern=re.search(place_pat,url)
    else:
        pattern=re.search(animal_pat,url)

    return (pattern.group(1))



#reads the apache log file  and returns a sorted list of urls of images

def read_urls(filename):
    f=open(filename,'r')
    file_1=f.read()
    pattern='.*GET (.*/puzzle.*.jpg)'
    url_list=sorted(list(set(re.findall(pattern,file_1))), key=url_sort_helper)
    #url_list=sorted(list(set(re.findall(pattern,file_1))))


    for url in range(len(url_list)):
        url_list[url]='http://code.google.com/'+ url_list[url]
    return url_list





#downloads the image from the list of url and constructs a html file that puts the image back in order.

def download_images(img_urls,dir_path):
    '''
    Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.'''
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

  # +++your code here+++]
    images_path=[]
    for i,url in enumerate(img_urls):
        print ('Downloading Image:',i)
        images_path.append('<img src="{0}/image{1}.jpg">'.format(dir_path,i))
        urllib.request.urlretrieve(url,'image/image%d.jpg' %i) # retrives images from the websites

    index_file=open('index.html', 'a')
    html_string= '''<verbatim>
    <html>
    <body>
    %s
    </body>
    </html>
    '''% (''.join(images_path))

    index_file.write(html_string)
    index_file.close()





##########################################################
#download_images(read_urls('animal_code.google.com'),'image')


def main():
    inp=input('Input Filename ')
    inp=inp.split()

    download_images(read_urls(inp[0]),inp[1])


if __name__ == '__main__':
  main()
