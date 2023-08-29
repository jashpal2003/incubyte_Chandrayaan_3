from spacecraft import Spacecraft

# test 1: Moving in a straight line
initial_position = (0, 0, 0)
initial_direction = 'N'
commands = ['f', 'f', 'f', 'f', 'f']
chandrayaan_3 = Spacecraft(initial_position[0], initial_position[1], initial_position[2], initial_direction)
chandrayaan_3.execute_commands(commands)
print("Example 1 - Final Position:", chandrayaan_3.position)
print("Example 1 - Final Direction:", chandrayaan_3.direction)

# test 2: Turning and moving
initial_position = (0, 0, 0)
initial_direction = 'E'
commands = ['l', 'f', 'u', 'r', 'f', 'b', 'b']
chandrayaan_3 = Spacecraft(initial_position[0], initial_position[1], initial_position[2], initial_direction)
chandrayaan_3.execute_commands(commands)
print("Example 2 - Final Position:", chandrayaan_3.position)
print("Example 2 - Final Direction:", chandrayaan_3.direction)

# test 3: Moving and turning in different directions
initial_position = (0, 0, 0)
initial_direction = 'N'
commands = ['f', 'l', 'f', 'd', 'r', 'f', 'u']
chandrayaan_3 = Spacecraft(initial_position[0], initial_position[1], initial_position[2], initial_direction)
chandrayaan_3.execute_commands(commands)
print("Example 3 - Final Position:", chandrayaan_3.position)
print("Example 3 - Final Direction:", chandrayaan_3.direction)
