



def pushfiletoartifactory(*args, **kwargs):
    import requests
    import hashlib
    import shutil
    import os
    import re
    import getpass

    artifactory_url = raw_input("User Please Enter Artifactory URL : ")

    #artifactory_url = "http://**************/artifactory/OSAT-STABLE/Test2/svn2git"       # your artifactory instance


    filelocation = raw_input("User Please Enter file location which need to be pushed to Artifactory :")

    artifactory_username = raw_input("User Please enter Quicklook Id : ")

    #artifactory_username = 'vs186041'         # your username

    artifcatory_password = getpass.getpass('Password:')

    filename = filelocation.split('/')[-1]
    upload_url = artifactory_url + '/' + filename
    content_type = 'application/archive'

    # checksums are useful for making sure the upload was successful

    md5_checksum = hashlib.sha1(open(filelocation).read()).hexdigest()

    headers = {'content-type': content_type,
               'X-Checksum-Md5': hashlib.md5(open(filelocation).read()).hexdigest(),
               'X-Checksum-Sha1': md5_checksum}

    
    print ("File transferring to location file {} in Progress......".format(upload_url))
    # pushing file data to Artifactory

    with open(filelocation, 'rb') as f:
        response = requests.put(upload_url ,auth=(artifactory_username , artifcatory_password ),data=f, headers=headers)

    # check for success
    if response.status_code != 201:
        raise Exception("something went wrong!!!!")
    else:
        DownloadURL =  response.json()['downloadUri']  # download url for this new artifact
        print   "Succesfully done you can download repo from Location : {} ".format(DownloadURL)


