class LinearSearch:
    def __init__(self, array: list):
        self.array = sorted(array)

    def search(self, target):
        pass


def main():
    sorted_array = [1,2,3,4,5,6,7,8]
    target_value = 7
    linear_search = LinearSearch(sorted_array)
    index_of_number = linear_search.search(target_value)

    if index_of_number != -1:
        print(f'Target value {target_value} found at {index_of_number}')
    else:
        print(f'Target value {target_value} not found')

if __name__ == "__main__":
    main()

