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

def prep_zillow_final(cached=True):
    '''
        This function obtains all zillow data for single family units,
        renames the columns,
        and converts it into our prefered final state
        by dropping or filling null values and dealing with zeros.
    '''
    df = get_zillow_data()
    columns_to_drop = ['airconditioningtypeid', 'architecturalstyletypeid', 'basementsqft', 'buildingclasstypeid',
                  'decktypeid', 'finishedfloor1squarefeet', 'finishedsquarefeet12', 'finishedsquarefeet13',
                  'finishedsquarefeet15', 'finishedsquarefeet50', 'finishedsquarefeet6', 'fireplacecnt',
                  'hashottuborspa', 'poolsizesum', 'pooltypeid10', 'pooltypeid2', 'pooltypeid7', 'storytypeid',
                  'threequarterbathnbr', 'typeconstructiontypeid', 'yardbuildingsqft17', 'yardbuildingsqft26',
                  'fireplaceflag', 'taxdelinquencyflag', 'taxdelinquencyyear', 'id', 'buildingqualitytypeid',
                  'calculatedbathnbr', 'latitude', 'longitude', 'propertylandusetypeid', 'rawcensustractandblock',
                  'regionidcity', 'regionidcounty', 'regionidneighborhood', 'regionidzip', 'unitcnt',
                  'structuretaxvaluedollarcnt', 'landtaxvaluedollarcnt', 'assessmentyear', 'taxamount',
                  'censustractandblock', 'transactiondate', 'propertyzoningdesc', 'logerror', 'parcelid',
                  'numberofstories', 'garagecarcnt', 'garagetotalsqft', 'heatingorsystemtypeid', 'propertycountylandusecode']
    df = df.drop(columns=columns_to_drop)
    df = df.drop(columns=['id.1', 'parcelid.1'])
    df = df.rename(columns={'bathroomcnt': 'bathroom', 'bedroomcnt': 'bedroom', 'calculatedfinishedsquarefeet': 'sqft',
                        'taxvaluedollarcnt': 'propertytaxvalue', 'lotsizesquarefeet': 'lotsqft'})
    df['poolcnt'] = df.poolcnt.fillna(0)
    df['roomcnt'] = np.where(df['roomcnt'] == 0.0, (df.bathroom + df.bedroom), df['roomcnt'])
    df = df[~df['fullbathcnt'].isna()]
    df = df[df['bedroom'] != 0]
    df = df[~df['lotsqft'].isna()]
    df = df[~df['yearbuilt'].isna()]
    return df