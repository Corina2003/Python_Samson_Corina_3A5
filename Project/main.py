import requests
from bs4 import BeautifulSoup
import time
from threading import Thread, Event
from tkinter import messagebox

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

def run_crawler():
    start_url = url_entry.get()
    search_tag = tag_entry.get()

    if not start_url or not search_tag:
        messagebox.showerror("Input Error", "Please provide both a start URL and a tag.")
        return

    if not is_valid_url(start_url):
        messagebox.showerror("Input Error", "Invalid Start URL.")
        return

    stop_event.clear()

    def update_gui(message):
        result_text.insert(tk.END, message)
        result_text.see(tk.END)
        app.update_idletasks()

    def threaded_crawl():
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Crawling pages...\n")
        found_links = scrape_links(start_url, search_tag, stop_event, update_gui)

        if not stop_event.is_set():
            result_text.insert(tk.END, "\nCrawling complete.\n")

        if found_links:
            result_text.insert(tk.END, "\nIdentified Links:\n")
            for index, (link, size) in enumerate(found_links, start=1):
                result_text.insert(tk.END, f"{index}. {link} | Size: {size} MB\n")
        else:
            result_text.insert(tk.END, "No links found or the provided URL is inaccessible.\n")

    Thread(target=threaded_crawl).start()

def stop_crawler():
    stop_event.set()
    result_text.insert(tk.END, "\nCrawling stopped by user.\n")
