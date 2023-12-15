# Zyfra Gold Concentrate Recovery Prediction

## Project Description
### Project Overview
This project aims to optimize gold production for Zyfra by predicting the yield of gold concentrate from gold ore. Utilizing data from various stages of the gold extraction process, the goal is to train a regression model for accurate gold recovery prediction.

### Data Description
- **Complete Dataset:** Contains observations and all features/targets, including those calculated post-extraction.
- **Training Set:** A subset of the complete dataset for training the model.
- **Test Set:** Features available at the start of the extraction process, used for making predictions.

### Methodology
#### Data Preprocessing
- Verified accuracy of recovery calculations.
- Analyzed and compared metal concentrations at different stages.
- Evaluated feed size distributions in training and test sets.
- Handled missing values and selected relevant targets.

#### Model Training and Evaluation
- Experimented with linear regression and random forest regression models.
- The primary metric for success was symmetric mean absolute error (sMAPE).
- Calculated sMAPE for both rougher and final concentrate recovery, finding a weighted average for the final score.

### Key Findings
- The random forest regression model demonstrated a sMAPE of 4.95% in cross-validation.
- Final testing on the test set yielded a 7.53% sMAPE.
- The model's performance was benchmarked against a dummy model created from the fully processed dataset, showing comparable or better performance.

### Business Implications and Recommendations
- **Optimized Production Planning:** Utilize model predictions to plan gold extraction more efficiently, ensuring maximal recovery of gold concentrate.
- **Cost Reduction:** Identify stages with lower recovery rates for targeted process improvements, reducing operational costs.
- **Strategic Decision Making:** Leverage predictive insights for strategic decisions in procurement and resource allocation based on expected yield.

## Media
### Concentrations of Gold across Stages
![image](https://github.com/jnorfolk/Zyfra-Gold-Recovery/assets/117448822/75c6a6d2-2dc6-4275-aadf-ea22e67c4852)

## Link to Notebook
[Notebook](https://github.com/jnorfolk/Zyfra-Gold-Recovery/blob/main/Zyfra-Gold-Recovery.ipynb)

## Demo Video
Pending

## Installation and Deployment

### Prerequisites
- Python 3.9.16
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

5. Deactivate the Virtual Environment (After Use)
Type `deactivate`

### Ideas for Project Improvement
- **Advanced Analytical Techniques:** Explore more complex machine learning algorithms or ensemble methods to further refine prediction accuracy.
- **Real-time Data Integration:** Develop a system for incorporating real-time extraction data to make the model adaptive to current operational conditions.
- **Process Optimization:** Use model insights to identify and address inefficiencies in the extraction process.

## Acknowledgments
- This project was a part of a collaborative effort with my program TripleTen and Zyfra, providing real-world data and context for effective model development; however, these proprietary datasets cannot be shared online.
