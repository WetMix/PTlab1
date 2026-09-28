# -*- coding: utf-8 -*-
import json

import pytest

from src.Types import DataType
from src.JSONDataReader import JSONDataReader


class TestJSONDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        data = {
            "Иванов Иван Иванович": {
                "математика": 67,
                "литература": 100,
                "программирование": 91
            },
            "Петров Петр Петрович": {
                "математика": 78,
                "химия": 87,
                "социология": 61
            }
        }
        return json.dumps(data, ensure_ascii=False), {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 78),
                ("химия", 87),
                ("социология", 61)
            ]
        }

    @pytest.fixture()
    def filepath_and_data(self, file_and_data_content, tmpdir):
        p = tmpdir.mkdir("jsondir").join("my_data.json")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data) -> None:
        reader = JSONDataReader()
        content = reader.read(filepath_and_data[0])
        assert content == filepath_and_data[1]

    def test_read_empty(self, tmpdir) -> None:
        p = tmpdir.mkdir("jsondir_empty").join("empty.json")
        p.write_text("{}", encoding='utf-8')
        reader = JSONDataReader()
        assert reader.read(str(p)) == {}
