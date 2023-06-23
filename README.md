Welcome to the A* Algorithm Repository! Here, you'll find an implementation of the A* algorithm, which is used to find the shortest path between two points in a graph.


https://github.com/Amenephous/A_Star/assets/48127920/69357db8-6a13-4796-80f7-93239479da22
Astar Algorithm using one bot


https://github.com/Amenephous/A_Star/assets/48127920/c5339490-600d-41f5-bf0f-f9eff82457fe
Astar Algorithm using multiple bots



Before executing this code, it is essential to have the pyamaze library installed on your machine. Here are the steps to download it on different operating systems:

For Windows:
1.Open the command prompt by pressing the Windows key + R and typing cmd.
2.Enter the following command: pip install pyamaze

For Mac OS and Linux:
1.Open the terminal by pressing Command + Spacebar and typing terminal.
2.Enter the following command: pip install pyamaze


To get started, simply navigate to the code and uncomment the relevant sections based on your needs. We've included detailed comments to guide you through the process.

Our implementation includes two heuristics - Manhattan and Euclidean - to help you find the most efficient path. However, please note that the current code only checks for neighbors in the East, South, West, and North directions, and doesn't consider diagonal neighbors. The "maze" is developed initially and is used(Class_Setup1). A separate setup can be made by altering the maze, developing new maze using pyamaze or the same maze can be used to run the code. 

Additionally, this implementation supports up to three agents or robots for pathfinding and taking the shortest path. If you require more agents, it is easy to modify the code using similar lines of code. Simply refer to the provided comments for guidance.



We hope that this implementation helps you in your journey towards finding the shortest paths in your graphs. 
Please feel free to leave any comments or feedback on the repository.
