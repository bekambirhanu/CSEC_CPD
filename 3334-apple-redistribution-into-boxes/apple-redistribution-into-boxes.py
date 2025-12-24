class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apple = sum(apple)
        capacity.sort()
        minimum_box_count = 0
        while total_apple > 0:
            box = capacity.pop()
            total_apple -= box
            minimum_box_count += 1
        return minimum_box_count