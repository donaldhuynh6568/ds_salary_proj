#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 16:35:54 2021

@author: donaldhuynh
"""

import glassdoor_scraper as gs
import pandas as pd
path= "C:/Users/kimje/Documents/ds_salary_proj/chromedriver"

df= gs.get_jobs('Data Science', 5, False, path, 10)