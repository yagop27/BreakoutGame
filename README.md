<h1>Breakout game</h1>

This game was built with Python, using mainly the Turtle library. In this game the player controls a paddle with the left and right keys on the keyboard, with the objective of destroying the bricks on the screen with the ball that bounces off of the paddle. 

<h2>Prerequisites:</h2>

  Python 3.6 or higher installed on your system.

<h2>Running the application:</h2>

  1- Clone this repository or download the project files.
  
  2- Run the game by executing the following command in your terminal:
  
    python main.py
  
  3- Controls:

   - Use the left and right arrow keys to move the paddle.
   - Click anywhere on the screen to exit the game when you're done.

<h2>Code Strutcture</h2>

This project was organized in different files, using a OOP approach (except for the main file) looking to make the code more readable and maintainable. The files of the program are as follows:

  - main.py:
    - The main game loop, including setup for the screen, paddle, ball, and bricks.
    - Handles game logic such as ball movement, collisions, score updates, and resetting levels.
  - paddle.py:
    - Contains the Paddle class that creates the paddle and includes methods to move it left and right.
  - bricks.py:
    - Contains the Bricks class used to create the brick objects in a grid format.
  - ball.py:
    - Contains the Ball class that manages ball movement and bouncing logic.
  - score.py:
    - Contains the Score class, which handles score display and updates as bricks are destroyed.

  
<h2>License</h2> 

This project is open-source and available under the MIT License.

<h2>Contact</h2> 

If you have any questions, feel free to reach out to me at yagopais@id.uff.br.
