import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from acquire import get_zillow_data
import sklearn.preprocessing



##################### Prep MVP Zillow Data ##################

def prep_zillow_mvp(cached=True):
    '''
    This function obtains all zillow data for single family units,
    renames the columns,
    and strips it into a minimum viable product
    by dropping null values and columns with zeros
    '''
    #obtain zillow data
    df = get_zillow_data()
    #only grabs columns needed for a minimum viable product
    df = df[['calculatedfinishedsquarefeet', 'bedroomcnt', 'bathroomcnt', 'taxvaluedollarcnt']]
    #renames columns
    df = df.rename(columns = {'calculatedfinishedsquarefeet': 'sqrft', 'bedroomcnt':'bedroom', 'bathroomcnt':'bathroom', 'taxvaluedollarcnt':'taxvalue'})
    #drops null values
    df = df.dropna()
    #drops bedrooms that have a zero
    df = df[df.bedroom > 0]
    #drops bathrooms that have a zeero
    df = df[df.bathroom > 0]
    return df


##################### Split MVP Zillow Data ##################

def zillow_split(df):
    '''
    This function splits a dataframe into train, validate, and test sets
    '''
    train_and_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_and_validate, test_size=.25, random_state=123)
    return train, validate, test


#################### Scale MVP Zillow Data Set #####################
def add_scaled_columns(train, validate, test, columns_to_scale):
    '''
    This function uses a MinMaxScaler to scale numeric columns
    and add them back to the original dataframe
    '''
    #initialize scaler function
    scaler = sklearn.preprocessing.MinMaxScaler()
    #adds '_scaled' to columns that will be scaled
    new_column_names = [c + '_scaled' for c in columns_to_scale]
    #fitting columns to be scaled
    scaler.fit(train[columns_to_scale])

    #adding scaled columns back into their respective dataframes
    train = pd.concat([
        train,
        pd.DataFrame(scaler.transform(train[columns_to_scale]), columns=new_column_names, index=train.index),
    ], axis=1)
    validate = pd.concat([
        validate,
        pd.DataFrame(scaler.transform(validate[columns_to_scale]), columns=new_column_names, index=validate.index),
    ], axis=1)
    test = pd.concat([
        test,
        pd.DataFrame(scaler.transform(test[columns_to_scale]), columns=new_column_names, index=test.index),
    ], axis=1)

    return train, validate, test

def scale_wrangle_mvp_zillow(cached=True):
    '''
    This function acquires prep_zillow_mvp data, 
    splits into train, validate, and test,
    scales the numeric columns using min-max scaling,
    and adds the scaled columns to the respective split data sets
    '''
    #loads mvp dataframe
    df = prep_zillow_mvp(cached)
    #splits data into train, validate, test
    train, validate, test = zillow_split(df)
    #identifies columns to be scaled
    columns_to_scale = ['sqrft', 'bedroom', 'bathroom']
    #scales columns
    train, validate, test = add_scaled_columns(train, validate, test, columns_to_scale)
    return train, validate, test