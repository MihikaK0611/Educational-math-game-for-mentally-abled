# Educational Math Game

## Overview

The Educational Math Game is an interactive learning tool developed using Pygame, specifically designed for mentally disabled individuals or small kids. This game aims to make learning math engaging and accessible through a visually appealing and interactive environment. It features three main sections: Learn, Play, and Test.

## Features

- **Learn Section**: Provides educational content using videos. Includes buttons for learning Addition, Subtraction, Multiplication, and Division.
- **Play Section**: Offers a story-based math adventure. Players solve math problems to progress through a narrative involving solving challenges like crossing a bridge.
- **Test Section**: A quiz-based game where players answer math questions to earn points and test their knowledge.

## Usage

### Run the Game

Start the game by running the `main.py` script:

```bash
python main.py

### Navigate the Game

#### Main Menu
- **Choose between Learn, Play, and Test sections.** 
- **Use the "Exit" button to close the game.**

#### Learn Section
- **Click on buttons to watch educational videos on various math topics.**

#### Play Section
- **Solve math problems to progress through the story.** 
- **Videos are shown at specific points in the story.**

#### Test Section
- **Answer quiz questions to test your math skills and earn points.**

### Controls

- **Back Button**: Return to the main menu from any section.
- **Enter Key**: Submit answers in the Play section.
- **Backspace Key**: Edit answers in the Play section.


## Code Structure

- **main.py**: Entry point of the game. Manages the main menu and navigation between different sections.
- **learn.py**: Handles the Learn section with educational videos and text.
- **play.py**: Manages the Play section with interactive math problems and a story-based adventure.
- **test.py**: Implements the Test section with a quiz-based math game.
- **utils.py**: Contains utility functions for drawing text, buttons, and handling sounds.
- **music_utils.py**: Provides functions to play, pause, and resume background music.

## Additional Information

- The game is designed to be visually appealing and interactive, with features tailored to make learning math accessible and enjoyable for mentally disabled individuals and small kids.
- Background music and sound effects enhance the interactive experience.
- Videos are used to illustrate key parts of the story and keep players engaged.
