# Matrix Cascade

  > A simple Pygame based recreation of the iconic digital rain animation from the movie "The Matrix". Watch as the green characters cascade down the screen in random sequences and varying shades of green.

##Getting Started

  > Prerequisites

    >>You need to have pygame installed to run this animation. You can install it using pip:

      >>>bash

      >>>pip install pygame

##Running the Program

  > Simply clone this repository, navigate to the directory and run:

    >>bash

    >>python matrix_cascade.py

##Features

  > Cascading random characters inspired by the English keyboard.

  > Four varying shades of green to mimic the depth effect of the original animation.

  > Ability to run in full screen mode without any frame or borders.

  > Dynamic drop generation and management for smooth animation.

##How it works

  > Drop: The core component that defines the character, its speed, color and position.

  > Stream: Represents a column of drops. Each stream is responsible for a single column's cascading characters.

  > Layers: Four pre-defined layers that define the different shades of green and speeds.

  > Main Loop: The main loop (matrix_cascade()) that drives the animation. It handles screen updates and user inputs.

##Customizing

  > You can modify the constants at the beginning of the script to adjust the look and feel of the cascade:

    >>CELL_SIZE: Determines the size of each character cell.

    >>ROWS, COLS: Define the number of rows and columns for the cascade.

    >>chars: A list of characters that the cascade can use. By default, it uses characters from the English keyboard.

##License

  > This project is open source and available under the MIT License.

##Acknowledgments

  > Inspired by the iconic digital rain sequence from the movie "The Matrix".
