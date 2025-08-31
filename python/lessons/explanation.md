## Enhanced `flatten` for Custom Behavior

The `flatten` function can be enhanced to handle more complex scenarios, such as flattening up to a certain depth or including other iterable types like tuples and sets. The beauty of the `flatten_list` wrapper is that it can reuse the enhanced `flatten` without any changes.

Here's an enhanced version of the `flatten` function:

```python
def flatten_enhanced(iterable, max_depth=None, current_depth=0):
    for item in iterable:
        if isinstance(item, (list, tuple, set)) and (max_depth is None or current_depth < max_depth):
            yield from flatten_enhanced(item, max_depth, current_depth + 1)
        else:
            yield item

# Example Usage with flatten_enhanced
# To get a list from the enhanced generator, you'd still use list()
# or create a new wrapper function like flatten_list_enhanced

# Example 1: Flattening lists, tuples, and sets
nested_complex = [1, (2, {3, 4}), [5, 6], 7]
flat_complex = list(flatten_enhanced(nested_complex))
print(flat_complex) # Output might vary for sets due to inherent order, but elements will be there

# Example 2: Flattening up to a specific depth
nested_deep = [1, [2, [3, 4]], 5]
flat_shallow = list(flatten_enhanced(nested_deep, max_depth=1))
print(flat_shallow) # Output: [1, 2, [3, 4], 5]

flat_full = list(flatten_enhanced(nested_deep)) # No max_depth, flattens completely
print(flat_full) # Output: [1, 2, 3, 4, 5]
```

### Explanation of Enhancements:

*   **`flatten_enhanced(iterable, max_depth=None, current_depth=0)`**:
    *   Takes an `iterable` (can be a list, tuple, or set).
    *   `max_depth`: An optional integer to specify how many levels deep to flatten. If `None`, it flattens completely.
    *   `current_depth`: Tracks the current recursion depth, initialized to `0`.

*   **`if isinstance(item, (list, tuple, set))`**:
    *   The `isinstance` check now includes `tuple` and `set` in addition to `list`, allowing the function to flatten these iterable types as well.

*   **`and (max_depth is None or current_depth < max_depth)`**:
    *   This condition ensures that recursion only happens if `max_depth` is not set (i.e., `None`, meaning flatten all the way) OR if the `current_depth` is less than the specified `max_depth`. This controls the flattening depth.

*   **`yield from flatten_enhanced(item, max_depth, current_depth + 1)`**:
    *   The recursive call now passes `max_depth` down and increments `current_depth` to keep track of the current level of nesting.

This enhanced version provides more flexibility while maintaining the generator-based efficiency.