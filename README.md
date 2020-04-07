# Homework 3

In this homework, we will analyze data related to cases
of COVID-19.

# Data

The data we will use comes from a New York Times
[Github repository](https://github.com/nytimes/covid-19-data).
It contains data from the United States, and it is
updated daily. There are two datasets, one is
by county, and the other is by state. For more information
about the data, please read the repository's
`README.md`.


# Setup

You can import the data directly from Github by using
pandas and the raw Github data
[(tutorial)](https://projectosyo.wixsite.com/datadoubleconfirm/single-post/2019/04/15/Reading-csv-data-from-Github---Python).

Since this data is updated frequently (several times per day),
this method is preferable to downloading a static data file.

```python
# get state-level data
pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')

# get county-level data
pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
```

Use the tools and techniques from the Python labs
that demonstrate how to use `pandas`. Some parts
of the assignment were already completed during labs.

<!--  -->
# Scoring
This assignment will be graded out of 12 points. There is a
maximum of 16 possible points.

## 1. Summarize the data (4 points)

1. What is the _percent_ increase in cases each day?
2. What is the _percent_ increase in deaths each day?
3. Which state has the highest case fatality rate as of the most
   recent day? Which is the lowest? Case fatality rate is the
   number of deaths divided by the number of cases.
4. Which county has the highest case fatality rate as of the most
   recent day?

## 2. Visualize the data (4 points)

1. Plot the total number of cases & deaths in the US for each day.
2. Plot the case fatality rate in the US for each day. Case
   fatality rate is the number of deaths divided by the number
   of cases.
3. Plot the case _growth rate_ in the US for each day.
4. Plot the case _growth rate_ for three states for each day.


## 3. Get insights from the data (4 points)

1. Which states had the most new cases in the previous day (top 5)?
2. Which counties had the most new cases in the previous day (top 5)?
3. Which states had the greatest percentage increase cases in the
   previous day (top 5)?
4. Which counties had the greatest percentage increase in cases in
   in the previous day (top 5)?

## 4. Conduct your own analysis (up to 4 points)
You may run an analysis of your choosing that is not included
in the above sections, for a maximum of four points. The analyses
should be at least as substantial as those in the above
sections to receive credit. You can also look at other related
datasets. Johns Hopkins has
[worldwide data](https://github.com/CSSEGISandData/COVID-19).

# Submission

Commit and push your code to this Git repository. The
instructor will grade the last commit before the due
date.
