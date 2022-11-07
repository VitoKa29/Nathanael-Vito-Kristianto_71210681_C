class PriorityQueueSortedList:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0

    def add(self, data, priority):
        self._data.append((data, priority))
        self._data=sorted(self._data, key=lambda x:x[1])

    def removePriority(self, priority):
        if self.isEmpty() is True:
            print("Priority Queue Kosong!")
        else:
            ind = []
            for i in range(len(self._data)):
                if self._data[i][1] == priority:
                    ind.append(self._data[i])
            for i in ind:
                self._data.remove(i)

    def remove(self):
        if self.isEmpty() is not True:
            x = 9999
            index = 0
            n = 0
            for i in range(len(self._data)):
                if self._data[i][1] > x:
                    pass
                else:
                    x = self._data[i][1]
                    index = i
                    n += 1
            del self._data[index]
        else:
            print("Priority Queue Kosong!") 

    def peek(self):
        if self.isEmpty() is not True:
            x = 9999
            data = ''
            for i in range(len(self._data)):
                if self._data[i][1] > x:
                    pass
                else:
                    x = self._data[i][1]
                    data = self._data[i][0]
            print("Data prioritas tertinggi: ('"+data+"',",x,")")
        else:
            print('Priority Queue Kosong')
    
    def update(self, priority, data):
        if self.isEmpty() is True:
            print("Priority Queue Kosong!")
        else:
            for i in range(len(self._data)):
                if self._data[i][1] == priority:
                    self._data[i] = (data, priority)
        
    def printIsiQueue(self):
        print("Isi Semua Queue: ",end='')
        for i in range(len(self._data)):
            print(self._data[i], end=', ')


sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
sortedList.update(4, "Karin")
sortedList.update(3, "Rafi")
sortedList.remove()
sortedList.removePriority(4)
sortedList.peek()
sortedList.printIsiQueue()
