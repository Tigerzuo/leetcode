class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # check if the difference is odd or even
        if abs((int(ord(coordinates[0])) - 96) - int(coordinates[1])) % 2 == 0:
            return False
        else:
            return True
