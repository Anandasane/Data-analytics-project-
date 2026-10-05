# Data Analysis Projects – freeCodeCamp

This repository contains my solutions to the five projects required for the **Data Analysis with Python** certification from freeCodeCamp. Each project focuses on a different aspect of data analysis: numerical computations with NumPy, data manipulation with Pandas, and data visualization with Matplotlib and Seaborn.

## 📋 Table of Contents

- [Projects Overview](#-projects-overview)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Datasets](#-datasets)
- [How to Run](#-how-to-run)
- [Project Details](#-project-details)
- [Acknowledgements](#-acknowledgements)

## 📊 Projects Overview

| # | Project | Main File | Key Libraries |
|---|---------|-----------|---------------|
| 1 | Mean-Variance-Standard Deviation Calculator | `mean_var_std.py` | NumPy |
| 2 | Demographic Data Analyzer | `demographic_data_analyzer.py` | Pandas |
| 3 | Medical Data Visualizer | `medical_data_visualizer.py` | Pandas, Seaborn, Matplotlib |
| 4 | Page View Time Series Visualizer | `time_series_visualizer.py` | Pandas, Matplotlib, Seaborn |
| 5 | Sea Level Predictor | `sea_level_predictor.py` | Pandas, Matplotlib, SciPy |

## 🛠 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   cd YOUR-REPO-NAME
   ```

2. **Install required packages**
   ```bash
   pip install numpy pandas matplotlib seaborn scipy
   ```

   Or, if a `requirements.txt` is provided:
   ```bash
   pip install -r requirements.txt
   ```

## 📂 Datasets

Each project uses a specific dataset. Download them and place them in the root directory of the repository (or in the respective project folders if you organize them separately).

| Project | Dataset File | Source |
|---------|--------------|--------|
| Demographic Data Analyzer | `adult.data` | [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data) |
| Medical Data Visualizer | `medical_examination.csv` | [Kaggle – Cardiovascular Disease Dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset) (rename `cardio_train.csv` to `medical_examination.csv`) |
| Page View Time Series Visualizer | `fcc-forum-pageviews.csv` | Included in the freeCodeCamp boilerplate; can also be downloaded from [GitHub](https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/master/fcc-forum-pageviews.csv) |
| Sea Level Predictor | `epa-sea-level.csv` | Included in the freeCodeCamp boilerplate; can also be downloaded from [GitHub](https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/master/epa-sea-level.csv) |

> **Note:** The Mean-Variance-Standard Deviation Calculator does not require any external dataset; it takes a list of nine numbers as input.

## 🚀 How to Run

Each project has its own `main.py` file for testing. To run a specific project, navigate to its directory (if organized separately) or stay in the root directory and run the corresponding `main.py`. For example:

```bash
python3 main.py
```

Alternatively, you can run individual project files directly:

```bash
python3 mean_var_std.py
python3 demographic_data_analyzer.py
python3 medical_data_visualizer.py
python3 time_series_visualizer.py
python3 sea_level_predictor.py
```

## 📁 Project Details

### 1. Mean-Variance-Standard Deviation Calculator
- **File:** `mean_var_std.py`
- **Description:** A function `calculate()` that takes a list of 9 numbers, converts it to a 3×3 NumPy array, and returns a dictionary with the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.
- **Key Concepts:** NumPy array reshaping, axis-wise operations, `.tolist()` conversion.

### 2. Demographic Data Analyzer
- **File:** `demographic_data_analyzer.py`
- **Description:** Uses Pandas to answer questions about a 1994 Census dataset, such as race distribution, average age of men, education levels and salary percentages, and more.
- **Key Concepts:** Pandas filtering, `value_counts()`, `groupby()`, boolean indexing, `round()`.

### 3. Medical Data Visualizer
- **File:** `medical_data_visualizer.py`
- **Description:** Visualizes medical examination data using Seaborn and Matplotlib. Creates a categorical plot and a correlation heatmap after cleaning the data.
- **Key Concepts:** `pd.melt()`, `sns.catplot()`, `sns.heatmap()`, correlation matrix, outlier filtering, BMI calculation.

### 4. Page View Time Series Visualizer
- **File:** `time_series_visualizer.py`
- **Description:** Visualizes daily page views on the freeCodeCamp forum from 2016 to 2019 using line, bar, and box plots.
- **Key Concepts:** Time series indexing, resampling, `sns.boxplot()`, `df.plot()`, date formatting, quantile filtering.

### 5. Sea Level Predictor
- **File:** `sea_level_predictor.py`
- **Description:** Analyzes global average sea level change since 1880 and predicts sea level rise through 2050 using linear regression.
- **Key Concepts:** `scipy.stats.linregress`, scatter plots, line of best fit, extrapolation, Matplotlib labels.



---

Feel free to explore each project and reach out if you have any questions!