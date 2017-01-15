# -*- coding: utf-8 -*-
from datetime import timedelta


class Schedule(object):

    def __init__(self, items):
        """initial object Talk"""
        self.items = items
        self.not_time = []
        self.list_slice = []
        self.morning_max = timedelta(minutes=180)
        self.afternoon_max = timedelta(minutes=240)
        self.track_min_total = self.morning_max + self.afternoon_max

    def chunks_talks(self):
        """slice talks in 420 min"""
        total = timedelta()
        list_talk = []
        total_items = len(self.items) - 1

        for index, item in enumerate(self.items):
            if item["minute"]:
                total += item["minute"]
                if total > self.track_min_total:
                    self.list_slice.append(list_talk)
                    total = timedelta()
                    total += item["minute"]
                    list_talk = []
                list_talk.append(item)
                if index == total_items:
                    self.list_slice.append(list_talk)
                    break
            else:
                self.not_time.append(item)

        return {"not_time": self.not_time,
                "list_talk": self.list_slice}
