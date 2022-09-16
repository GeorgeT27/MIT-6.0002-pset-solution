# Writeup Solution

**What difference does choosing a specific day to plot the data for versus calculating the yearly average have on our graphs (i.e., in terms of the R2​ values and the fit of the resulting curves)? Interpret the results.**

The average year data have a better R2 value as well as the ratio of standard error (which is twice higher for the year value).
It does make sense because if we take the data from one day which is not sensitive enough. Taking the average year data will "smooth" the data.

----
**Why do you think these graphs are so noisy? Which one is more noisy?**

The "Jan 1st" data is more noisy, because the data points are more spread out. In this case, we are only looking at the New York data. Therefore, probably NEW YORK have an unstable temperture which could cause the noise shown.

----
**How do these graphs support or contradict the claim that global warming is leading to an increase in temperature? The slope and the standard error-to-slope ratio could be helpful in thinking about this.**

The one with average year data supports the global warming idea because the gradient of the regression line is positive.There is a slight increase in temperture. However, it is not that reliable due to the low coefficient of determination.

----
**How does this graph compare to the graphs from part A ​(i.e., in terms ofthe R2​ ​ values, the fit of the resulting curves, and whether the graph supports/contradicts our claim about global warming)? Interpret the results.**

R2 value is much higher, Ratio of SE is much lower which means it is more reliable. We can now conclude there is a posstive correlation bewtween time and temperture, in other word, global warming is true.

----
**Why do you think this is the case?**

It seems if we want to predict global warming, we need data at least from different areas. The previous one have not enough data which produces high noise.

-----
**How would we expect the results to differ if we used 3 different cities?What about 100 different cities?**

For 3 different cities, I believe the noise will be more than the 21 cities. On the other hand, 100 cities will provide a regression model at least as good as the 21 cities one. However, potentially  we may need to consider the problem of overfitting.

----
**How would the results have changed if all 21 cities were in the same regionof the United States (for ex., New England)?**

I believe the data will be more dense, because the temperture will have a less varience. However, it doesn't answer the question which is about global warming.

----
**How does this graph compare to the graphs from part A and B (​i.e., in terms of the R2​ ​ values, the fit of the resulting curves, and whether the graph supports/contradicts our claim about global warming)?Interpret theresults.**

The data is even more accurate with a higher R2 value. There is less outlier.

----
**Why do you think this is the case?**

By looking at mean of each 5 years, we are minimizing the noise and get rid of any potiential outlier.

----
**How do these models compare to each other?**

The higher the degree of freedom is, the higher accuracy the model has.

----
**Which one has the best R2 ? Why?**

The last model where degreee of fit=20 has the highest R2. It is because more degree of freedom allows the curve to fit to the curver closely which reduces the error.

----
**Which model best fits the data? Why?**

The last one because it has the highest R2 value which means there is less variance between the estimated values and real values.

----
**How did the different models perform? How did their RMSEs compare?**

Model with degree=1 has the best RMSE, other model performed worse. The curve with degree=20 has the worst RMSE, this is because we overfitt the graph.

----
**Which model performed the best? Which model performed the worst? Are they the same as those in part D.2.I? Why?**

As I said in the previous answer, degree=1 performed the best and degree=20 performed the worst. They are not the same with the training data set. It shows the one score higher in the training data will not always be the optimum one in the testing data. It is because of overfitting.

----
**If we had generated the models using the A.4.II data (i.e. average annual temperature of New York City) instead of the 5-year moving average over 22 cities, how would the prediction results 2010-2015 have changed?**

The result will be less accurate and there would be a lot more noise as the New York data is more spread out compare to the 22 cities data. The RMSE of the result will probably be higher for the higher degree of freedom.

----
**Does the result match our claim (i.e., temperature variation is getting larger over these years)?**

It doesn't match the claim. It seems to be the time have a negative correlation to the temperture.

----
**Can you think of ways to improve our analysis?**

The relation between temperture and time is not quite a lienar relation,we should improve our analysis by trying higher degree model. We probably need more data points and a longer period for a better analysis. 

