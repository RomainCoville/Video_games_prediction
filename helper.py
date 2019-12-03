# This py file will be used to store usefull function which will help during
# the construction of the recommender system

###### Imports ######

#Data manipulation
import pandas as pd
import numpy as np
import string
import re

#File manipulation
import os
import gzip
import ast

#####################

def parseDataFromFile(fname):
    """
    Function used to read and parse a given file.
    param : fname : file to parse name.
    """
    for l in open(fname):
        yield ast.literal_eval(l)


def user_dataframe(user_dict):
    """
    Function to return a data frame containing the information about a single user.
    param : user_dict : dictionnary of user info to render in a dataframe.
    """
    user_info = [(elt['item_id'],elt['item_name'],elt['playtime_forever']
                  ,elt['playtime_2weeks']) for elt in user_dict['items']]
    user_info_df = pd.DataFrame(user_info,columns = ['item_id','item_name','playtime_forever','playtime_2weeks'])

    user = pd.DataFrame(user_dict).drop(['steam_id','items_count','items','user_url'],axis = 1)
    user_df = pd.concat([user,user_info_df],axis = 1)

    return user_df

def text_cleaning(df,col):
    """
    Function to clean text data for every rows of a given columns in a dataframe.
    params: df : dataframe in which to clean the text dataframe.
            col : columns name where to apply the cleaning function.
    """
    df[col] = df[col].apply(lambda x: x.lower())
    df[col] = df[col].apply(lambda x: x.strip())
    df[col] = df[col].apply(lambda x: x.replace(' ',''))
    df[col] = df[col].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
    df[col] = df[col].apply(lambda x: re.sub(r'[^\x00-\x7f]',"",x))

def unique_elt(df,col):
    """
    Function to return a list of unique values contained in a Series of lists.
    params : df : dataframe on which to apply the function.
             col : dataframe's column on which to apply the function.
    """
    return list(set([a for b in df[col].tolist() for a in b]))





