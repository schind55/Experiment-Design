
# coding: utf-8

'''
This class implements method for retrieving language, summary and description of all the libraries available in Pypi. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''

from urllib.request import urlopen
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

class PypiPackagesInformation:
    def __init__(self):
        self.req = ('https://pypi.org/simple')
    
    def get_packages(self):
        response = urlopen(self.req)
        the_page = response.read()
        soup = BeautifulSoup(the_page,"html5lib")
        #print(soup)
        libraries = soup.find_all('a')
        packages = [library.text for library in libraries]
        print("%d packages in pypi" %len(packages))
        return packages

    def getDescription(self,library):
        url = ('https://pypi.python.org/pypi/'+library+'/json')
        #print(url)
        description,language,summary = None,None,None
        try:
            results = urlopen(url)
            soup = BeautifulSoup(results.read(),"html5lib")
            data = soup.find('body').text
            d = json.loads(data)
            #print(d)
            try:
                description = (d['info']['description']).strip()
            except:
                pass
            try:
                summary = (d['info']['summary']).strip()
            except:
                pass
            try:
                language = d['info']['classifiers']
                for i in range(len(language)):
                    l = language[i]
                    if 'Programming Language' in l:
                        language = l.split('::')[1].strip()
                        break
            except:
                pass

        except:
            print(library + " not found!")
        return description,language,summary
    
    def get_pypi_packages_information(self):
        packages = get_packages()
        packages_description = []
        packages_language = []
        packages_summary = []
        for i in range(len(packages)):
            if i%25000==0:
                print("%d packages info retrieved" %i)
            description,language,keywords,summary = None,None,None,None
            try:
                description,language,summary = self.getDescription(packages[i])
            except:
                pass
            packages_description.append(description)
            packages_language.append(language)
            packages_summary.append(summary)
            #print(description,language)
        packages_info = pd.DataFrame({'package_name':packages,'package_description':packages_description,
                                      'language':packages_language,'summary':packages_summary})
        return packages_info
    

