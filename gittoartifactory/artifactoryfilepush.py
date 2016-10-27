import requests
import hashlib
import getpass

def pushfiletoartifactory(targetLocation , *args, **kwargs):

    try:
        pre_check(targetLocation)

        # Intializing Variables required

        artifactory_url = raw_input("User Please Enter Artifactory URL : ")

        #artifactory_url = "http://153.64.146.90:8080/artifactory/OSAT-STABLE/Test2/svn2git"       # your artifactory instance
        
        filelocation = raw_input("User Please Enter file location Example: /root/filename (or) D:/filenmae :")

        artifactory_username = raw_input("User Please Quicklook Id : ")

        #artifactory_username = 'vs186041'         # Quicklook Id :

        artifcatory_password = getpass.getpass('Password:')


        filename = filelocation.split('/')[-1]
        
        upload_url = artifactory_url + '/' + filename
        
        content_type = 'application/archive'
        
        # checksums are useful for making sure the upload was successful

        md5_checksum = hashlib.sha1(open(value).read()).hexdigest()

        headers = {'content-type': content_type,
                   'X-Checksum-Md5': hashlib.md5(open(value).read()).hexdigest(),
                   'X-Checksum-Sha1': md5_checksum}

        # pushing file data to Artifactory

        with open(value, 'rb') as f:
            response = requests.put(upload_url ,auth=(artifactory_username , artifcatory_password ),data=f, headers=headers)

        # check for success

        if response.status_code != 201:
            raise Exception("something went wrong!!!!")
        else:
            DownloadURL =  response.json()['downloadUri']  # download url for this new artifact
            print   "Succesfully done you can download repo from Location : {} ".format(DownloadURL)
    except Exception,e:
        print "Exception raised : ", e

