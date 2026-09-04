# OS Shutdown Controller 🖥️

A simple command-line utility built with Python that triggers a timed system shutdown while providing an immediate option for the user to abort the process via terminal input.

## ✨ Features

* **Automated Shutdown Trigger:** Uses Python's built-in `os` module to communicate directly with the operating system's shutdown utility.
* **Abort Mechanism:** Allows users to cancel the pending shutdown command safely before the timer expires.
* **Streamlined Flow:** Executes sequentially without complex threading, perfect for quick automation tasks.

## 🚀 How it works

1. Run the script.
2. The program schedules a system shutdown to take place after 60 seconds.
3. Input `cancel` in the terminal prompt if you wish to stop the shutdown sequence.
4. If confirmed, the system aborts the timer; otherwise, the operating system proceeds with the countdown.

## 🛠️ Requirements

* Python 3.x installed.
* Compatible with Windows operating systems (utilizes native `shutdown` commands).
* No external dependencies required.
