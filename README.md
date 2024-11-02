# Time Series Regression Models

This project implements time series regression models to analyze and forecast consumption expenditure and electricity prices. It leverages regression analysis to estimate parameters and evaluate model performance using various datasets.

## Project Overview

The project includes the following key tasks:

1. **Regression Model for Consumption Expenditure**:
   - Fit a regression model to the US consumption expenditure dataset, estimating the relationship between consumption (y), income (x1), and production (x2).

2. **Optimal Regression Model Selection**:
   - Using a cross-validation framework, select the optimal regression model structure from all available explanatory variables in the US consumption expenditure dataset.

3. **Electricity Price Forecasting**:
   - For the GEFCOM dataset, fit a regression model using the first 365 days of data for each hour. 
   - Plot the estimated parameters beta_1 and beta_2 for each hour.

4. **Enhanced Regression Model**:
   - Using the first 365 days, extend the analysis with additional explanatory variables, including lagged prices and electricity load forecasts. 
   - Here, D_{d,i} represents dummy variables for the day of the week. 

5. **Forecasting Electricity Prices**:
   - Use the estimated parameters from the enhanced regression model to produce price forecasts for the period covering days 366 to 1082.

## Data

The project utilizes two primary datasets:
- The US consumption expenditure dataset for tasks involving consumption, income, and production variables.
- The GEFCOM dataset for analyzing electricity prices and loads, focusing on temporal dynamics and relationships between various explanatory variables.

## Results

The project outputs include visualizations of regression parameters and forecasts, alongside metrics that evaluate the performance of the models in predicting electricity prices.
