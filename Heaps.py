import heapq

# Heaps (Min and Max) = stored as a tree (also called priority queue)

list_ex = [100, 248, 7, 23, 2, 24, 13]  # implement a heap using a list(array)
heapq.heapify(list_ex)  # creates a new heap from list_ex
print(list_ex)


# Get the indices for node relations from the array
def get_left_child(index):
    return 2 * index + 1


def get_right_child(index):
    return 2 * index + 2


def get_parent(index):
    return (index - 1) / 2


# Pop from the heap (removes and returns the min/max)
print(heapq.heappop(list_ex))
print(list_ex)

# Add to the heap
heapq.heappush(list_ex, 10)
print(list_ex)

