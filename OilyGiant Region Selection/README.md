# OilyGiant Well Location Optimization

## Project Description
### Project Overview
The objective of this project was to determine the most profitable region for drilling 200 new oil wells from a choice of three regions. The selection criteria were based on maximizing profit margins, considering oil quality and volume, while keeping the risk of loss below 2.5%.

### Data Preprocessing and Model Training
- **Data Verification:** Ensured the data's suitability for model training.
- **Model Development:** Trained and validated linear regression models for each region, focusing on root mean squared error (RMSE) and R² score as evaluation metrics.

### Analysis and Decision Process
- **Oil Profitability Calculation:** Determined the necessary oil volume for profitability and estimated potential yield from the top 200 wells.
- **Profit Calculation:** Selected the largest 200 oil wells in each region and calculated the actual profits.
- **Risk Assessment:** Applied bootstrapping to evaluate loss risks and establish confidence intervals.

### Key Findings and Conclusions
- **Region Performance:**
  - **Region 1:** Exhibited the lowest risk of loss (1.2%) and the highest average profit (4.8 million USD). Best RMSE and R² scores, suggesting high model reliability, despite lower predicted reserve volume.
  - **Region 2:** Had the largest predicted volume but the worst RMSE and R² scores.
  - **Region 0:** Showed moderate predicted reserve volume and better RMSE and R² scores than Region 2.
- **Profitability Analysis:** All regions potentially profitable with the top 200 sites, but actual availability of these sites poses a risk.
- **Risk Management:** The high R² score for Region 1 indicates lower prediction risk, influencing the final decision despite preliminary profit considerations.

### Conclusions and Business ImplicationsS
Region 1 was selected as the optimal location for new oil wells, balancing between profitability and risk. The choice was driven by its lowest risk profile and acceptable profit margins, demonstrating the importance of accurate prediction and risk management in resource-intensive industries.

## Media
### Bootstrapping Results for Top Region
![bootstrapping_result](https://github.com/jnorfolk/Data-Projects-TripleTen/assets/117448822/776d2193-3b06-4ea4-a72f-84f1d27d7ab0)

## Project Notebook
[OilyGiant Project Notebook](https://github.com/jnorfolk/OilyGiant-Region-Selection/blob/main/OilyGiant.ipynb)

## Demo Video
Pending

## Installation and Deployment
### System Requirements
Python 3.9.16, Jupyter Notebook, and essential libraries (Pandas, NumPy, Scikit-learn).

### Installation Instructions
#### 1. Install Python
Download and install Python 3 from [python.org](https://www.python.org/downloads/).

#### 2. Set Up a Virtual Environment (Optional but Recommended)
Using a virtual environment keeps project dependencies separate. Create and activate it:
- **Create:** `python3 -m venv oilygiant_env`
- **Activate:**
  - Windows: `oilygiant_env\Scripts\activate`
  - macOS/Linux: `source oilygiant_env/bin/activate`

#### 3. Install Required Libraries
Install Pandas, NumPy, and Scikit-learn using pip:
```
pip install pandas numpy scikit-learn
```

#### 4. Run the Jupyter Notebook
Install Jupyter Notebook (if not installed): 
`pip install notebook`
Launch it: 
`jupyter notebook`
Navigate to and open the OilyGiant.ipynb file in the notebook interface.

#### 5. Deactivate the Virtual Environment (After Use)
Run `deactivate` to exit the virtual environment.

## Future Recommendations
- **Enhanced Modeling:** Explore more advanced or ensemble machine learning models to refine predictions.
- **Risk Optimization:** Develop strategies to further minimize risks in other promising regions.
- **Data Expansion:** Consider additional data points or features that could improve prediction accuracy and profitability assessment.

## Credits and Acknowledgments
Thanks to TripleTen for providing these datasets. I am unable to publish these proprietary datasets to the internet.
