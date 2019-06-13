# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:57:43 2019

@author: chinmay
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm
data= pd.read_excel("C:\\Users\\chinmay\\Desktop\\WebsiteRatings.xlsx")
#print(data.head())
#print(data)

plt.figure(figsize=(12,6))
plt.scatter(data["User"],data["ratings"],c='blue')
print(data)
plt.xlabel("USERS")
plt.ylabel("RATINGS OUTOF 5")
plt.show

#now creating linear Approximation

x= data["User"].values.reshape(-1,1)
y= data["ratings"].values.reshape(-1,1)
reg= LinearRegression()
reg.fit(x,y)

#reg.coef_ and reg.intercept_ calculates the value of slope and C
print("The linear regression model is Y={:.5}X+ {:.5}".format(reg.coef_[0][0],reg.intercept_[0]))

#now creating predictions 
predictions=reg.predict(x)
plt.figure(figsize=(12,6))
plt.scatter(data["User"],data["ratings"],c='red')

plt.plot(data["User"],predictions,c='red',linewidth=2)
plt.xlabel("USERS")
plt.ylabel("RATINGS OUTOF 5")
plt.show

#Now accessig efficiency using RSquared model

x=data['User']
y=data['ratings']
x2=sm.add_constant(x)

est=sm.OLS(y,x2)
est2=est.fit()
print(est2.summary())

print("Enter user no.")
p=int(input())
rate=p*reg.coef_[0][0]+reg.intercept_[0]
print("User will rate",rate)