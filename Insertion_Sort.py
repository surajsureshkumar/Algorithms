class InsertionSort:
    def __init__(self, array: list):
        self.array = array

    def insertion_sort(self):
        for idx in range(1,len(self.array)):
            current_element = self.array[idx]
            previous_element = idx - 1
            
            while previous_element >= 0 and self.array[previous_element] > current_element:
                self.array[previous_element + 1] = self.array[previous_element]
                previous_element -= 1
            
            self.array[previous_element + 1] = current_element
        return self.array
        
def main():
    array = [2,6,5,1,4,3]
    algo = InsertionSort(array)
    sorted_array = algo.insertion_sort()
    print(sorted_array)

if __name__ == "__main__":
    main() 