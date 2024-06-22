import pandas as pd 
from io import StringIO
import os
current_file = os.getcwd()
data_file_location =os.path.join(current_file,'file_location.txt')

with open(data_file_location,'r') as file:

    file = file.readline()
    fileid = file


def filter_data_show(file=fileid,id=None):

    with open(file, 'r') as file:
        file_contents = file.read()

    df = pd.read_csv(StringIO(file_contents))
    df.columns = df.columns.str.upper()
    #print(df)

    filter_data = df[(df['ITEM NAME']==str(id)) | (df['UNIQID2']==str(id)) | (df['UNIQID3']==str(id)) | (df['SKU']==str(id)) ]
    sizes = filter_data['SIZE'].unique()
    colors = filter_data['COLOUR'].unique()


    data = [id,sizes,colors]
    return data

def data_filtar(file=file,id=None,color=None,size=None):
    with open(file, 'r') as file:
        file_contents = file.read()

    df = pd.read_csv(StringIO(file_contents))
    df.columns = df.columns.str.upper()

    final_data = df[((df['ITEM NAME']==str(id)) | (df['UNIQID2']==str(id)) | (df['UNIQID3']==str(id)) | (df['SKU']==str(id)))&(df['SIZE']==size)&(df['COLOUR']==str(color))]

    sku = final_data['SKU CODE'].tolist()
    tally = final_data['TALLY CODE'].tolist()
    link = final_data['LINK'].tolist()


    data =[sku,tally,link,id,color,size]
    #print(data)
    return data

#filter_data_show(file=file,id=412)
#data_filtar(file=file,id=412,color='LGN',size=36)
