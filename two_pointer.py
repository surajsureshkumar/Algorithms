class TwoPointer:
    def __init__(self, array: list, left: int, right: int):
        self.array = sorted(array)
        self.left = 0
        self.right = len(array) - 1
    
    def algo(self,):
        """Two pointer algorithms"""
        # initialize any variables if required
        while self.left < self.right:
            # perform desired set of conditions like comparison or relation...
                # return or append to a result variable/array
            
            # move the left pointer and the right pointer to the next and previous value
            self.left += 1
            self.right -= 1
        
        # return desired result here
    
    # a full algorithm would look like this:
    # this algorithm finds pairs of numbers in the array whose sum equals a target value 
    # def algo(self, target: int):
    #     result = []
    #     while self.left < self.right:
    #         current_sum = self.array[self.left] + self.array[self.right]
    #         if current_sum == target:
    #             result.append((self.array[self.left], self.array[self.right]))
    #             self.left += 1
    #             self.right -= 1
    #         elif current_sum < target:
    #             self.left += 1
    #         else:
    #             self.right -= 1
    #     return result
    
def main():
    # edit the below code according to need
    array = [1,2,3,45,56]
    two_pointer = TwoPointer([])
    result = two_pointer.algo(array)
    print(result)

if __name__ == "__main__":
    main()