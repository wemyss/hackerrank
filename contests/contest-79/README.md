# 1 - Largest triangle area

## Question

You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

__Example:__
```
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.
```

<img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png" style="height:328px; width:400px" />

__Notes:__
- `3 <= points.length <= 50`.
- No points will be duplicated.
- `-50 <= points[i][j] <= 50`.
- Answers within `10^-6` of the true value will be accepted as correct.

## Solution notes


- Simple brute force solution. Iterate over all possible combinations and return the maximum triangle area that can be formed.
- Used a formula to calculate area from given points on a plane


---


# 2 - Binary tree pruning

## Question

We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

```
Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]

Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
```

<img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png" style="width:450px" />

```
Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
```
<img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png" style="width:450px" />

```
Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
```
<img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png" style="width:450px" />

__Note:__
- The binary tree will have at most 100 nodes.
- The value of each node will only be 0 or 1.


## Solution notes

- Recursive solution that prunes from the leaves up as far as it can.
- 2 base cases:
	- node can be removed (0 val and no children)
	- node cannot be removed (1 val or has children)
- 2 recursive cases:
	- has left child, prune the left child and assign the pruned subtree to `root.left`
	- has right child, prune the right child and assign the pruned subtree to `root.right`


---


# 3 - Largest sum of averages

## Question

We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

```
Example:
Input:
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation:
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
```


__Note:__
- `1 <= A.length <= 100`.
- `1 <= A[i] <= 10000`.
- `1 <= K <= A.length`.
- Answers within `10^-6` of the correct answer will be accepted as correct.

## Solution notes

- Did not attempt (started very late)
- Pretty sure it is a DP solution, perhaps a modified max contiguous sum?


---


# Question 4

- Did not see
