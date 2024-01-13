# Ice Video Game Sales Analysis

## Project Description
### Overview
This project examines video game sales data to uncover patterns that determine game success in 2017, focusing on data from 2013 to 2016. The analysis seeks to predict trends based on various factors such as platform lifespans, genre popularity, and regional preferences.

### Background
The data, provided by Practicum, includes detailed information on video game sales through 2016. The analysis emphasizes the years following the release of the Xbox One and PS4 in late 2012, aiming to understand the evolving video game market dynamics.

### Data Analysis and Model Building
- Preprocessed data for analysis, including standardizing column names and handling missing values.
- Analyzed sales trends over the years, with a focus on the period post-2013.
- Explored correlations between reviews and sales, particularly for the Xbox One platform.
- Investigated regional differences in game sales, focusing on platform, genre, and ESRB ratings.

### Key Findings
- The peak of game releases was in 2008-2009, with a decline observed in later years.
- PS4 and Xbox One platforms showed increasing sales, predicting a rise in their profitability.
- Shooter, sport, and platformer genres showed high global sales, whereas adventure, strategy, and puzzle genres were less profitable.
- Statistical tests indicated no significant difference in user ratings between Xbox One and PC games.

## Conclusions and Business Implications
- Platforms like PS4 and Xbox One are likely to be profitable in the upcoming years.
- Genres such as action, shooter, and sports are expected to perform well, especially in North America and Europe.
- The PC platform, due to its longevity, remains a significant area of focus despite lower recent sales.

## Media
### Correlation between scores and sales for Xbox One
![Correlation between scores and sales for Xbox One](https://github.com/jnorfolk/Data-Projects-TripleTen/blob/main/Ice%20Video%20Game%20Sales/images/score-sales-correlation.png)

### Global sales per genre
![Global sales per genre](https://github.com/jnorfolk/Data-Projects-TripleTen/blob/main/Ice%20Video%20Game%20Sales/images/sales-per-genre.png)

## Link to Project Notebook
[Link to Notebook](https://github.com/jnorfolk/Data-Projects-TripleTen/blob/main/Ice%20Video%20Game%20Sales/video_game_sales.ipynb)

## Demo Video
Pending

## Installation and Deployment
### System Requirements
- Python 3.9.16
- Jupyter Notebook, and essential libraries (Pandas, NumPy, Matplotlib, Seaborn).

### Installation Instructions
#### 1. Install Python
Download and install Python 3 from [python.org](https://www.python.org/downloads/).

#### 2. Set Up a Virtual Environment (Optional but Recommended)
Create and activate a virtual environment:
- **Create:** `python3 -m venv gamesales_env`
- **Activate:**
  - Windows: `gamesales_env\Scripts\activate`
  - macOS/Linux: `source gamesales_env/bin/activate`

#### 3. Install Required Libraries
`pip install pandas numpy matplotlib seaborn`

#### 4. Run the Jupyter Notebook
Install Jupyter Notebook: `pip install notebook`
Then launch it: `jupyter notebook`
Open the `Video-Game-Sales-Analysis.ipynb` file in the notebook interface.

#### 5. Deactivate the Virtual Environment (After Use)
Type `deactivate`

## Future Enhancements
- Incorporate machine learning models for predictive analytics.
- Extend the data range to include more recent years for updated trend analysis.
- Apply more advanced statistical methods to deepen the analytical insights.

## Credits and Acknowledgments
Special thanks to Practicum for providing the dataset. Datasets are proprietary and cannot be shared online.
