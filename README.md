<a id='section_6'></a>
<h1><center>Zillow Regression Project</center></h1>
<center> Author: Matthew Mays, Gilbert Noriega </center>

[About the Project](#section_1) [Data Dictionary](#section_2) [Initial Hypotheses/Thoughts](#section_3) [Project Plan](#section_4) [How to Reproduce](#section_5)



<a id='section_1'></a>
## About the Project
___

### Background
> We are junior data scientists on the Zillow data science team and are given a dataset containing millions of rows of data for houses in the United States. The "hot months" (in terms of real estate demand) are approaching quickly and the team needs to know what are the drivers for predicting single unit properties tax value. To complicate the matter, Zach lost the email that told us where these properties were located. Ugh, Zach :-/. Because property taxes are assessed at the county level, we would like to know what states and counties the properties are located in. Oh, did I forget to mention we needed it yesterday? 
>>
> So.... What are you waiting around for? Let's get started already!

___
>*Acknowledgement:The dataset was provided by Codeup from the MySequel Database* 

___

### Goals
> Our goal for this project is to create a model that will predict the values of single unit properties that the tax district assesses using the property data from those whose last transaction was during the months of May and June in 2017. We will deliver the following: 
>
> - a report in the form of a presentation
> - a github repository containing an acquire.py, prepare.py, model.py, and a jupyter notebook walkthrough
> - the distribution of tax rates for each county
  
[back to the top](#section_6)

___

<a id='section_2'></a>
## Data Dictionary

| Features | Definition |
| :------- | :-------|
| bathroom | the amount of bathrooms inside the home |
| bedroom  | the amount of bedrooms inside the home |
| sqft| the total square feet of the home |
| fips  | numeric codes which uniquely identify geographic areas |
| fullbathcnt | the amount of full bathrooms(shower included) inside the home |
| lotsqft  | the total square feet of the entire property |
| poolcnt | amount of pools at the home|
| roomcnt  | the total amount of rooms inside the home |
| yearbuilt | the year the home was built |

|  Target  | Definition |
|:-------- |:---------- |
|  propertytaxvalue  | value of properties that the tax district assesses |

[back to the top](#section_6)
___
<a id='section_3'></a>
## Initial Hypotheses & Thoughts

>### Thoughts
>
> - We could add a new feature?
> - Should I turn the continuous variables into booleans?

>### Hypotheses
>    - One Sample T-Test : A T-test lets us compare a categorical and a continuous variable by comparing the mean of the continuous variable by subgroups based on the categorical variable.
>       - H<sub>0</sub>: there is no difference between left-handers exam scores and the overall average.
>       - H<sub>a</sub>: there is a difference between left-handers exam scores and the overall average.

>   - Two Sample T-Test:  A T-test lets us compare a categorical and a continuous variable by comparing the means between two different supgroups. 
>        - H<sub>0</sub>: There is no difference in the exam scores for those who studied with flashcards and those who didn't.
>        - H<sub>a</sub>: There is a difference in the exam scores for those who studied with flashcards and those who didn't.

>    - Correlation: A correlation test lets us compare a continuous variabe with another continuous variable to see if there is a relationship, not a causation. 
>       - H<sub>0</sub>: There is no linear correlation between the number of hours studied and the score on the exam.
>       - H<sub>a</sub>: There is a linear correlation between the number of hours studied and the score on the exam.

>   - x<sup>2</sup>: The x<sup>2</sup> test can be used to compare two categorical variables to see if they are independent or dependent. 
>        - H<sub>0</sub>: Drive is independent of transmission type.
>        - H<sub>a</sub>: Drive is dependent of transmission type.

[back to the top](#section_6)
___
<a id='section_4'></a>
## Project Plan: Breaking it Down

>- acquire
>    - acquire data from MySQL
>       - join tables to include transaction date
>    - save as a pandas dataframe
>    - summarize the data
>    - plot distribution

>- prepare
>    - address missing data
>    - address outliers
>    - create features
>    - split into train, validate, test

>- explore
>    - plot correlation matrix of all variables
>    - test each hypothesis
>    - plot the continuous variables

>- model and evaluation
>    - which features are most influential: use SelectKBest and rfe
>    - try different algorithms: LinearRegression, LassoLars, Polynomial Regression
>    - evaluate on train
>    - select top 3 +/- models to evaluate on validate
>    - select best model
>    - create a model.py that pulls all the parts together.
>    - run model on test to verify.

>- conclusion
>    - summarize findings
>    - make recommendations
>    - next steps


[back to the top](#section_6)

___

<a id='section_5'></a>
## How to Reproduce

>1. Download data from zillow database in MySQL with Codeup credentials.
>2. Install acquire.py, prepare.py and model.py into your working directory.
>3. Run a jupyter notebook importing the necessary libraries and functions.
>4. Follow along in report.ipynb or forge your own exploratory path. 

[back to the top](#section_6)