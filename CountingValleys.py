def countingValleys(steps, path):
    counterList = []
    counter = 0
    counterList.append(counter)
    for step in path:
        if step == 'U':
            counter += 1
        else:
            counter -= 1
        counterList.append(counter)
    counter2 = 0
    for index in range(len(counterList) - 1):
        if counterList[index] == 0 and counterList[index + 1] < 0:
            counter2 += 1
    return counter2
