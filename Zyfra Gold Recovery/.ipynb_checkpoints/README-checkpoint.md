# Zyfra Gold Concentrate Recovery Prediction

## Link to Notebook
[Notebook](https://github.com/jnorfolk/Zyfra-Gold-Recovery/blob/main/Zyfra-Gold-Recovery.ipynb)

## Project Overview
This project aims to optimize gold production for Zyfra by predicting the yield of gold concentrate from gold ore. Utilizing data from various stages of the gold extraction process, the goal is to train a regression model for accurate gold recovery prediction.

## Data Description
- **Complete Dataset:** Contains observations and all features/targets, including those calculated post-extraction.
- **Training Set:** A subset of the complete dataset for training the model.
- **Test Set:** Features available at the start of the extraction process, used for making predictions.

## Methodology
### Data Preprocessing
- Verified accuracy of recovery calculations.
- Analyzed and compared metal concentrations at different stages.
- Evaluated feed size distributions in training and test sets.
- Handled missing values and selected relevant targets.

### Concentrations of Gold across Stages
![image](https://github.com/jnorfolk/Zyfra-Gold-Recovery/assets/117448822/75c6a6d2-2dc6-4275-aadf-ea22e67c4852)


### Model Training and Evaluation
- Experimented with linear regression and random forest regression models.
- The primary metric for success was symmetric mean absolute error (sMAPE).
- Calculated sMAPE for both rougher and final concentrate recovery, finding a weighted average for the final score.

## Key Findings
- The random forest regression model demonstrated a sMAPE of 4.95% in cross-validation.
- Final testing on the test set yielded a 7.53% sMAPE.
- The model's performance was benchmarked against a dummy model created from the fully processed dataset, showing comparable or better performance.

## Conclusions and Business Implications
- The developed model successfully predicts gold concentrate recovery at different stages, aiding in optimizing the gold production process.
- The random forest model's consistent low error in cross-validation suggests its potential in real-world application.

## Installation and Deployment

### Prerequisites
- Python 3.x
- Jupyter Notebook or JupyterLab

### Setting Up Your Environment
1. **Install Python:** Download and install from [python.org](https://www.python.org/downloads/).

2. **Create a Virtual Environment (Recommended):**
   - Create: `python -m venv zyfra_env`
   - Activate:
     - Windows: `zyfra_env\Scripts\activate`
     - macOS/Linux: `source zyfra_env/bin/activate`

3. **Install Required Libraries:**
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn

4. **Run the Jupyter Notebook**
Install Jupyter Notebook: `pip install notebook`
Then launch it: `jupyter notebook`
Open the `Zyfra-Gold-Recovery.ipynb` file in the notebook interface.

#### 5. Deactivate the Virtual Environment (After Use)
Type `deactivate`

## Acknowledgments
- This project was a part of a collaborative effort with my program TripleTen and Zyfra, providing real-world data and context for effective model development.
