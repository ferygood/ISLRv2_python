# 2. Statistical Learning  

## Conceptual

**Q1.** For each of parts (a) through (d), indicate whether i. or ii. is correct, and explain your answer. In general, do we expect the performance of a flexible statistical learning method to perform better or worse than an inflexible method when :

a. The sample size n is extremely large, and the number of predictors p is small?  
Better. A flexible method will fit the data closer and with the large sample size, would perform better than an inflexible approach.

b. The number of predictors p is extremely large, and the number of observations n is small?  
Worse. A flexible method would overfit the small number of observations.

c. The relationship between the predictors and response is highly non-linear?  
Better. With more degrees of freedom, a flexible method would fit better than an inflexible one. 

d. The variance of the error terms, i.e. σ2=Var(ε), is extremely high?  
Worse. A flexible method would fit to the noise in the error terms and increase variance.  

**Q2.** Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.  
a. We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.  
Regression and inference with n=500 and p=3  

b. We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.  
Classification and prediction with n=20 and p=13  

c. We are interesting in predicting the % change in the US dollar in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the dollar, the % change in the US market, the % change in the British market, and the % change in the German market.  
Regression and prediction with n=52 and p=3
