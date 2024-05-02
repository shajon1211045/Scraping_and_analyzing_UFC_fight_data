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

You can access the Tableau Public dashboard https://public.tableau.com/app/profile/zahidul.islam.shajon/viz/UFC_FIGHT_ANALYSIS/Dashboard3

## Findings and Observations from the Dashboard
1. Bigger fighters have more ratio in the top chart for knockouts like Heavyweights, Light Heavyweights and Middleweights.
2. Relatively smaller fighters dominate most submission wins top chart specially fighters in the lightweight divison.
3. The orthodox fighting stance has been the most effective for winning a fight as it has the most winnig counts across different weight classes.
5. Some of the most well known knockout and submission artists (many of them never became world champion) have most wins in the first round and relatively less popular fighters have most losses in the first round except a few popular names like Donald cereone, Frank Mir and Antonio Silva.
6. Almost all the fighters in the winning and losing top chart for fifth round are former and current world champions.
7. Over the years most of the fights won in the first and second round are via knockouts.
8. Third and Fifth round are largely decision wins as we know in the UFC there are only three and five round fights. It appears fighters who make it to final round tend to not get subbed or knocked out.  

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


