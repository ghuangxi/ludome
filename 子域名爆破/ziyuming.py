import requests
import dns.resolver
import tkinter as tk
from tkinter import filedialog, messagebox

# 枚举子域名
def enumerate_subdomains():
    try:
        # 获取用户输入的域名
        domain = domain_entry.get()
        # 获取字典文件路径
        wordlist_path = wordlist_entry.get()
        # 读取字典文件
        with open(wordlist_path, 'r') as f:
            subdomains = f.readlines()
        # 枚举子域名
        results = []
        for subdomain in subdomains:
            subdomain = subdomain.strip()
            if subdomain:
                hostname = subdomain + '.' + domain
                try:
                    answers = dns.resolver.query(hostname, 'A')
                    for rdata in answers:
                        ip_address = str(rdata)
                        results.append((hostname, ip_address))
                except Exception:
                    pass
        # 输出结果到 GUI 界面
        result_text.delete(1.0, tk.END)
        if results:
            subdomain_list = list(set([result[0] for result in results]))
            for subdomain in subdomain_list:
                result_text.insert(tk.END, f"{subdomain}\n")
        else:
            result_text.insert(tk.END, "No subdomains found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# 选择字典文件
def select_wordlist():
    wordlist_path = filedialog.askopenfilename(title="Select Wordlist File")
    if wordlist_path:
        wordlist_entry.delete(0, tk.END)
        wordlist_entry.insert(0, wordlist_path)

# 创建 GUI 界面
window = tk.Tk()
window.title("Subdomain Enumeration")
window.geometry('600x400')

# 创建输入框和按钮
domain_label = tk.Label(window, text="Domain:")
domain_label.pack(pady=10)
domain_entry = tk.Entry(window, width=50)
domain_entry.pack(pady=10)
wordlist_frame = tk.Frame(window)
wordlist_frame.pack(pady=10)
wordlist_label = tk.Label(wordlist_frame, text="Wordlist File Path:")
wordlist_label.pack(side=tk.LEFT)
wordlist_entry = tk.Entry(wordlist_frame, width=50)
wordlist_entry.pack(side=tk.LEFT, padx=10)
wordlist_button = tk.Button(wordlist_frame, text="Select", command=select_wordlist)
wordlist_button.pack(side=tk.LEFT)
enumerate_button = tk.Button(window, text="Enumerate Subdomains", command=enumerate_subdomains)
enumerate_button.pack(pady=10)

# 创建输出框
result_label = tk.Label(window, text="Results:")
result_label.pack(pady=10)
result_text = tk.Text(window)
result_text.pack(pady=10)

# 运行 GUI 界面
window.mainloop()
