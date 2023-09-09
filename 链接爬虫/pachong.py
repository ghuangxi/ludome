import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

# 爬取指定网页中的链接
def crawl_links():
    try:
        # 获取用户输入的网址
        url = url_entry.get()
        # 发送 HTTP 请求
        response = requests.get(url)
        # 解析 HTML 页面
        soup = BeautifulSoup(response.content, 'html.parser')
        links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                links.append(href)
        # 输出链接到 GUI 界面
        result_text.delete(1.0, tk.END)
        for link in links:
            result_text.insert(tk.END, link + "\n")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# 创建 GUI 界面
window = tk.Tk()
window.title("Web Link Crawler")
window.geometry('600x400')

# 创建输入框和按钮
url_label = tk.Label(window, text="Input the website URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(window, width=50)
url_entry.pack(pady=10)
crawl_button = tk.Button(window, text="Crawl Links", command=crawl_links)
crawl_button.pack(pady=10)

# 创建输出框
result_label = tk.Label(window, text="Links:")
result_label.pack(pady=10)
result_text = tk.Text(window)
result_text.pack(pady=10)

# 运行 GUI 界面
window.mainloop()
