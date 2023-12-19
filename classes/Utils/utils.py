
# coding: utf-8

# In[ ]:

class utils:
    def __init__(self):
        print("loading utils...")
    
    def take(self,n, iterable):
        "Return first n items of the iterable as a list"
        return list(islice(iterable, n))

    def get_top_values_from_dict(self,df,col,top_count):    
        count_all = Counter(list(df[col].values))
        count_sorted = dict(sorted(count_all.items(), key=lambda kv: kv[1], reverse=True))
        count_sorted.pop("", None)
        count_sorted.pop(None,None)
        count_top = dict(self.take(top_count,count_sorted.items()))
        return count_top
       
    def load_pickle(self,path,file):
        print("Loading Dataset...")
        df = pd.read_pickle(path+file)
        print("Done.")
        print("Shape of the dataset: ",df.shape)
        return df

    def load_csv(self,path,file):
        print("Loading Dataset...")
        df = pd.read_csv(path+file+'.csv')
        print("Done.")
        print("Shape of the dataset: ",df.shape)
        return df
  