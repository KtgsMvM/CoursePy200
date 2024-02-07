from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume < 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем жидкости в стакане

     # TODO инициализировать объект "Стакан"


if __name__ == "__main__":
    glass1 = Glass(200, 50)  # TODO инициализировать два объекта типа Glass
    glass2 = Glass(300, 120)
    # TODO попробовать инициализировать не корректные объекты

    incorrect_capacity_volume_type = 0
    incorrect_occupied_volume_value = - 50
