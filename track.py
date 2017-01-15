# -*- coding: utf-8 -*-
from datetime import timedelta, datetime


class Track(object):

    def __init__(self, items):
        self.items = self.set_min_default(items)
        self.morning = []
        self.afternoon = []
        self.morning_max = timedelta(minutes=180)
        self.afternoon_max = timedelta(minutes=240)
        self.start = datetime.now().replace(hour=9, minute=0)
        self.lunch = self.start.replace(hour=12, minute=0)
        self.networking = self.start.replace(hour=16, minute=0)
        self.start_afternoon = self.start.replace(hour=13, minute=0)
        self.create_talk_combinations()

    def set_min_default(self, items):
        new_list = []
        for index, item in enumerate(items):
            if not item["minute"]:
                item['minute'] = timedelta(minutes=5)
            new_list.append(item)
        return new_list

    def create_talk_combinations(self):
        """Create talk list mornig or afternoon"""
        total_min = timedelta()
        for item in self.items:
            total_min += item['minute']
            if total_min <= self.morning_max:
                self.morning.append(item)
            else:
                self.afternoon.append(item)

    def mount_str(self, time, title):
        """ Mount str title and Time """
        time = time.strftime("%I:%M%p")
        return "%s %s \n" % (time,
                             title)

    def get_hour(self, items, start, interval="Lunch"):
        """Return list track hour"""
        items_str = ""
        for item in items:
            items_str += self.mount_str(start, item['title'])
            start += item["minute"]

        if interval == "Lunch":
            items_str += self.mount_str(self.lunch, interval)
        elif start >= self.networking and \
                start <= self.networking.replace(hour=17, minute=0):
            items_str += self.mount_str(start, interval)
        return items_str

    def get_list_track(self):
        """ Create string output"""
        track_str = self.get_hour(self.morning, self.start)

        track_str += self.get_hour(self.afternoon,
                                   self.start_afternoon,
                                   "Networking Event")
        return track_str
