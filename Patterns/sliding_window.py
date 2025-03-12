class SlidingWindow:
    def __init__(self, left: int, curr: int, answer: int):
        self.left = 0 # start of the window
        self.curr = 0 # to keep track of the current sum or any other variable according to the requirement
        self.answer = 0 # to store the final answer
        
    def sliding_window(self, arr:list, target: int):
        for right in range(len(arr) - 1):
            # add some logic here to track the sum
            # self.curr += arr[right]

            #while CONDITION_FOR_WINDOW_BEING_INVALID:
                # do some logic to "remove" the leftmost element from the window 
                # like below and increment the pointer to the next element 
                self.curr -= arr[self.left]
                self.left += 1
            
            # update answer by getting either the max or the min of the window as
            # per the requirement and update the variable
            #self.answer = max(right - self.left + 1, self.answer)
        
        return # desired answer
    
def main():
    arr = [3, 1, 2, 7, 4, 2, 1, 1, 5]
    target = 6
    window = SlidingWindow()
    print(window.sliding_window(arr,target))

if __name__ == "__main__":
    main()