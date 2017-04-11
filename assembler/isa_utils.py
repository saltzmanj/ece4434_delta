class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        try:
            val = self.items.pop()
            return val
        except:
            return None;
    
    def __len__(self):
        return len(self.items)

    # def __str__(self):
    #     qlen = len(self);
    #     strout = "";
    #     for (index, el) in enumerate(self.items):
    #         if index == 0:
    #             strout += str(el.value) + "->"
    #         elif index == qlen - 1:
    #             strout += str(el.value)
    #         else:
    #             strout += str(el.value) + "->"
    #     return strout