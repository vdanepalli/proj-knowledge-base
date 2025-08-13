# Coding Problems

## Leetcode 

### Fundamentals

- Big O -- runtime or memory usage vs input size
  - complexity and scalability, not speed (computer dependent)
  - provides you the vocabulary needed to decide which algorithm is best and communicate the same
- Data Structure -- way to store and access data.

- Linear Data Structures -- Arrays, Hash Tables, Linked Lists, Stacks and Queues

<br/><br/>

- Array (`list`) -- dynamic array -- flexible
  - Continuous block of memory 
  - Access, Append -- O(1)
  - Search, Insert -- O(n)
- Strings are like arrays, stored in continuous block, but are immutable. 
- Two Pointers
  - moving towards, away, same direction
  - O(n^2) --> O(n) -- solve in single pass

```py
# Reverse_List
def reverse_list(array):
    left, right = 0, len(array) - 1
    while left <= right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
```


<br/><br/>

- Hash Tables (`dict`)
  - key-value pairs
  - insert, lookup, delete - O(1)
  - hash function -- converts input into a number -- index

```py
# Duplicate_Exists

def duplicate_exists(array):
    seen = {}
    for element in array:
        if element in seen:
            return True
        seen[element] = 1
    return False
```


<br/><br/>

- Linked Lists
  - Each element is a Node (object) holding data and pointer
  - Scavenger hunt
  - Access - O(n)
  - Insert/Delete - O(1)
- Queues -- FIFO -- Enqueue, Dequeue -- LinkedLists
- Stacks -- LIFO -- Push, Pop
- `collections.deque` -- double ended queue


<br/><br/>

Tree -- hierarchical data. Nodes connected by edges. 
- Root, Parent, Child, Leaf
- Binary Trees -- max of 2 children (left, right)
- Binary Search Trees, Heaps

Tree Traversal
- Breadth First Search -- BFS -- level by level -- uses queue to track nodes to visit
  - finding shortest path. 
  - can't get lost along one path or a rabbit hole
- Depth First Search -- DFS -- as deep as possible -- uses backtracking -- commonly through recursion -- call stack behind scenes
  - checking if path exists, or need to visit each node


<br/><br/>

Heaps -- Priority Queue -- `heapq` -- implememnts min-heap by default
- a kind of binary tree.
- keeps track of min or max in a collection. 
- Min-Heap and Max-Heap
- finding min/max - O(1)
- adding - O(log n)
- removing min/max - O(log n)

### Amazon

Two Sum 

```py
# Brute-force implementation
def twoSum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

# Optimal solution using a hash map
def twoSum_optimal(nums, target):
    # Create a hash map to store numbers we have seen and their indices
    # Key: number, Value: index
    seen_map = {} # This is our O(1) lookup dictionary
    for i, num in enumerate(nums):
        complement = target - num
        # Check if the complement exists in our map
        if complement in seen_map:
            return [seen_map[complement], i]        
        seen_map[num] = i
```


<br/><br/>

Longest Substring Without Repeating Characters
- substring -- continuous block of characters
- generating substring -- O(n^2)
- check if substring is non-repeating -- O(n)
- Naive is O(n^3)

Sliding Window -- window on a sequence that can expand or shrink. 
- left, right -- boundaries of window
- find best window satisfying our condition. 


```py
def lengthOfLongestSubstring(s: str) -> int:
    char_set = set() # A set to store the characters in the current window
    left = 0 # The left pointer of our sliding window
    max_length = 0 # The result to store the maximum length found so far

    for right in range(len(s)): # The right pointer of our sliding window, which iterates through the string
        # Check if the current character is already in our window's set.
        # If it is, we need to shrink the window from the left.
        while s[right] in char_set:
            char_set.remove(s[left]) # Remove the character at the left pointer from the set
            left += 1 # Move the left pointer one step to the right        
        
        # Now that the window is valid (no s[right] duplicate),
        char_set.add(s[right]) # add the current character to the set.
        
        current_length = right - left + 1 # Update our result with the length of the current valid window
        max_length = max(max_length, current_length)
        
    return max_length

print(f'"abcabcbb" -> {lengthOfLongestSubstring("abcabcbb")}') # Expected: 3
print(f'"bbbbb" -> {lengthOfLongestSubstring("bbbbb")}')       # Expected: 1
print(f'"pwwkew" -> {lengthOfLongestSubstring("pwwkew")}')   # Expected: 3


def lengthOfLongestSubstring_optimized(s: str) -> int:
    # Map to store the last seen index of each character
    # Key: character, Value: index
    last_seen_map = {}
    
    left = 0
    max_length = 0

    for right in range(len(s)):
        char = s[right]
        
        # Check if we have seen this character before AND
        # if its last position is within our current window.
        if char in last_seen_map and last_seen_map[char] >= left:
            # If so, we have a repeat in our window.
            # Jump the left pointer to the position right after the last occurrence.
            left = last_seen_map[char] + 1
            
        # Update the last seen position for the current character.
        last_seen_map[char] = right
        
        # Calculate the length of the current window and update the max.
        current_length = right - left + 1
        max_length = max(max_length, current_length)
        
    return max_length

# Example Usage:
print(f'"abcabcbb" -> {lengthOfLongestSubstring_optimized("abcabcbb")}') # Expected: 3
print(f'"abba" -> {lengthOfLongestSubstring_optimized("abba")}')       # Expected: 2
print(f'"pwwkew" -> {lengthOfLongestSubstring_optimized("pwwkew")}')   # Expected: 3
```

<br/><br/>

String to Integer (atoi)

```py

```