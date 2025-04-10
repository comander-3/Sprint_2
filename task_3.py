class PointsForPlace:
    points = 0
        
    @staticmethod
    def get_points_for_place(place):
        if place > 100:
            return f'Баллы начисляются только первым 100 участникам'
        elif place < 1:
            return f'Спортсмен не может занять нулевое или отрицательное место'
        else:
            points = 101 - place
            return points


class PointsForMeters:
    points = 0

    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            return f'Количество метров не может быть отрицательным'
        else:
            points = meters * 0.5
            return points


class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        PointsForPlace.__init__(self)
        PointsForMeters.__init__(self)    

    
    def get_total_points(self, meters, place):
        total = self.get_points_for_meters(meters) + self.get_points_for_place(place)
        return total


print(PointsForPlace.get_points_for_place(10))
print(PointsForMeters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))