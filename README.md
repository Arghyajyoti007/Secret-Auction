# 🕵️‍♂️ Silent Auction CLI Tool (Python)

A fun and interactive command-line auction system where participants can place secret bids. The program collects all bids and announces the winner at the end — without revealing interim bids, just like a silent auction!

---

## 🎯 Project Summary

This project simulates a **Silent Auction**, where multiple users can submit bids anonymously via the terminal. Once all participants have submitted their bids, the program identifies and announces the highest bidder and their bid amount.

---

## 🧠 Features

- Accepts multiple participant bids.
- Keeps all bids **secret** during the process.
- Dynamically determines the highest bidder.
- Clears the screen (via newlines) to simulate privacy between bidders.
- ASCII art banner via external module.

---

## 🛠️ Technologies Used

- Python 3
- Standard Input/Output
- Custom Modules:
  - `Day9_SilentAuctionArt` – contains the ASCII art/logo

---

## 📷 Sample Output
```
 ____  _ _            _        _   _             
/ ___|| (_)_ __   ___| |_ __ _| |_(_) ___  _ __  
\___ \| | | '_ \ / _ \ __/ _` | __| |/ _ \| '_ \ 
 ___) | | | | | |  __/ || (_| | |_| | (_) | | | |
|____/|_|_|_| |_|\___|\__\__,_|\__|_|\___/|_| |_|

What's your name : Alice
What's your bid : $ 150
Are there any other Bidders, Type 'Yes' or 'No' : yes
... (screen clears) ...

What's your name : Bob
What's your bid : $ 180
Are there any other Bidders, Type 'Yes' or 'No' : no

Max Bidder is Bob & his bid is $ 180

```

## 👨‍💻 Author
Arghyajyoti Samui  
GitHub: @Arghyajyoti007  


