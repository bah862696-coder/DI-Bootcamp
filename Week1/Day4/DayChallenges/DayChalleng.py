
class Pagination:
    # Step 2 : Constructor
    def __init__(self, items=None, page_size=10):
        # If no items are given
        if items is None:
            items = []
        # Attributes
        self.items = items
        self.page_size = page_size
        # Current page index
        self.current_idx = 0
        # Total number of pages
        self.total_pages = math.ceil(len(self.items) / self.page_size)
    # Step 3 : Show visible items
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]
    # Step 4 : Navigation methods
    # Go to specific page
    def go_to_page(self, page_num):
        page_num = int(page_num)
        # Check if page is valid
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("Page number out of range")
        # Convert user page number to index
        self.current_idx = page_num - 1
        return self
    # Go to first page
    def first_page(self):
        self.current_idx = 0
        return self
    # Go to last page
    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self
    # Next page
    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self
    # Previous page
    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self
    # Step 5 : String method
    def __str__(self):
        return "\n".join(self.get_visible_items())
#
# Step 6 : Test the code
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
# First page
print(p.get_visible_items())
# ['a', 'b', 'c', 'd']
# Next page
p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']
# Last page
p.last_page()
print(p.get_visible_items())
# ['y', 'z']
# String method
print(str(p))
# Method chaining
print(
    p.first_page()
     .next_page()
     .next_page()
     .next_page()
     .get_visible_items()
# ['m', 'n', 'o', 'p']
# Error handling tests
try:
    p.go_to_page(10)
except ValueError as error:
    print(error)
try:
    p.go_to_page(0)
except ValueError as error:
    print(error)