import numpy as np  # type: ignore
import random

# Step 1: Set up the road and actions
road_length = 5  # Positions: 0 to 4
actions = ["left", "right"]

# Step 2: Create a Q-table filled with zeros
Q = np.zeros((road_length, len(actions)))

# Step 3: Set learning parameters
episodes = 1000
learning_rate = 0.8
gamma = 0.9
epsilon = 0.3  # 30% chance to try something random

# Step 4: Train the agent
for episode in range(episodes):
    state = 0  # Start at position 0

    while state != 4:  # Goal is position 4
        # Epsilon-greedy choice
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, 1)  # Explore
        else:
            action = np.argmax(Q[state])  # Exploit

        # Take the action
        if action == 0:
            new_state = max(0, state - 1)
        else:
            new_state = min(4, state + 1)

        # Reward: 1 if goal reached, 0 otherwise
        reward = 1 if new_state == 4 else 0

        # Q-learning update
        Q[state, action] = Q[state, action] + learning_rate * (
            reward + gamma * np.max(Q[new_state]) - Q[state, action]
        )

        state = new_state

# Step 5: Show the learned Q-table
print("Learned Q-table:")
print(Q)

# Step 6: Let the agent try crossing the road
state = 0
steps = 0
path = []
print("\nAgent's path to cross the road:")
while state != 4:
    action = np.argmax(Q[state])
    if action == 0:
        state = max(0, state - 1)
        path.append("left")
    else:
        state = min(4, state + 1)
        path.append("right")
    steps += 1
    print(f"Step {steps}: Move {actions[action]} -> Position {state}")

print(f"\nFinal path: {' -> '.join(path)}")
print(f"Goal reached in {steps} steps!")
