
# coding: utf-8

# In[ ]:

from classes.utils.utils import utils

class plot_seaborn:
    def __init__(self):
        self.utils = utils()
        
    def plot_seaborn_category(df,col,top_count,start,plotname,palette):
        sns.set(style="darkgrid")
        count = utils.get_top_values_from_dict(df,col,top_count)
        d = df[df[col].isin(list(count.keys())[start:])]
        if start>0:
            print("Largest set: ",dict(utils.take(start,count.items())))
        var = list(count.keys())[0]
        total = sum(list(count.values()))
        ax = sns.countplot(x=col,data=d,order=d[col].value_counts().index,palette=palette)
        if isinstance(var,int):
            #' \n (' +str(count[int(ax.get_xticklabels()[i].get_text())])+')'
            labels = [str(int(float(ax.get_xticklabels()[i].get_text()))) + ' \n (' +str(round(count[int(float(ax.get_xticklabels()[i].get_text()))]/total*100,2))+'%)'  for i in range(len(ax.get_xticklabels()))]
        elif isinstance(var,str): 
            #' \n (' +str(count[ax.get_xticklabels()[i].get_text()])+')'
            labels = [ax.get_xticklabels()[i].get_text() + ' \n (' +str(round(count[ax.get_xticklabels()[i].get_text()]/total*100,2))+'%)'  for i in range(len(ax.get_xticklabels()))]
        else: 
            #' \n (' +str(count[ax.get_xticklabels()[i].get_text()])+')'
            labels = [ax.get_xticklabels()[i].get_text() + ' \n (' +str(round(count[int(ax.get_xticklabels()[i].get_text())]/total*100,2))+'%)'  for i in range(len(ax.get_xticklabels()))]

        ax.set_xticklabels(labels,rotation=60)
        ax.set_title(plotname)
        ax.set_xlabel(col)

        def change_width(ax, new_value) :
            for patch in ax.patches :
                current_width = patch.get_width()
                diff = current_width - new_value

                # we change the bar width
                patch.set_width(new_value)

                # we recenter the bar
                patch.set_x(patch.get_x() + diff * .5)

        if len(labels) <=1:
            change_width(ax,.1)
        elif len(labels) <= 5 and len(labels) >1:
            change_width(ax,.5)

        for p in ax.patches:
            ax.annotate('{:}'.format(p.get_height()), (p.get_x()+0.1, p.get_height()+0.1))


        fig.tight_layout()
        if start>0:
            ax.text(.8, .8, str(dict(take(start,count.items()))),
                    horizontalalignment='right',verticalalignment='bottom',
                    transform=ax.transAxes,size='medium', color='black')
        return ax


