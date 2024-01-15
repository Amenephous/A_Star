# A* Algorithm
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-1.0-blue)](https://github.com/Amenephous/A_Star/releases)


Welcome to the A* Algorithm Repository! Here, you'll find an implementation of the A* algorithm, which is used to find the shortest path between two points in a graph.

## Implementation 

https://github.com/Amenephous/A_Star/assets/48127920/69357db8-6a13-4796-80f7-93239479da22

Astar Algorithm using one bot


https://github.com/Amenephous/A_Star/assets/48127920/c5339490-600d-41f5-bf0f-f9eff82457fe

Astar Algorithm using multiple bots

## Usage
Before running this code, ensure the pyamaze library is installed on your machine. Follow these steps based on your operating system:

### For Windows:
1. Open the command prompt by pressing the Windows key + R and typing cmd.
2. Enter the following command: `pip install pyamaze`

### For Mac OS and Linux:
1. Open the terminal by pressing Command + Spacebar and typing terminal.
2. Enter the following command: `pip install pyamaze`


To get started, simply navigate to the code and uncomment the relevant sections based on your needs. We've included detailed comments to guide you through the process.

This implementation supports two heuristics - Manhattan and Euclidean - to efficiently find paths. However, please note that the current code only checks for neighbors in the East, South, West, and North directions, excluding diagonal neighbors. I initially developed the "maze" using pyamaze (Class_Setup1), but you can alter the maze, create a new one using pyamaze, or use the same maze to run the code.

Additionally, this supports up to three agents or robots for pathfinding. If you need more agents, it's easy to modify the code using similar lines. Simply refer to the provided comments for guidance.

I hope this implementation aids you in finding the shortest paths in your graphs. 

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.
## License

This project is licensed under the MIT License - see the LICENSE file for details.
