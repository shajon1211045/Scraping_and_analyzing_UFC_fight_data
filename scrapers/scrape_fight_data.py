from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import csv

def navigate_to_event_pages():
    driver = webdriver.Chrome()
    try:
        driver.get("http://ufcstats.com/statistics/events/completed?page=all")
        # Wait for the presence of all event rows
        event_rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".b-statistics__table-row"))
        )
        # Slice the event rows to exclude the first two rows
        event_rows = event_rows[2:]
        # Extract event links
        event_links = [event_row.find_element(By.CSS_SELECTOR, "a").get_attribute("href") for event_row in event_rows]
        # Print the number of events
        print("Number of Events:", len(event_links))
        # Navigate to each event link
        for event_link in event_links:
            print("Navigating to:", event_link)
            driver.get(event_link)
            # Wait for the table body to be present
            table_body = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "b-fight-details__table-body"))
            )
            # Scrape fight data
            event_info = scrape_event_info(driver)
            scrape_fight_data(table_body, event_info)
    finally:
        driver.quit()

def scrape_event_info(driver):
    event_name = driver.find_element(By.CSS_SELECTOR, ".b-content__title-highlight").text
    event_date = driver.find_element(By.CSS_SELECTOR, ".b-list__box-list-item").text
    location = driver.find_element(By.CSS_SELECTOR, ".b-list__box-list-item:nth-child(2)").text
    return {'Event Name': event_name, 'Date': event_date, 'Location': location}

def scrape_fight_data(table_body, event_info):
    fights = table_body.find_elements(By.CLASS_NAME, "b-fight-details__table-row")
    for fight in fights:
        data = {}
        columns = fight.find_elements(By.CLASS_NAME, "b-fight-details__table-col")
        
        # Extracting data from each fight row
        data['Win/Loss'] = columns[0].text.replace("\n", ", ")
        data['Fighters'] = columns[1].text.replace("\n", ", ")
        data['KD'] = columns[2].text.replace("\n", ", ")
        data['Str'] = columns[3].text.replace("\n", ", ")
        data['Td'] = columns[4].text.replace("\n", ", ")
        data['Sub'] = columns[5].text.replace("\n", ", ")
        data['Weight Class'] = columns[6].text.split()[0]
        data['Method'] = columns[7].text.replace("\n", ", ")
        data['Round'] = columns[8].text
        data['Time'] = columns[9].text
        
        # Adding event info
        data.update(event_info)
        
        # Storing data in CSV
        with open('fight_data.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)

if __name__ == "__main__":
    navigate_to_event_pages()
