import requests
from bs4 import BeautifulSoup
import time

def is_valid_url(url):
    return url.startswith("http://") or url.startswith("https://")

def scrape_links(start_url, search_tag, stop_event, update_gui, delay=1):
    links_collected = set()
    try:
        update_gui(f"Accessing the main page: {start_url}\n")
        response = requests.get(start_url, timeout=5)
        response.raise_for_status()

        parsed_page = BeautifulSoup(response.content, 'html.parser')

        for link_tag in parsed_page.find_all('a', href=True):
            current_link = link_tag.get('href')
            if not current_link.startswith('http'):
                update_gui(f"Skipping invalid link: {current_link}\n")
                continue

            try:
                time.sleep(delay)
                check_response = requests.get(current_link, timeout=5)
                check_response.raise_for_status()

                size_in_mb = round(len(check_response.content) / (1024 * 1024), 3)
                links_collected.add((current_link, size_in_mb))
                update_gui(f"Valid link found: {current_link} | Size: {size_in_mb} MB\n")

            except requests.RequestException as err:
                update_gui(f"Error accessing link: {current_link} - {err}\n")
            except Exception as general_err:
                update_gui(f"Unexpected error for link: {current_link} - {general_err}\n")

    except requests.RequestException as main_err:
        update_gui(f"Error accessing main URL {start_url} - {main_err}\n")
    except Exception as general_main_err:
        update_gui(f"Unexpected error for main URL {start_url} - {general_main_err}\n")

    return links_collected
