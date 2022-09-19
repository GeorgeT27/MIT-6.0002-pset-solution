# Brute force vs greedy algorithm

I have run my code several time. What I have found out is for a set of 10 data points, brute force seems to take shorter time. Theoretically, brute force should take longer time than greedy, so why is my algorithm showing the wrong result? 

Firstly, I think I didn't optimise my greedy algorithm. After I find which pigs can fit in the first valid spaceship. I need to go through each pigs that I have already put into the ship again and again which takes time when number is large.

 Secondly, when I run the brute force algorithm, there is n! numbers of partition I need to look at. However, I didn't look at them fully. (If one spaceship in a partition exceed the limit, I will break the loop which means I am not going to look at that partition again.) Therefore, this will reduce significant amount of time. 

I think when n is large, the runtime for brute force will be more than greedy algorithm.