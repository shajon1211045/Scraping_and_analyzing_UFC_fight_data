# UFC Fight Data Analysis Project

## Project Overview
This project focuses on the analysis of UFC (Ultimate Fighting Championship) fight data to gain insights into various aspects of the sport, such as fighter performance, fight outcomes, and trends over time. The data is collected through web scraping techniques from the official UFC website and then analyzed using Python scripts and Jupyter Notebooks.

## Project Structure
The project structure is organized as follows:

### Data Folder
Contains the following CSV files:
- `fight_data.csv`: Contains data on UFC fight events, including event details, fight results, and match statistics.
- `fighter_stats.csv`: Includes statistics and attributes of UFC fighters, such as height, weight, reach, and fighting style.
- `transformed_data.csv`: A transformed and cleaned version of the raw data, prepared for analysis.

### Scrapers Folder
Contains Python scripts for web scraping UFC data:
- `scrape_fight_data.py`: Script to scrape data on UFC fight events from the official UFC website.
- `scrape_fighter_stats.py`: Script to scrape statistics and attributes of UFC fighters.

### Notebooks Folder
Contains Jupyter Notebooks for data analysis and exploration:
- `Data_transformation_&_EDA.ipynb`: Notebook for data transformation, cleaning, and exploratory data analysis (EDA).

### Requirements.txt
Lists all Python dependencies required to run the scripts and notebooks in the project.

## Getting Started
To replicate the data collection process or run the analysis notebooks, follow these steps:
1. Clone the repository:
`git clone https://github.com/yourusername/ufc-fight-data-analysis.git`
2. Navigate to the project directory:
`cd ufc-fight-data-analysis`
3. Initialize and activate a virtual environment (optional but recommended):
`virtualenv venv   
source venv/bin/activate`
4. Install dependencies:
`pip install -r requirements.txt`

