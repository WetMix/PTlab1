# -*- coding: utf-8 -*-
import json

from Types import DataType
from DataReader import DataReader


class JSONDataReader(DataReader):

    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            raw = json.load(file)

        self.students = {}
        for student, subjects in raw.items():
            self.students[student] = [
                (subject, int(score))
                for subject, score in subjects.items()
            ]
        return self.students
