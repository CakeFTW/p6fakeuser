import keyboard



print("press 'escape' to quit...")

record = keyboard.record()

#get rid of escape input
record.pop()

keys = []
times = []
up_down = []
for e in record:
    keys.append(e.scan_code)
    times.append(e.time)
    up_down.append(e.event_type)

keyboard.play(record)

#set times to be relative to starting time
times = [x - times[0] for x in times]
print(keys)


file = open("keyboard.txt","w")
file.write('KEYBOARD\n')
[file.write(str(x) + ',') for x in keys]
file.write('\n')
[file.write(str(x) + ',') for x in times]
file.write('\n')
[file.write(str(1)+',' if x in 'down' else str(0) + ',') for x in up_down ]
