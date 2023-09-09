import threading
import tkinter as tk
import tkinter.scrolledtext as st
import tkinter.filedialog as fd
import requests

class DirectoryScanner:
    def __init__(self, url, wordlist, threads):
        self.url = url
        self.wordlist = wordlist
        self.threads = threads
        self.found_directories = []
        self.running_threads = []
    
    def start_scan(self):
        with open(self.wordlist, "r") as f:
            wordlist = f.read().splitlines()
        for word in wordlist:
            t = threading.Thread(target=self.scan_directory, args=(word,))
            self.running_threads.append(t)
            t.start()
            if len(self.running_threads) >= self.threads:
                for thread in self.running_threads:
                    thread.join()
                self.running_threads = []
        for thread in self.running_threads:
            thread.join()
        return self.found_directories
    
    def scan_directory(self, word):
        url = self.url + "/" + word
        response = requests.get(url)
        if response.status_code == 200:
            self.found_directories.append(url)

class Application:
    def __init__(self, master):
        self.master = master
        master.title("Directory Scanner")

        self.url_label = tk.Label(master, text="URL:", font=("Arial", 12))
        self.url_label.grid(row=0, column=0, pady=10)
        self.url_entry = tk.Entry(master, font=("Arial", 12))
        self.url_entry.grid(row=0, column=1, columnspan=2, pady=10)

        self.wordlist_label = tk.Label(master, text="Wordlist:", font=("Arial", 12))
        self.wordlist_label.grid(row=1, column=0, pady=10)
        self.wordlist_entry = tk.Entry(master, font=("Arial", 12))
        self.wordlist_entry.grid(row=1, column=1, pady=10)
        self.browse_button = tk.Button(master, text="Browse", font=("Arial", 12), command=self.select_wordlist)
        self.browse_button.grid(row=1, column=2, pady=10)

        self.threads_label = tk.Label(master, text="Threads:", font=("Arial", 12))
        self.threads_label.grid(row=2, column=0, pady=10)
        self.threads_entry = tk.Entry(master, font=("Arial", 12))
        self.threads_entry.grid(row=2, column=1, pady=10)

        self.scan_button = tk.Button(master, text="Scan", font=("Arial", 12), command=self.start_scan)
        self.scan_button.grid(row=3, column=0, columnspan=3, pady=10)

        self.results_label = tk.Label(master, text="Results:", font=("Arial", 12))
        self.results_label.grid(row=4, column=0, pady=10)
        self.results_text = st.ScrolledText(master, font=("Arial", 12), width=50, height=20, state='disabled')
        self.results_text.grid(row=4, column=1, columnspan=2, pady=10)

    def select_wordlist(self):
        filetypes = (("Text files", "*.txt"), ("All files", "*.*"))
        filename = fd.askopenfilename(title="Select wordlist file", filetypes=filetypes)
        if filename:
            self.wordlist_entry.delete(0, tk.END)
            self.wordlist_entry.insert(0, filename)

    def start_scan(self):
        url = self.url_entry.get()
        wordlist = self.wordlist_entry.get()
        threads = int(self.threads_entry.get())

        self.results_text.configure(state='normal')
        self.results_text.delete('1.0', 'end')
        self.results_text.configure(state='disabled')

        scanner = DirectoryScanner(url, wordlist, threads)
        results = scanner.start_scan()

        self.results_text.configure(state='normal')
        if results:
            self.results_text.insert('end', "\n".join(results))
        else:
            self.results_text.insert('end', "No directories found.")
        self.results_text.configure(state='disabled')

root = tk.Tk()
app = Application(root)
root.mainloop()

