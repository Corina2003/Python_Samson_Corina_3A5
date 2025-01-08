import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox, scrolledtext
from threading import Thread, Event
import time

#Scrieti un tool care pornind de la pagina web si un tag primiti ca parametri listeaza traseul
#parcus de tool atunci cand acceseaza toate paginile ce au acel tag.
#Tool-ul va considera un tag valid daca link-ul contine acel tag in interiorul campului <a ...> </a>
#Daca intr-o pagina sunt mai multe pagini ce contin acel tag vor fi accesate toate

#OUTPUT:
#Traseul parcurs de tool: Nume link si dimensiune pagina accesata
#Logul de rulare si erorile aparute


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
            attributes = str(link_tag.attrs)
            current_link = link_tag.get('href')

            if search_tag not in attributes:
                update_gui(f"Skipping link (tag not in <a ...> attributes): {current_link} - Attributes: {attributes}\n")
                continue

            if not current_link.startswith('http'):
                update_gui(f"Skipping invalid link: {current_link}\n")
                continue

            try:
                time.sleep(delay)
                check_response = requests.get(current_link, timeout=5)
                check_response.raise_for_status()

                size_in_mb = round(len(check_response.content) / (1024 * 1024), 3)
                links_collected.add((current_link, size_in_mb))
                update_gui(f"Valid link found: {current_link} | Size: {size_in_mb} MB | Attributes: {attributes}\n")

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

app = tk.Tk()
app.title("Web Crawler Tool")

stop_event = Event()

tk.Label(app, text="Start URL:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
url_entry = tk.Entry(app, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(app, text="Tag:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
tag_entry = tk.Entry(app, width=50)
tag_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Button(app, text="Run Crawler", command=run_crawler).grid(row=2, column=0, padx=5, pady=10)
tk.Button(app, text="Stop Crawler", command=stop_crawler).grid(row=2, column=1, padx=5, pady=10)

result_text = scrolledtext.ScrolledText(app, width=80, height=20)
result_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

app.mainloop()

