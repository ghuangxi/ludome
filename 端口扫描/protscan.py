import socket
import threading
import tkinter as tk


def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False


class PortScannerGUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Port Scanner")
        self.window.geometry("600x500")

        tk.Label(self.window, text="Enter IP Address:").pack()
        self.ip_entry = tk.Entry(self.window)
        self.ip_entry.pack()

        tk.Label(self.window, text="Enter Starting Port:").pack()
        self.start_port_entry = tk.Entry(self.window)
        self.start_port_entry.pack()

        tk.Label(self.window, text="Enter Ending Port:").pack()
        self.end_port_entry = tk.Entry(self.window)
        self.end_port_entry.pack()

        self.result_text = tk.Text(self.window)
        self.result_text.pack()

        self.scan_button = tk.Button(self.window, text="Scan", command=self.scan_ports)
        self.scan_button.pack()

    def scan_ports(self):
        self.result_text.delete("1.0", tk.END)
        ip = self.ip_entry.get()
        start_port = int(self.start_port_entry.get())
        end_port = int(self.end_port_entry.get())

        self.scan_button.config(state=tk.DISABLED)

        for port in range(start_port, end_port+1):
            t = threading.Thread(target=self.check_port, args=(ip, port))
            t.start()

    def check_port(self, ip, port):
        result = scan_port(ip, port)
        if result:
            self.result_text.insert(tk.END, f"Port {port} is open\n")

        self.scan_button.config(state=tk.NORMAL)


if __name__ == '__main__':
    scanner = PortScannerGUI()
    scanner.window.mainloop()
