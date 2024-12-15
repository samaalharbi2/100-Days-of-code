# 🐢 Turtle Crossing Capstone 🛣️

Welcome to the **Turtle Crossing Capstone**, a fun and interactive game built using Python's Turtle Graphics. This project is part of the **100 Days of Code** series, following along with the **Complete Python Pro Bootcamp for 2023** by **Dr. Angela Yu**.

---

## 📅 Day 23 of 100: Build the Turtle Crossing Capstone Game

In this project, you will control a turtle character that needs to cross a busy road, avoiding obstacles like cars and trucks. The goal is to successfully make it to the other side without being hit, while increasing the difficulty as you progress.

---

## 🚀 Main Features

- **Player Movement**: Control the turtle using the **W** key to move it up the screen.
- **Traffic Obstacles**: Cars and trucks move across the screen in both directions, and the player must avoid them.
- **Increasing Difficulty**: As the game progresses, the speed of the traffic increases, making it harder to avoid collisions.
- **Score Tracking**: Each time the turtle successfully crosses the road, you gain a point, and the difficulty increases.

---

## 🛠️ Usage & Requirements

### Requirements:
- Python 3.11
- Turtle Graphics module

---

## 📝 Game Workflow

1. **Control the Turtle**:
   - **Move Up**: Use the **W** key to move the turtle up the screen.

2. **How the Traffic Moves**:
   - **Cars and Trucks**: Vehicles move across the screen in both directions. Avoid them by maneuvering the turtle.

3. **Scoring**:
   - Each time the turtle successfully crosses the road, you score a point. The game speed increases each time you cross to make the game more challenging.

4. **Avoid Collisions**:
   - If the turtle collides with a vehicle, the game resets, and you can try again.

---

## 🗂️ Game Files Structure

1. **`car_manager.py`**:
   - This file is responsible for generating and managing cars for each level. It handles the random placement and movement of vehicles, and it increases the traffic speed with each level.

2. **`player.py`**:
   - This file manages the player's movement. It listens for key inputs (specifically the **W** key) to move the turtle upwards. It also checks for collision with vehicles and handles game resets when necessary.

3. **`scoreboard.py`**:
   - This file keeps track of the player's current level. It displays the level at the top of the screen and updates it every time the player successfully crosses the road.



