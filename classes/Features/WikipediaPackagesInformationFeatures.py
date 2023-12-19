
# coding: utf-8

# In[15]:


#Import statements
from SPARQLWrapper import SPARQLWrapper, JSON
import requests 

class WikipediaPackagesInformationFeatures:
    def __init__(self,library_counts):
        self.library_counts = library_counts
        
    def get_sparql_query(self,library):  
        query = 'SELECT ?item ?typeLabel ?itemDescription WHERE {?item rdfs:label "'+library+'"@en. SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}'
        return query

    def get_wikipedia_api_query(self,library):
        query = 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&titles='+library+'&exsentences=3'
        print(query)
        return query 

    def get_sparql(self,library):    
        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setQuery(self.get_sparql_query(library))
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        return results

    def get_wikipedia_api(self,library):
        results = requests.get(self.get_wikipedia_api_query(library))
        #print(results)
        return results

    def get_wikipedia_packages_information_features(self):    
        usage = []
        for k,v in self.library_counts.items():
            #print(k)
            description = None
            results = self.get_sparql(k)
            for result in results["results"]["bindings"]:
                keys = result.keys()
                if 'itemDescription' in keys:
                    description = result['itemDescription']['value'] 
                    #print(description)
            if not description:
                description = self.get_wikipedia_api(k)
            #print(description)
            if description == '200':
                description = input("Enter the usage")
            usage.append(description)

        df = pd.DataFrame({'library':list(library_counts.keys()),'usage':usage})
        return df

