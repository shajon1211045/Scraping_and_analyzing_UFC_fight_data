# UFC Fight Data Analysis Project

## Project Overview
This project focuses on analyzing UFC (Ultimate Fighting Championship) fight data scraped from [UFC Stats](http://www.ufcstats.com/statistics/events/completed?page=all). The goal is to gain insights into various aspects of UFC fights, including fighter performance, fight outcomes, and trends over time. The analysis is conducted using Python scripts for data scraping and Jupyter Notebooks for exploratory data analysis (EDA). Additionally, a Tableau Public dashboard is created to visualize the findings.

## Dashboard Overview
The Tableau Public dashboard showcases the following analyses:
1. Top knockout artists across different weight classes
2. Top submission artists across different weight classes
3. Distribution of win counts across different weight classes
4. Win counts by different fighting stances across different weight classes
5. Fighters with the most losses across different rounds
6. Fighters with the most wins across different rounds
7. Number of wins by different fighting methods over the years across different rounds

You can access the Tableau Public dashboard [here](#) (link to be updated).

## Findings and Observations from the Dashboard
1. Brazilian fighters dominate the top knockout artists list across various weight classes.
2. Submission artists from different weight classes show a diverse distribution, with certain weight classes having more prominent submission specialists.
3. The win counts are distributed unevenly across different weight classes, indicating varying levels of competition and dominance.
4. Certain fighting stances seem to be more effective in specific weight classes, with orthodox and southpaw stances being the most common.
5. Fighters with the most losses across different rounds tend to have longer fighting careers and higher experience levels.
6. Fighters with the most wins across different rounds often demonstrate consistent performance and adaptability.
7. The popularity and effectiveness of different fighting methods have evolved over the years, with trends reflecting changes in rules, regulations, and fighter strategies.

## How to Replicate the Project
To replicate the data scraping and analysis process, follow these steps:
1. Clone the repository:
git clone https://github.com/yourusername/ufc-fight-data-analysis.git
2. Navigate to the project directory:
cd ufc-fight-data-analysis
3. Initialize and activate a virtual environment (optional but recommended):
virtualenv venv
source venv/bin/activate
4. Install dependencies:
pip install -r requirements.txt
5. Run the Python scripts in the `scrapers` folder to scrape UFC fight data.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


