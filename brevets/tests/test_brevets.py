"""
Nose tests for project, specifically testing the open and close
time calculations made in acp_times.py
"""
import nose    # Testing framework
import arrow
from acp_times import open_time, close_time

date = arrow.get("2021-01-01T00:00:00")

def test_open():
    assert open_time(0, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-01T00:00"
    assert open_time(50, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-01T01:28"
    assert open_time(200, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-01T05:53"
    assert open_time(201, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-01T05:55"
    assert open_time(300, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-01T09:00"
    assert open_time(399, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-01T12:06"
    assert open_time(400, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-01T12:08"
    assert open_time(401, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-01T12:10"
    assert open_time(600, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-01T18:48"
    assert open_time(1000, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-02T09:05"

def test_close():
    assert close_time(0, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-01T01:00"
    assert close_time(50, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-01T03:30"
    assert close_time(200, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-01T13:20"
    assert close_time(201, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-01T13:24"
    assert close_time(300, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-01T20:00"
    assert close_time(399, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-02T02:36"
    assert close_time(400, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-02T02:40"
    assert close_time(401, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-02T02:44"
    assert close_time(600, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-02T16:00"
    assert close_time(1000, 1000, date).format('YYYY-MM-DDTHH:mm') == "2021-01-04T03:00"
