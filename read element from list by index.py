def get_element_by_index(my_list, index):
       try:
           element = my_list[index]
           return element
       except IndexError:
           return "Error: Index is out of range."

# Example usage:
my_list = [10, 20, 30, 40, 50]
# Valid index
index_to_read = 2
element = get_element_by_index(my_list, index_to_read)
print("Element at index:",element)

  # Invalid index
index_to_read = 10
element = get_element_by_index(my_list, index_to_read)
print("Element at index:",element)