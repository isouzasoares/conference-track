# -*- coding: utf-8 -*-
from datetime import timedelta
from track import Track


class Schedule(object):

    def __init__(self, items):
        """initial object Talk"""
        self.items = items
        self.not_time = []
        self.list_slice = []
        self.track_min_total = timedelta(minutes=420)
        self.chunks_talks()

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
            else:
                self.not_time.append(item)

            if index == total_items:
                self.list_slice.append(list_talk)
                break

        self.splice_not_time()
        return {"not_time": self.not_time,
                "list_talk": self.list_slice}

    def splice_not_time(self):
        """Add not time in list_slice"""
        minutes_index = []
        for list_item in self.list_slice:
            sum_min = sum([i["minute"].seconds / 60 for i in list_item])
            minutes_index.append(sum_min)
        sum_min = minutes_index[:]
        sum_min.sort()

        for lighttalk in self.not_time:
            for minute in sum_min:
                if ((minute + 5) <= (self.track_min_total.seconds / 60)):
                    index = minutes_index.index(minute)
                    self.list_slice[index].append(lighttalk)
                    break

    def print_track(self):
        """ """
        str_track = ""
        for index, item in enumerate(self.list_slice):
            str_track += "Track %s \n" % (str(index + 1))
            str_track += Track(item).get_list_track()
        return str_track
