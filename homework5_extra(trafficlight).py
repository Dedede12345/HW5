traffic_light = ['green', 'yellow', 'red']
steps = ['go', 'steady', 'stop']
traffic_actions = dict(zip(traffic_light, steps))
print(traffic_actions['green'])