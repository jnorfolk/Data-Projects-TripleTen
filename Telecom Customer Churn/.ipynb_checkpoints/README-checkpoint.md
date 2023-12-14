# Interconnect Telecom Churn Prediction

## Link to Project Notebook
[Notebook](https://github.com/jnorfolk/Telecom-Churn/blob/main/Telecom-Churn-Final.ipynb)

## Project Description
### Overview
This project aims to forecast client churn for the telecom operator Interconnect. Utilizing client data, the goal is to identify potential churners early to offer them special deals and promotions, thereby reducing churn rates.

### Background
Interconnect provides various telecom services, including landline communication and internet through DSL or fiber optic cables. Additional services include internet security, technical support, cloud storage, TV streaming, and movie directories. Clients have the option to choose monthly payments or 1- or 2-year contracts, with various payment methods and electronic invoicing.

## Methodology
### Data Analysis and Model Building
- Analyzed personal and plan-related data of Interconnect's clientele.
- Constructed a predictive model focusing on factors like tenure, contract type, and internet service type.

### Key Findings
- The final model achieved an AUC-ROC score of 0.90, indicating high accuracy in predicting user churn.
- Identified key churn indicators: tenure less than 1000 days, month-to-month contracts, and fiber optic internet service users.

### Feature Importances
![image](https://github.com/jnorfolk/Telecom-Churn/assets/117448822/86ff7e44-9a16-435e-8410-5fdfcdb77715)

## Conclusions and Business Implications
- Effective prediction of potential churn allows for targeted promotional strategies.
- Recommendations include focusing retention efforts on users within the identified high-risk categories.

## Installation and Deployment
### System Requirements
- Python 3.x, Jupyter Notebook, and essential libraries (Pandas, NumPy, Scikit-learn, Matplotlib).

### Installation Instructions
#### 1. Install Python
Download and install Python 3 from [python.org](https://www.python.org/downloads/).

#### 2. Set Up a Virtual Environment (Optional but Recommended)
Create and activate a virtual environment:
- **Create:** `python3 -m venv interconnect_env`
- **Activate:**
  - Windows: `interconnect_env\Scripts\activate`
  - macOS/Linux: `source interconnect_env/bin/activate`

#### 3. Install Required Libraries
```
pip install pandas numpy scikit-learn matplotlib
```

#### 4. Run the Jupyter Notebook
Install Jupyter Notebook: `pip install notebook`
Then launch it: `jupyter notebook`
Open the `Telecom-Churn-Final.ipynb` file in the notebook interface.

#### 5. Deactivate the Virtual Environment (After Use)
Type `deactivate`

## Future Enhancements
- Explore more complex models and feature engineering techniques to further improve the prediction accuracy.
- Investigate the impact of other client services and features on churn rates.

## Credits and Acknowledgments
Data provided by TripleTen.
