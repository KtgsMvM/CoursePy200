class Glass:
    def __init__(self, capacity_volume: int, occupied_volume: int):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
    # glass = Glass()
    # print(type(book) is book. __class__)

if __name__ == "__main__":
    glass = Glass(200, 0)
    print(dir(glass))
