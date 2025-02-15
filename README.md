# 🐍 My Simple Game - Terminal Snake Game (Dockerized)

Welcome to **My Simple Game**, a classic **Snake Game** built using Python and the `curses` library, designed to run directly in the terminal. This game is fully containerized with Docker, making it easy to run anywhere without installing dependencies. 🚀

## 📌 Features
- **Minimalist Terminal UI** – No fancy setup, just open your terminal and start playing.
- **Dockerized for Portability** – Run the game instantly without installing Python or dependencies.
- **Smooth Gameplay** – Responsive controls and real-time updates.
- **Lightweight & Fast** – Runs efficiently inside a container.

## 🚀 Quick Start
You don’t need to install Python or any packages—just use Docker to play the game instantly!

### 1️⃣ Clone the Repository
```bash
 git clone https://github.com/iemafzalhassan/my-simple-game.git
 cd my-simple-game
```

### 2️⃣ Build the Docker Image
```bash
 docker build -t iemafzalhassan/my-simple-game .
```

### 3️⃣ Run the Game
```bash
 docker run --rm -it iemafzalhassan/my-simple-game
```

## 🎮 How to Play
- **Arrow Keys** – Control the snake’s direction.
- **Eat Food** – Grow longer and increase your score.
- **Avoid Walls & Yourself** – The game ends if you hit a wall or your own tail.
- **Press 'Q'** – Quit the game anytime.

## 🔧 Troubleshooting
If you encounter an error like `setupterm: could not find terminal`, try running Docker with the `TERM` environment variable:
```bash
 docker run --rm -it -e TERM=xterm iemafzalhassan/my-simple-game
```

## 🛠️ Built With
- **Python** – Core game logic
- **Curses Library** – Terminal-based UI handling
- **Docker** – Containerization for portability

## 📢 Contributing
Got ideas to improve the game? Feel free to fork the repository, open issues, or submit pull requests!

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---
**Developed by [@iemafzalhassan](https://github.com/iemafzalhassan)** – Bringing DevOps and Gaming Together! 🐍

