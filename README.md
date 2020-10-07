<a id='section_6'></a>
# <h1><center>Zillow Regression Project</center></h1>
<center> Author: Matthew Mays, Gilbert Noriega </center>

[About the Project](#section_1) [Data Dictionary](#section_2) [Initial Hypotheses/Thoughts](#section_3) [Project Plan](#section_4) [How to Reproduce](#section_5)



<a id='section_1'></a>
## About the Project
___

### Background
> List background here.
If you use this dataset in your research, please credit the authors

___

### Goals
> My goal for this project is to create a model that will ___. I will deliver the following: acquire.py, prepare.py, model.py, report.ipynb, and predictions.csv
  
[back to the top](#section_6)

___

<a id='section_2'></a>
## Data Dictionary

| Features | Definition |
| :------- | :-------|
| Feature1 | definition |
| Feature2 | definition |

|  Target  | Definition |
|:-------- |:---------- |
|  target  | definition |

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
>    - acquire data from _____ (join tables)
>    - save as a pandas dataframe
>    - plot distribution

>- prepare
>    - address missing data
>    - address outliers
>    - create features
>    - split into train, validate, test

>- explore
>    - plot correlation matrix of all variables
>    - test each hypothesis
>    - plot the continuous variables using a swarmplot or boxplot

>- model and evaluation
>    - try different algorithms: decision tree, logistic regression, random forest, knn, svm
>    - which features are most influential?
>    - evaluate on train
>    - select top 3 +/- models to evaluate on validate
>    - select best model
>    - create a model.py that pulls all the parts together.
>    - run model on test to verify.

>- conclusion
>    - summarize findings
>    - make recommendations
>    - next steps
>    - how to run with new data.


[back to the top](#section_6)

___

<a id='section_5'></a>
## How to Reproduce

>1. Download data from 
>2. Install acquire.py, prepare.py and model.py into your working directory.
>3. Run the jupyter notebook.

[back to the top](#section_6)