# Leetcode

## Two Sum

```py
def find_two_sum(nums, target):
    # Iterate through each element using its index 'i'
    for i in range(len(nums)): # Loop 1: Goes from index 0 to n-1
        # Iterate through the *remaining* elements *after* index 'i'
        # Start 'j' from 'i + 1' to avoid using the same element twice
        # and to avoid checking the same pair twice (e.g., nums[1]+nums[0] after nums[0]+nums[1])
        for j in range(i + 1, len(nums)): # Loop 2: Goes from index i+1 to n-1
            # Check if the sum of elements at indices i and j equals the target
            if nums[i] + nums[j] == target: # Check against 'target', not 0
                # Found the pair, return their indices
                return [i, j]


def two_sum_optimal(nums, target):
    seen_map = {}  # Dictionary to store number: index pairs encountered so far

    # Enumerate provides both index and value for each element
    for index, value in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - value

        # Check if this complement has been seen before (is in the map)
        if complement in seen_map:
            # Found the pair! Return the index of the complement (from the map)
            # and the current index.
            return [seen_map[complement], index]
        else:
            # Complement not found yet.
            # Store the current number and its index in the map for future checks.
            # We store it *after* the check to avoid using the same element twice.
            seen_map[value] = index

    # No return needed here because the problem guarantees a solution exists.


def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1

    while left < right: # Continue as long as the pointers haven't crossed
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum > target:
            # Sum is too large. Need a smaller sum.
            # Since the array is sorted, move the right pointer leftwards.
            right -= 1
        else: # current_sum < target
            # Sum is too small. Need a larger sum.
            # Since the array is sorted, move the left pointer rightwards.
            left += 1
```

## Valid Parentheses


```py
def is_valid_parentheses(s: str) -> bool:
    # Stack to keep track of opening brackets encountered.
    # We use a list as a stack: append() is push, pop() is pop.
    stack = []

    # Hash map to store mappings of closing brackets to opening brackets.
    # This makes checking for matches easy: map[')'] == '('
    bracket_map = {")": "(", "]": "[", "}": "{"}

    for char in s:
        # If the character is a closing bracket
        if char in bracket_map:
            # Check two things:
            # 1. Is the stack currently empty? (Means no matching opener)
            # 2. If not empty, does the top element match the required opener?
            #    - stack[-1] gets the top element without removing it (like peek)
            #    - bracket_map[char] gets the required opening bracket for the current closing bracket
            # If either condition fails, the string is invalid.
            # We use a placeholder '#' if the stack is empty to avoid errors
            # and ensure the comparison fails i f stack is empty.
            top_element = stack.pop() if stack else '#'

            if bracket_map[char] != top_element:
                return False # Mismatch or closing bracket with no opener
        else:
            # It's an opening bracket, push it onto the stack
            stack.append(char)

    # After the loop, the string is valid ONLY if the stack is empty.
    # If the stack is not empty, it means there were unclosed opening brackets.
    return not stack # Returns True if stack is empty, False otherwise
```

