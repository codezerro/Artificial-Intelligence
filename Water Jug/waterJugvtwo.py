# water jug problem
from collections import deque


def WaterJug(jug1, jug2, goal):
    isPossible = False
    # dictonary  for store unique value
    map = {}
    # queue store the and dequeue --> list
    queue = deque()
    # path to store the solutation path -->list
    path = []
    # initial path (0,0)
    queue.append((0, 0))

    # main bfs
    while queue:
        first = queue[0]  # store the first element
        queue.popleft()  # pop the front element

        # check the node visited or not
        if map.get(tuple(first)) == 1:
            continue

        # never meet the jug requirments
        if (first[0] > jug1) or (first[1] > jug2) or (first[0] < 0) or (first[1] < 0):
            continue

        # store the path
        path.append((first[0], first[1]))
        # marked as visited
        map[tuple(first)] = 1

        # if reach the goal
        if (first[0] == goal) or (first[1] == goal):
            isPossible = True

            # change the jug
            if (first[0] == goal):
                if (first[1] != 0):
                    path.append((first[0], 0))
            else:
                if (first[1] != 0):
                    path.append((first[1], 0))

            # print("get the solutions", first[0], first[1])
            # print the solutions
            for val in range(len(path)):
                print(path[val][0], path[val][1])
            # print(path)
            return path
            break

        x = first[0]
        y = first[1]

        # fill the jug1 and jug2

        # 1. fil the jug1
        if (x < jug1):
            queue.append((jug1, y))

        # 2 fill the jug2
        if (y < jug2):
            queue.append((x, jug2))

        # Empty the jug1 and jug2
        # 3. empty the jug2
        if (y > 0):
            queue.append((x, 0))

        # 4. empty the jug1
        if (x > 0):
            queue.append((0, y))

        # 5. pour water jug2 --> jug1
        if (((x + y) > 0) and ((x + y) >= jug1) and (y > 0) and (x > 0)):
            aa = jug1
            bb = y - (jug1 - x)
            queue.append((aa, bb))

        # 6. pour water jug1 --> jug2
        if (((x + y) > 0) and ((x + y) >= jug2) and (x > 0) and (y > 0)):
            bb = jug2
            aa = x - (jug2 - y)
            queue.append((aa, bb))

        #  (x+y,0)
        if ((0 < (x + y) and (x + y) <= jug1) and (y > 0)):
            aa = x + y
            bb = 0
            queue.append((aa, bb))

        # (0, x+y)
        if ((0 < (x + y) and (x + y) <= jug2) and (x >= 0)):
            bb = x + y
            aa = 0
            queue.append((aa, bb))
    # loop end
    if not isPossible:
        print("Can't solve the problem! :-( ")


WaterJug(4, 3, 2)
