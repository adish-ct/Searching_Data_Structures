# binary search

# set lower bound and upper bound
# find mid-value and check whether the number is find or not
# check the value is greater than or lesser than mid-value and re set lower bound and upper bound
# continue the process in a loop

# def binary_search(li, value):
#     lb = 0
#     ub = len(li) - 1
#     while lb <= ub:
#         mid = (lb + ub) // 2
#         if li[mid] == value:
#             print("Item found", mid)
#             return
#         if value < li[mid]:
#             ub = mid - 1
#         else:
#             lb = mid + 1
#     return print("item not found")
#
#
# new_li = [1, 3, 4, 5, 12, 24, 36, 42, 58, 69, 82]
# binary_search(new_li, 26)

""""
    ---   complexity of Binary Search ---  
        time complexity : O(log n)
        time complexity (best case) : O(1)
        time complexity (worst case) : O(log n)
        auxiliary space complexity : O(1)
        we can perform only sorted array
"""

# Linear Search

# we need to traverse entire list or array
# need a loop to traverse
# check the iterator is the element whichone we have to find
# condition statement for check
# return the output
#
# def linear_search(li, value):
#     for i in li:
#         if i == value:
#             return print("Value found", li.index(i))
#     return print("Value is not found")
#
#
# new_li = [1, 3, 4, 5, 12, 24, 36, 42, 58, 69, 82]
# linear_search(new_li, 24)
#
# """
#     --- complexity linear search ---
#
#     time complexity (best case) : O(1)
#     time complexity (worst case) : O(n)
#     space complexity  : O(1)
#     we can perform on unsorted array
# """
