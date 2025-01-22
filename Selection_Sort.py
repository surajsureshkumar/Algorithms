class SelectionSort:
    def __init__(self,array):
        self.array = array
    
    def selection_sort(self,):
        """Selection sort Algorith Implementation

        Returns:
            returns sorted list
        """
        for element in range(0 , len(self.array) - 1):
            minimum_value = element

            for uncompared_element in range(element + 1, len(self.array)):
                if self.array[uncompared_element] < self.array[minimum_value]:
                    minimum_value = uncompared_element

            if minimum_value != element:
                self.array[minimum_value] , self.array[element] = self.array[element], self.array[minimum_value]
        
        return self.array

def main():
    array = [3,5,7,56,33,2]
    selction_sort = SelectionSort(array)
    sorted_array = selction_sort.selection_sort()
    print(sorted_array)
    

if __name__ == "__main__":
    main()