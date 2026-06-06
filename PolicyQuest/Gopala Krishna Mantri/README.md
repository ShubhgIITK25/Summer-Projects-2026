## 3. Impact of gamma

the discount factor is a parameter that determiines how much the rewards in the future are cared offor.

### gamma = 0

in this case agent only cares about the immediate next step.
unless it is standing exactly one square away from the treasure, all actions look equally worthless (0 reward). The policy fails to converge , resulting in random wandering and wall-bumping.

### gamma = 0.6

the agent somewhat cares about the final goal
The agent takes teh shortest possible path. because taking a longer, safer detour reduces the final value, the agent will 'skim" the holes to minimize step count.


### gamma 0.99

when gamma is near 1, the agent values a reward 50 steps from now almost as much as a reward current step.
the agent seeks the safest possible path. because the penalty for taking a longer route is negligible, the agent is willing to take a walk around the outside edge of the map to avoid walking near any holes.

## 4. Impact of changing reward structure

### S=0; H=-1; G=1;

in this case the agent random paths but manages to reach the end goal without running into a hole.

### S=-1; H=-1; G=1;

in this case, the agent tries to run into a hole as fast as possibel. because there is penalty for staying longer but not as enough reward at goal to compensate for it

### S=-1; H=-20; G=100;

in this case, the agent takes the shortest possible path by avoiding holes to reach the goal. because there is penalty for staying longer and more penalty for falling into a hole, and enough reward at the goal to compensate