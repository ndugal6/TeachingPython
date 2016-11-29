from collections import deque

#using list as stack
stack = [
    'first', 'second', 'third', 'fourth'
]

stack.pop()
stack.append('new fourth')
print(stack)

queue = deque(stack)
queue.append('fifth')
queue.popleft()
print(queue)
for i in queue: print(i)

