# Monty-Hall-Puzzle-Simulator
A Python script simulating the classic Monty Hall problem. Participants choose one of three doors to reveal either a car or a goat. The code explores the strategies of sticking with the original choice or switching doors after a goat is revealed, demonstrating the counterintuitive probability result of the game.

In the Monty Hall problem, there are three doors. Behind one of the doors, there is a valuable prize (often represented as a car, referred to as "BMW" in the code), and behind the other two doors, there are goats. A participant (you) chooses one door, and then the host (Monty Hall) opens one of the remaining doors to reveal a goat. The participant is then given the option to switch their choice to the other unopened door or stick with their initial choice.

The puzzle arises from the question: What is the best strategy for the participant? Should they stick with their original choice, or should they switch doors to improve their chances of winning the prize?

How the Code Simulates the Game:

The code initializes three doors as an empty list and two goat doors as an empty list.

It uses a loop to simulate the game scenario multiple times (in this case, 10 times).

Inside the loop:

One of the doors is randomly assigned the prize ("BMW"), and the other doors are assigned "GOAT."
A goat door is chosen randomly among the remaining doors (not the participant's choice) to be opened by the host.
The participant is asked if they want to swap their choice or not ("y" for yes, "n" for no).
If the participant chooses to swap:
If their initial choice was a goat door, they win by swapping.
If their initial choice was the prize door, they lose by swapping.
If the participant chooses not to swap:
If their initial choice was a goat door, they lose.
If their initial choice was the prize door, they win without swapping.
The code keeps track of the number of wins for both the swapping and not swapping strategies.
After the loop, the code prints the total number of wins for both the swapping and not swapping strategies.

Simulation and Probability:

The Monty Hall problem is counterintuitive because the best strategy is to always switch doors after the host reveals a goat. The code simulates this scenario and demonstrates that the swapping strategy has a higher probability of winning the prize compared to the not swapping strategy. Over a large number of simulations, you should observe that the "total swap wins" will generally be greater than the "total without swap wins." This is a demonstration of the concept of conditional probability.
