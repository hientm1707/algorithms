import random


class MyDS:
    
    
    def __init__(self) -> None:
        self.arr = []
        self.hmap = {}
    
    
    def add(self, ele):
        idx = self.hmap.get(ele, None)
        if idx is not None:
            return False
        self.arr.append(ele)
        self.hmap[ele] = len(self.arr) -1
        return True
        
    def remove(self, ele):
        idx = self.hmap.get(ele, None)
        if idx is not None:
            return False
        # Delete the element
        del self.hmap[ele]
        
        #Begin swap
        last_ele = self.arr[-1]
        
        #Move the last element to index
        self.hmap[last_ele] = idx
        self.arr[idx] = last_ele
        
        
        #Delete the last element at the moment
        del self.hmap[ele]
        self.arr.pop()
        return True
        
        
    
    def remove_random(self, ele):
        ele = random.choice(self.arr)
        return self.remove(ele=ele)


if __name__ == '__main__':
    
    
    ds = MyDS()
    ds.arr.append(1)
    
    
    ds2 = MyDS()
    print(ds.arr, ds2.arr)