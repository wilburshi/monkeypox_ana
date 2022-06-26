# This is a analysis for monkey pox trend based on open source data set from Kaggle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

country_daily_cases = pd.read_csv('Daily_Country_Wise_Confirmed_Cases.csv')
worldwide_cases = pd.read_csv('Monkey_Pox_Cases_Worldwide.csv')
worldwide_detection_timeline = pd.read_csv('Worldwide_Case_Detection_Timeline.csv')
