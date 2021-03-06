class Heap(object):
    HEAP_SIZE = 10;
    def __init__(self):
        self.currentPosition = -1;
        self.heap = [0]*Heap.HEAP_SIZE;
    def insert(self, item):
        if self.isFull():
            print("heap is full..");
            return;
        self.currentPosition = self.currentPosition + 1;
        self.heap[self.currentPosition] = item;
        self.fixUp(self.currentPosition);
    def isFull(self):
        if self.currentPosition == Heap.HEAP_SIZE:
            return True;
        else:
            return False;
    def fixUp(self, index):
        parentIndex = int((index-1)/2);
        while parentIndex >=0 and self.heap[parentIndex] < self.heap[index]:
            temp = self.heap[parentIndex];
            self.heap[parentIndex] = self.heap[index];
            self.heap[index] = temp;
            index = parentIndex;
            parentIndex = int((index-1)/2);

    def printList(self):
        for i in range(0, self.currentPosition+1):
            print(self.heap[i]);

    def getMax(self):
        result = self.heap[0];
        self.currentPosition -= 1;
        self.heap[0] = self.heap[self.currentPosition];
        del self.heap[self.currentPosition + 1];
        self.fixDown(0, -1);
        print(result);

    def fixDown(self, index, upto):
        if upto < 0:
            upto = self.currentPosition;
        while index <= upto:
            leftChild = 2*index+1;
            rightChild = 2*index+2;

            if leftChild <= upto:
                childToSwap = None;
                if rightChild > upto:
                    childToSwap = leftChild;
                else:
                    if self.heap[leftChild] > self.heap[rightChild]:
                        childToSwap = leftChild;
                    else:
                        childToSwap = rightChild;
                if self.heap[index] < self.heap[childToSwap]:
                    temp = self.heap[index];
                    self.heap[index] = self.heap[childToSwap];
                    self.heap[childToSwap] = temp;
                else:
                    break;
            else:
                break;
    def heapSort(self):
        for i in range(0, self.currentPosition + 1):
            temp = self.heap[0];
            print("%d" % temp);
            self.heap[0] = self.heap[self.currentPosition - i];
            self.heap[self.currentPosition - i] = temp;
            self.fixDown(0,self.currentPosition - i -1);

heap = Heap();
heap.insert(12);
heap.insert(-3);
heap.insert(23);
heap.insert(4);
print("printing..");
heap.printList();
print("sorting...")
heap.heapSort();
heap.getMax();
