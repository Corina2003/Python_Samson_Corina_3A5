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

def is_valid_link(link):
    return link.startswith("http://") or link.startswith("https://")

def fetch_links(main_url, keyword, terminate_event, display_log, pause_time=1):
    collected_links = set()
    processed_links = set()
    display_log(f"Opening main page: {main_url}\n")

    try:
        response = requests.get(main_url, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        display_log(f"Failed to open {main_url} - {e}\n")
        return collected_links

    parsed_content = BeautifulSoup(response.content, 'html.parser')
    link_elements = parsed_content.find_all('a', href=True)

    for element in link_elements:
        link = element.get('href')
        attributes = str(element.attrs)

        if keyword not in attributes or link in processed_links:
            display_log(f"Ignoring link: {link}\n")
            continue

        if not is_valid_link(link):
            display_log(f"Invalid link skipped: {link}\n")
            continue

        processed_links.add(link)

        try:
            time.sleep(pause_time)
            link_response = requests.get(link, timeout=5)
            link_response.raise_for_status()
            page_size = round(len(link_response.content) / (1024 * 1024), 3)
            collected_links.add((link, page_size))
            display_log(f"Collected: {link} | Size: {page_size} MB\n")
        except requests.RequestException as error:
            display_log(f"Error accessing {link}: {error}\n")
        except Exception as unexpected_error:
            display_log(f"Unexpected error for {link}: {unexpected_error}\n")

    return collected_links

def initiate_crawler():
    main_url = url_input.get()
    keyword = tag_input.get()

    if not main_url or not keyword:
        messagebox.showerror("Input Error", "Please provide both a start URL and a tag.")
        return

    if not is_valid_link(main_url):
        messagebox.showerror("Input Error", "Invalid Start URL.")
        return

    terminate_event.clear()

    def display_log(message):
        output_text.insert(tk.END, message)
        output_text.see(tk.END)
        app.update_idletasks()

    def threaded_scan():
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Scanning pages...\n")
        found_links = fetch_links(main_url, keyword, terminate_event, display_log)

        if not terminate_event.is_set():
            output_text.insert(tk.END, "\nScanning completed.\n")

        if found_links:
            output_text.insert(tk.END, "\nIdentified Links:\n")
            for index, (link, size) in enumerate(found_links, start=1):
                output_text.insert(tk.END, f"{index}. {link} | Size: {size} MB\n")
        else:
            output_text.insert(tk.END, "No matching links found or URL is inaccessible.\n")

    Thread(target=threaded_scan).start()

def halt_crawler():
    terminate_event.set()
    output_text.insert(tk.END, "\nScanning stopped by user.\n")

app = tk.Tk()
app.title("Web Scanner Tool")

terminate_event = Event()

tk.Label(app, text="Start URL:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
url_input = tk.Entry(app, width=50)
url_input.grid(row=0, column=1, padx=5, pady=5)

tk.Label(app, text="Tag:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
tag_input = tk.Entry(app, width=50)
tag_input.grid(row=1, column=1, padx=5, pady=5)

tk.Button(app, text="Start Scan", command=initiate_crawler).grid(row=2, column=0, padx=5, pady=10)
tk.Button(app, text="Stop Scan", command=halt_crawler).grid(row=2, column=1, padx=5, pady=10)

output_text = scrolledtext.ScrolledText(app, width=80, height=20)
output_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

app.mainloop()
