#!/bin/python3

import sys
import math


class Heap:
    def __init__(self):
        self.h = []

    # LEFT CHILD
    def leftChildIndex(self, parent_index):
        return 2 * parent_index + 1

    def leftChild(self, parent_index):
        return self.h[self.leftChildIndex(parent_index)]

    def hasLeftChild(self, parent_index):
        return self.leftChildIndex(parent_index) < self.size()

    # RIGHT CHILD
    def rightChildIndex(self, parent_index):
        return 2 * parent_index + 2

    def rightChild(self, parent_index):
        return self.h[self.rightChildIndex(parent_index)]

    def hasRightChild(self, parent_index):
        return self.rightChildIndex(parent_index) < self.size()

    # CHILD
    def smallestChildIndex(self, parent_index):
        if not self.hasRightChild(parent_index) or self.leftChild(parent_index) <= self.rightChild(parent_index):
            return self.leftChildIndex(parent_index)
        else:
            return self.rightChildIndex(parent_index)

    def largestChildIndex(self, parent_index):
        if not self.hasRightChild(parent_index) or self.leftChild(parent_index) >= self.rightChild(parent_index):
            return self.leftChildIndex(parent_index)
        else:
            return self.rightChildIndex(parent_index)

    # PARENT
    def parentIndex(self, child_index):
        return math.floor((child_index - 1) / 2)

    def parent(self, child_index):
        return self.parentIndex(child_index)

    def hasParent(self, child_index):
        return self.parentIndex(child_index) >= 0

    # GENERAL
    def get(self, index):
        return self.h[index]

    def isEmpty(self):
        if len(self.h) == 0:
            print("The heap is empty!")

    def heapifyUp(self):
        raise NotImplementedError("Please Implement this method")

    def heapifyDown(self):
        raise NotImplementedError("Please Implement this method")

    def swap(self, a, b):
        self.h[a], self.h[b] = self.h[b], self.h[a]

    def add(self, item):
        self.h.append(item)
        self.heapifyUp()

    def peek(self):
        self.isEmpty()
        return self.h[0]

    def pinch(self):
        self.isEmpty()
        tmp = self.h[0]
        self.h[0] = self.h.pop()
        self.heapifyDown()
        return tmp

    def size(self):
        return len(self.h)



class MinHeap(Heap):
    def heapifyDown(self):
        curr = 0

        while self.hasLeftChild(curr):
            smallest_child_index = self.smallestChildIndex(curr)

            if self.h[curr] < self.h[smallest_child_index]:
                break
            self.swap(curr, smallest_child_index)
            curr = smallest_child_index

    def heapifyUp(self):
        curr = self.size() - 1

        while self.hasParent(curr):
            parent_index = self.parentIndex(curr)

            if self.h[curr] > self.h[parent_index]:
                break
            self.swap(parent_index, curr)
            curr = parent_index


class MaxHeap(Heap):
    def heapifyDown(self):
        curr = 0

        while self.hasLeftChild(curr):
            smallest_child_index = self.largestChildIndex(curr)

            if self.h[curr] > self.h[smallest_child_index]:
                break
            self.swap(curr, smallest_child_index)
            curr = smallest_child_index

    def heapifyUp(self):
        curr = self.size() - 1

        while self.hasParent(curr):
            parent_index = self.parentIndex(curr)

            if self.h[curr] < self.h[parent_index]:
                break
            self.swap(parent_index, curr)
            curr = parent_index


class MedianHeap():
    def __init__(self):
        self.min_h = MinHeap()
        self.max_h = MaxHeap()

    def add(self, item):
        if item < self.median():
            self.max_h.add(item)
        else:
            self.min_h.add(item)

        if self.min_h.size() > self.max_h.size() + 1:
            # balance by moving one to max_h
            self.max_h.add(self.min_h.pinch())
        elif self.max_h.size() > self.min_h.size() + 1:
            # balance by moving one to min_h
            self.min_h.add(self.max_h.pinch())


    def median(self):
        if self.min_h.size() < self.max_h.size():
            return self.max_h.get(0)
        elif self.min_h.size() == self.max_h.size():
            if self.min_h.size() == 0:
                return 0
            return (self.min_h.get(0) + self.max_h.get(0)) / 2
        else:
            return self.min_h.get(0)


heap = MedianHeap()
n = int(input().strip())

a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    heap.add(a_t)
    print("%.1f" % heap.median())

