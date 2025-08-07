# Train Passenger Flow Analysis

## Overview

This project, conducted under the Ethiopian Space Science & Geospatial Institute, focuses on the Exploratory Data Analysis (EDA) of train passenger flow across the East-West (EW) and North-South (NS) lines. The analysis includes data cleaning, sensor comparison, data visualization, trend analysis, feature engineering, and clustering to gain insights into passenger flow patterns.

## Project Structure

The project repository is organized as follows:

-   `data/`: Contains both raw and processed datasets.
    -   `raw/`: Stores the original, unprocessed data.
    -   `processed/`: Stores the cleaned and transformed data, ready for analysis.
-   `notebooks/`: Includes Jupyter notebooks detailing the analysis steps.
    -   `compare_EW.ipynb`: Notebook for comparing EW line data.
    -   `compare_NS.ipynb`: Notebook for comparing NS line data.
    -   `EW-time table downward.ipynb`: Notebook for analyzing EW line downward direction data.
    -   `EW-time table.ipynb`: Notebook for analyzing EW line data.
    -   `NS-time table downward.ipynb`: Notebook for analyzing NS line downward direction data.
    -   `NS-time table.ipynb`: Notebook for analyzing NS line data.
    -   `1_EW_Line_Analysis.ipynb`: Detailed EDA for the East-West line.
    -   `2_NS_Line_Analysis.ipynb.ipynb`: Detailed EDA for the North-South line.
    -   `EW-vs-NS-Passenger-Flow-Comparision.ipynb`: Comparative analysis between EW and NS lines.
-   `scripts/`: Contains Python scripts used for data processing and analysis.
    -   `passenger_flow_utils.py`: Utility functions for data handling, flow analysis, clustering, and plotting.
    -   `plot_utils.py`: Utility functions for data visualization.
    -   `time_analysisss.py`: Script for time series analysis.
    -   `__init__.py`: Makes the directory a Python package.
-   `README.md`: Provides an overview of the project.
-   `LICENSE`: Contains the project's license information.
-   `.gitignore`: Specifies intentionally untracked files that Git should ignore.

## Data Processing and Analysis Steps

The analysis is performed in several key steps, each documented in the respective Jupyter notebooks:

1.  **Data Loading**: Raw data is loaded using the `load_data` function from the `time_analysisss` module ([`time_analysisss.load_data`](scripts/time_analysisss.py)).
2.  **Basic Checks**: Initial data quality checks are performed using the `basic_checks` function from the `passenger_flow_utils` module ([`passenger_flow_utils.basic_checks`](scripts/passenger_flow_utils.py)).
3.  **Handling Missing Values**: Columns with a high percentage of missing values are dropped using the `drop_high_nan_columns` function from the `time_analysisss` module ([`time_analysisss.drop_high_nan_columns`](scripts/time_analysisss.py)).
4.  **Column Renaming**: Columns are renamed for better readability.
5.  **Data Reshaping**: The data is reshaped from a wide to a long format using the `melt_and_pivot_train_schedule` function from the `time_analysisss` module ([`time_analysisss.melt_and_pivot_train_schedule`](scripts/time_analysisss.py)).
6.  **Missing Time Imputation**: Missing arrival and departure times are filled using station averages with the `fill_missing_times_with_station_avg` function from the `time_analysisss` module ([`time_analysisss.fill_missing_times_with_station_avg`](scripts/time_analysisss.py)).
7.  **Dwell Time Calculation**: Dwell time is calculated using the `calculate_dwell_time` function from the `time_analysisss` module ([`time_analysisss.calculate_dwell_time`](scripts/time_analysisss.py)).
8.  **Station Arrival Gap Statistics**: Arrival gap statistics are computed using the `compute_station_gap_stats` function from the `time_analysisss` module ([`time_analysisss.compute_station_gap_stats`](scripts/time_analysisss.py)).
9.  **Outlier Handling**: Outliers are identified and handled.
10. **Data Visualization**: Key statistics and data distributions are visualized using functions from the `plot_utils` module ([`plot_utils`](scripts/plot_utils.py)).

## Libraries Used

-   `pandas`: For data manipulation and analysis.
-   `matplotlib`: For creating visualizations.

## License

This project is licensed under the MIT License - see the LICENSE file for details.