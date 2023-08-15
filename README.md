# Project Proposal: Building a Quantitative Trading Strategy for REITs
### Jonathan Ling and Cameron Keith

## 1. Overview
Real Estate Investment Trusts (REITs) offer attractive investment opportunities in the commercial real estate market. This project aims to develop a quantitative trading strategy that leverages machine learning, sentiment analysis, and time series analysis to identify undervalued REITs within specific sectors and sub-sectors. The strategy will use market data from FactSet, sentiment analysis on REITs, and historical price data to make informed investment decisions. The goal is to achieve superior risk-adjusted returns and outperform benchmark indices by combining domain expertise, sentiment analysis, time series analysis, and portfolio optimization techniques.
## 2. Objectives
Develop a machine learning model for sentiment analysis on REITs to gauge positive and negative market sentiment.
Apply time series analysis to historical price data for REITs to identify patterns and trends.
Identify undervalued REITs based on sentiment analysis, time series analysis, market data, and other relevant factors.
Build a diversified REIT portfolio that optimizes returns while managing risk effectively.
Compare the performance of the strategy against benchmark indices and standard buy-and-hold approaches.
Dependent variable: predict continuous stock price of REITs in 6 months
Predicted sales price includes sentiment score
Then find top 40 REIT differentials and output portfolio
## 3. Methodology
Jonathan and Cameron
Data Collection: Gather historical market data for REITs from FactSet, including price, volume, financial ratios, and other relevant metrics. Obtain textual data for sentiment analysis from financial news sources and social media. 
Data dictionary: FactSet Real Estate Industry REIT
Cameron
Sentiment Analysis: Utilize NLP models like BERT or GPT to run sentiment analysis on the textual data to extract sentiment scores for each REIT.
Jonathan
Time Series Analysis: Apply time series analysis techniques such as ARIMA, LSTM, or bidirectional GRU on historical price data to identify patterns and trends.
Cameron
Feature Engineering: Engineer additional features such as sector-specific metrics, historical performance, and risk measures.
Jonathan and Cameron
Machine Learning Model: Train a machine learning model, potentially including bi-directional GRU, to predict undervalued REITs based on sentiment scores, time series analysis, market data, and other features. (may be too computationally expensive depending on the size of our dataset -> could resort to simple or hybrid design: use linear regression to extrapolate the trend, transform the target to remove the trend, and apply XGBoost to the detrended residuals.)
Evaluation: RMSE between actual and predicted price
Portfolio Optimization: Apply portfolio optimization techniques, such as Mean-Variance Optimization, to construct a diversified portfolio of REITs.
Backtesting and Evaluation: Backtest the trading strategy using historical data to assess its performance and risk characteristics.
Real-time Implementation: Develop a real-time monitoring system to evaluate the strategy's performance during current market conditions.
## 4. Deliverables
Sentiment analysis model for REITs.
Time series analysis of historical price data for REITs.
Machine learning model for identifying undervalued REITs.
Optimized portfolio of selected REITs.
Backtesting results and performance evaluation.
Real-time monitoring system for ongoing performance assessment.
## 5. Timeline
Data Collection and Preprocessing: 1 week
Sentiment Analysis Model and Time Series Analysis: 1 week
Machine Learning Model and Portfolio Optimization: 1 week
Backtesting and Evaluation plus Real-time Implementation: 1 week
Documentation and Final Report: 1 week
## 6. Conclusion
This project aims to develop a comprehensive quantitative trading strategy that leverages sentiment analysis, time series analysis, and machine learning to identify undervalued REITs within specific market sectors. By combining domain expertise, sentiment analysis, time series analysis, and portfolio optimization techniques, the strategy seeks to outperform benchmark indices and traditional buy-and-hold approaches in the commercial real estate market. The real-time monitoring system will ensure continuous evaluation and refinement of the strategy for optimal performance.
