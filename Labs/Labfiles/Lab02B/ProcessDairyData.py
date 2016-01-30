# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 20:57:58 2016

@author: Filip
"""

def azureml_main(frame1):
  import pandas as pd
  import os.path

## Set a flag to define the environment
  Azure = False 

## If in Azure, the data frame is passed to the function,
## If running in the IDE, load it from a local file
  if(Azure == False):
    pathName = "C:\\Users\\Filip\\Source\\Repos\\Data-Science-and-ML-Essentials\\Labs\\Labfiles\\Lab02B\\"
    fileName = "cadairydata.csv"
    filePath = os.path.join(pathName, fileName)
    frame1 = pd.read_csv(filePath)

## Select a subset of columns
  frame1 = frame1[["Year", "Month", "Cottagecheese.Prod", "Icecream.Prod", "Milk.Prod"]]

## Filter and add a column to show totals for August
  frame1 = frame1[frame1['Month']=='Aug']
  frame1["Total.Prod"] = frame1["Cottagecheese.Prod"] + frame1["Icecream.Prod"] + frame1["Milk.Prod"]
  return frame1
