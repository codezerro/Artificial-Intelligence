# water jug problem
from collections import deque


def waterjug(jug1, jug2, goal):
    # dictonary  for store unique value
    map = {}
    # queue store the and dequeue --> list
    queue = deque()
    # path to store the solutation path -->list
    path = []
    # initial path (0,0)
    queue.append((0, 0))

    while queue:
        first = queue[0]  # store the first element of the queue
        # print("f", first)
        queue.popleft()
        # queue.pop(0)  # pop the element
        # check the node visited or not
        tup = tuple(first)
        if map.get(tup) == 1:
            # print(map.get(tup))
            continue

        # meet the jug
        if (first[0] > jug1) or (first[1] > jug2) or (first[0] < 0) or (first[1] < 0):
            continue
        # if not get the goal
        # 1.fill the jug2 and jug1 keep at it is
        queue.append((first[0], jug2))
        # 2.fill the first jug1 and jug2 keep at it is
        queue.append((jug1, first[1]))
        # print(f'queue ==>', queue)

        path.append(first)  # add into the main path
        map[tuple(first)] = 1  # marked as visited
        # print(f'path ==> ', path)

        # check the get the destination or not
        if (first[0] == goal) or (first[1] == goal):
            print("get the solutions", first[0], first[1])
            print(queue)
            break

        # 3.pour water jug1 to ju2 and jug2 to jut1 #todo
        for i in range(max(jug1, jug2)):

            # // pour amount ap from Jug2 to Jug1
            c = first[0] + i
            d = first[1] - i

            # // check if this state is possible or not
            if (c == jug1) or (d == 0 and d >= 0):
                queue.append((c, d))
            # // Pour amount ap from Jug 1 to Jug2
            c = first[0] - i
            d = first[1] + i

            # // check if this state is possible or not
            if (c == 0 and c >= 0) or (d == jug2):
                print(c, d)
                queue.append((c, d))

        # 4.empty jug1 (0,y)
        queue.append((0, jug2))
        # 5.empty jug2 (x,0)
        queue.append((jug1, 0))


waterjug(4, 3, 2)


# u = first
