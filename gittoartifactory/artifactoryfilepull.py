
import requests
import hashlib
import shutil
import os
import re
import getpass
from sys import platform

def pullfilefromartifactory(*args, **kwargs):
    try:
        
        artifactory_url = raw_input("User Please Enter Artifactory URL : ")

        #artifactory_url = "http://153.64.146.90:8080/artifactory/OSAT-STABLE/Test2/svn2git"       # your artifactory instance

        artifactory_username = raw_input("User Please Quicklook Id : ")

        #artifactory_username = 'vs186041'         # your username

        artifcatory_password = getpass.getpass('Password:')


        filename = artifactory_url.split('/')[-1]
        dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        import requests
        response = requests.get(artifactory_url, auth = (artifactory_username,artifcatory_password), stream=True)
        if platform == 'win32':
            drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d) and d != 'C']
            if len(drives) >= 1:
                pathlocation = drives[0]
                pathlocation = pathlocation + '/' + filename
                print ("\n")
                print ("*" * 50)
                print " Downloading file at {} in Progress......".format(pathlocation)
                with open(pathlocation, 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
            else:
                pathlocation = 'C:'
                pathlocation = pathlocation + '/' + filename
                with open(pathlocation, 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
        else:
            pathlocation = os.path.expanduser("~")
            pathlocation = pathlocation + '/' + filename
            print ("\n")
            print ("*" * 50)
            print (" Downloading file at {} in Progress......".format(pathlocation))
            with open(pathlocation, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
        print  ("Succesfully Downloaded file.... User can check file under location {}".format(pathlocation))

    except Exception, e:
        print ("something went wrong!!!!", e)
