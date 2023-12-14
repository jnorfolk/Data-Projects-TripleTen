# OilyGiant Well Location Optimization

## Project Description
### Overview
This project focuses on identifying the optimal locations for new oil wells for OilyGiant mining company, using data-driven techniques to maximize profit and minimize risks.

### Features and Functionality
- **Data Collection:** Analysis of oil well parameters (quality and volume of reserves) across three regions.
- **Predictive Modeling:** Developed a linear regression model to predict reserve volumes in new wells.
- **Optimization:** Selection of the most profitable oil wells and regions based on model predictions.
- **Risk Analysis:** Employed Bootstrapping to assess potential profit and risks.
- **Motivation:** To enhance the efficiency of resource allocation in oil mining, leading to increased profitability and informed decision-making.
- **Technologies Used:** Data analysis and modeling were performed using Python, with libraries like Pandas, NumPy, and Scikit-learn.

## Visuals
![image](https://github.com/jnorfolk/OilyGiant-Region-Selection/assets/117448822/f246b58d-0d4b-4d51-82d6-527c330d0e03)


## Project Notebook
[OilyGiant Project Notebook](https://github.com/jnorfolk/OilyGiant-Region-Selection/blob/main/OilyGiant.ipynb): Access the detailed Jupyter notebook for an in-depth look at the data analysis and modeling process.

## Installation and Deployment
### System Requirements
Python 3.x, Jupyter Notebook, and essential libraries (Pandas, NumPy, Scikit-learn).

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
5. Deactivate the Virtual Environment (After Use)
Run `deactivate` to exit the virtual environment.

## Future Enhancements
- Enhance the predictive model by exploring more complex algorithms while considering the project's constraints.
- Implement more sophisticated risk assessment techniques to further minimize potential losses.

## Additional Documentation
Detailed explanation of each step in the notebook, including data preparation, model training, and validation.

## Credits and Acknowledgments
Thanks to TripleTen for providing these three datasets.
