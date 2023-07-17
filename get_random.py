import random


"""
Follow up: Does the DS contain duplicates?, does it have to keep the order of insert
"""

class MyDS:
    
    
    def __init__(self):
        self.arr = []
        self.hmap = {}
    
    
    def add(self, ele):
        idx = self.hmap.get(ele, None)
        print(idx)
        if idx is not None:
            raise Exception('Cannot add')
        self.arr.append(ele)
        self.hmap[ele] = len(self.arr) -1
        
    def remove(self, ele):
        idx = self.hmap.get(ele, None)
        if idx is not None:
            raise Exception('Cannot remove')
        # Delete the element
        
        #Begin swap
        last_ele = self.arr[-1]
        
        #Move the last element to index
        self.hmap[last_ele] = idx
        self.arr[idx] = last_ele
        
        
        #Delete the last element at the moment
        del self.hmap[ele]
        self.arr.pop()
        
        
    def __str__(self) -> str:
        return f'Array: {self.arr}, Map: {self.hmap}'
        
        
    
    def remove_random(self, ele):
        ele = random.choice(self.arr)
        self.remove(ele=ele)


if __name__ == '__main__':
    ds = MyDS()
    ds.add(1)
    ds.add(2)
    print(ds)