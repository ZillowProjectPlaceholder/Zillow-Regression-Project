import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression, LassoLars
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error


########################### Pairplot Function ###########################


def plot_variable_pairs(df, drop_scaled_columns = True):
    '''
    This function takes in a DataFrame and plots all of the 
    pairwise relationships along with the regression line for each pair.
    '''
    if drop_scaled_columns:
        scaled_columns = [c for c in df.columns if c.endswith('_scaled')]
        df = df.drop(columns = scaled_columns)
    #to see all the plots at once, pairplot but with more customizations
    g = sns.PairGrid(df)
    #the plots is the diagonal will be a distribution plot
    g.map_diag(plt.hist) #one for a single variable
    #the plots not in the diagonal will be a scatter plot
    g.map_offdiag(sns.regplot) #one for the interaction of two variables
    plt.show()
    return g

########################### SelectKBest Function ###########################

def select_kbest(predictors, target, number_of_features):
    '''
    This function takes in predictors(features), a target variable and the number of top features we want
    and returns the top features that correlate with the target variable.
    '''
    #Initialize the f_selector object, 
    #which defines the test for scoring the features 
    #and the number of features we want to keep,
    f_selector = SelectKBest(f_regression, k = number_of_features)
    
    #fitting the data into the model
    #scoring, ranking and identifying the top k features
    f_selector = f_selector.fit(predictors, target)
    
    #creating a list of the features that remain
    f_support = f_selector.get_support()

    #We get a list of the feature names selected from 
    #X_train using .loc with our mask, 
    #using .columns to get the column names, 
    #and convert the values to a list using .tolist()
    f_feature = predictors.iloc[:, f_support].columns.tolist()

    return f_feature


########################### RFE Function ###########################

def rfe(predictors, target, number_of_features):
    '''
    This function takes in predictors(features), a target variable and the number of top features we want 
    and returns the top features that lead to the best performing linear regression model. 
    '''
    #Initialize the linear regression object
    lm = LinearRegression()
    
    #Initialize the RFE object, 
    #setting the hyperparameters to be our linear regression 
    #(as the algorithm to test the features on) 
    #and the number of features to be returned
    rfe = RFE(lm, number_of_features)

    #Fit the RFE object to our data. 
    #(This means create multiple linear regression models,
    #find the one that performs best, 
    #and identify the predictors that are used in that model.
    #Those are the features we want.)
    #Transform our X dataframe to include only 
    #the 'number_of_features' that performed the best
    rfe.fit_transform(predictors, target)

    #Create a mask to hold a list of the features that were selected or not
    mask = rfe.support_

    #We get a list of the feature names selected from 
    #X_train using .loc with our mask, 
    #using .columns to get the column names, 
    #and convert the values to a list using .tolist()
    X_reduced_scaled_rfe = predictors.iloc[:, mask].columns.tolist()

    return X_reduced_scaled_rfe

########################### Train Modeling Functions ###########################


def linearReg_train(X_train, y_train):
    '''
    This function creates a multilinear reression model 
    for the training dataframe
    '''
    # Initialize the Linear Regression Object
    lm = LinearRegression(normalize=True)
    # Fitting the data to model
    lm.fit(X_train, y_train)
    # Get the predicted y-values
    lm_pred = lm.predict(X_train)
    # Evaluate RMSE
    lm_rmse = mean_squared_error(y_train, lm_pred)**(1/2)
    return lm_rmse


def lassoLars_train(X_train, y_train, alpha = 1):
    '''
    This function creates a LASSO and LARS model 
    for the training dataframe
    '''
    # Initialize the LassoLars aplha variable
    lars = LassoLars(alpha)
    # Fitting the data to model
    lars.fit(X_train, y_train)
    # Get the predicted y-values
    lars_pred = lars.predict(X_train)
    # Evaluate RMSE
    lars_rmse = mean_squared_error(y_train, lars_pred)**(1/2)
    return lars_rmse


def poly_linearReg_train(X_train, y_train, degrees):
    '''
    This function creates a polynomial regression model 
    for the training dataframe
    '''
    pf = PolynomialFeatures(degree=degrees)
    # Fitting and transforming the data to model
    X_train_squared = pf.fit_transform(X_train)
    # Feeding the squared data into our linear model
    lm_squared = LinearRegression()
    # Fitting the squared data to model
    lm_squared.fit(X_train_squared, y_train)
    # Get the predicted y-values
    lm_squared_pred = lm_squared.predict(X_train_squared)
    # Evaluate RMSE
    lm_squared_rmse = mean_squared_error(y_train, lm_squared_pred)**(1/2)
    return lm_squared_rmse


########################### Validate Modeling Functions ###########################


def linearReg_validate(X_train, y_train, X_validate, y_validate):
    '''
    This function creates a multilinear reression model 
    for the validate or test dataframe
    '''
    # Initialize the Linear Regression Object
    lm = LinearRegression(normalize=True)
    # Fitting the data to model
    lm.fit(X_train, y_train)
    # Get the predicted y-values
    lm_pred = lm.predict(X_validate)
    # Evaluate RMSE
    lm_rmse = mean_squared_error(y_validate, lm_pred)**(1/2)
    return lm_rmse

def lassoLars_validate(X_train, y_train, X_validate, y_validate, alpha = 1):
    '''
    This function creates a LASSO and LARS model 
    for the validate or test dataframe
    '''
    lars = LassoLars(alpha)
    # Fitting the data to model
    lars.fit(X_train, y_train)
    # Get the predicted y-values
    lars_pred = lars.predict(X_validate)
    # Evaluate RMSE
    lars_rmse = mean_squared_error(y_validate, lars_pred)**(1/2)
    return lars_rmse

def poly_linearReg_validate(X_train, y_train, X_validate, y_validate, degrees):
    '''
    This function creates a polynomial regression model 
    for the validate or test dataframe
    '''
    pf = PolynomialFeatures(degree=degrees)
    # Fitting and transforming the train data to model
    X_train_squared = pf.fit_transform(X_train)
    # Fitting the validate data to model
    X_validate_squared = pf.transform(X_validate)
    # Feeding the squared data into our linear model
    lm_squared = LinearRegression()
    # Fitting the squared data to model
    lm_squared.fit(X_train_squared, y_train)
    # Get the predicted y-values
    lm_squared_pred = lm_squared.predict(X_validate_squared)
    # Evaluate RMSE
    lm_squared_rmse = mean_squared_error(y_validate, lm_squared_pred)**(1/2)
    return lm_squared_rmse