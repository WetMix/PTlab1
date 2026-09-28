# -*- coding: utf-8 -*-
from Types import DataType
from CalcRating import CalcRating


class CalcQuartile:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: dict[str, float] = CalcRating(data).calc()

    def _get_third_quartile(self) -> float:
        values = sorted(self.rating.values())
        n = len(values)
        if n == 0:
            return 0.0
        # Метод ближайшего ранга (nearest-rank) для 75-го процентиля
        index = int(0.75 * (n - 1))
        return values[index]

    def get_students_in_third_quartile(self) -> dict[str, float]:
        threshold = self._get_third_quartile()
        return {
            student: score
            for student, score in self.rating.items()
            if score >= threshold
        }
