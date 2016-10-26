



from setuptools import setup

setup(name='gittoartifactory',
      version='0.1',
      description='The package used to send/download files from/to Artifactory',
      url='https://github.com/vamsi151/gitartifactory',
      author='vamsi singuluri',
      author_email='vamsikrishna.singuluri@teradata.com',
      install_requires=[
          'requests'
      ],
      packages=['gittoartifactory'],
      zip_safe=False)
