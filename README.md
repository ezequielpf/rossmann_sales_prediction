# Rossmann Sales Prediction

## Situation
Rossmann, a large pharmacy chain in Europe, needed to forecast store sales for the next six weeks to support budgeting and renovation decisions. Existing forecasts were manual, based on managers' intuition, and lacked accuracy and centralization, making strategic planning difficult.

## Task
Build a predictive model to estimate daily sales for each Rossmann store using historical data and store attributes, and compare different forecasting approaches (time series models and tree-based models).

## Action
- Merged sales data (train.csv) with store attributes (store.csv) to enrich the dataset.
- Created temporal and categorical features to capture sales patterns.
- Extensive EDA to identify seasonality, weekday effects and promo/competition signals.
- Feature engineering: temporal features, categorical encodings, competition/promo-derived features, and per-store lags & rolling statistics (7/14/28-day lags and moving averages).
- Implemented tree-based models (XGBoost), using cross-validation, feature selection, and hyperparameter tuning.
- Compared model performance with simple benchmarks (moving average, naive forecast).
- Evaluated results using metrics such as RMSPE, RMSE, and MAPE, both globally and per store.

## Result
- The global XGBoost model, using enriched data, outperformed time series models and simple benchmarks.
- The XGBoost model achieved a lower RMSPE (0.1424) than Naive Forecast (0.3018) and Moving Average (0.4004) methods, showing significant accuracy gains.
- The gain is 64.42% over the Moving Average and 52.79% over the Naive Forecast.

### Financial Impact (Hypothetical Example)

To illustrate the potential business gains of a more accurate model, consider the following scenario (hypothetical values, in euros):  

- **Number of stores:** 1,000  
- **Average daily sales per store:** €3,000  
- **Forecast horizon:** 42 days (6 weeks)  
- **Total revenue in the period:** €126,000,000  

#### Error Comparison (RMSPE)

| Model            | RMSPE (%) | Estimated Monetary Error (€) |
|------------------|-----------|-------------------------------|
| Moving Average   | 40.04%    | €50,450,400                   |
| Naive Forecast   | 30.18%    | €38,026,800                   |
| **XGBoost**      | **14.24%**| **€17,942,400**               |

#### XGBoost Gain

- **vs Moving Average:** €32,508,000 error reduction  
- **vs Naive Forecast:** €20,084,400 error reduction  
