from collections import deque
q = deque()
q.append((1, 2))
q.append((1, 1))
q.append((1, 3))
p = q[0]
print(p)

q.popleft()

print(q)
# q = [(2, 2), (3, 3)]
# q.append((1, 3))
# q.append((1, 1))
# q.append((1, 2))

# print(q)
# q.pop()
# # del q[0]
# print(q)
