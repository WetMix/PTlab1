# -*- coding: utf-8 -*-
import pytest

from src.Types import DataType
from src.CalcQuartile import CalcQuartile


class TestCalcQuartile:

    @pytest.fixture()
    def input_data(self) -> DataType:
        return {
            "Студент 1": [("математика", 100)],
            "Студент 2": [("математика", 90)],
            "Студент 3": [("математика", 80)],
            "Студент 4": [("математика", 70)],
        }

    def test_third_quartile_threshold(self, input_data) -> None:
        # Рейтинги: 70, 80, 90, 100
        # Q3 = 0.75 * (4-1) = 2.25 -> index=2 -> 90
        calc = CalcQuartile(input_data)
        assert calc._get_third_quartile() == 90

    def test_students_in_third_quartile(self, input_data) -> None:
        calc = CalcQuartile(input_data)
        result = calc.get_students_in_third_quartile()
        assert result == {"Студент 1": 100.0, "Студент 2": 90.0}

    def test_empty_data(self) -> None:
        calc = CalcQuartile({})
        assert calc.get_students_in_third_quartile() == {}
        assert calc._get_third_quartile() == 0.0

    def test_single_student(self) -> None:
        data = {"Один Студент": [("математика", 85)]}
        calc = CalcQuartile(data)
        assert calc.get_students_in_third_quartile() == {"Один Студент": 85.0}
