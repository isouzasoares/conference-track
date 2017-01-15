# -*- coding: utf-8 -*-
import re

from datetime import timedelta
from schedule import Schedule


class Talk(object):

    def __init__(self, talk_list):
        """initial object Talk"""
        self.talk_list = talk_list
        self.objects = []
        self.sorts = []
        self.create_talk_objects()

    def create_talk_objects(self):
        """return talk talk title and talk
           time"""
        for talk in self.talk_list:
            minute = re.search(r'(\d+min)', talk)
            if minute:
                minute = minute.group()
                minute = re.match(r'(\d+)', minute).group()
                minute = timedelta(minutes=int(minute))
                if minute >= timedelta(minutes=420):
                    raise Exception("Entries older than 420"
                                    " minutes are not allowed")
            else:
                minute = ""
            self.objects.append({"title": talk,
                                 "minute": minute})

    def output(self):
        """ Return output talk """
        print(Schedule(self.objects).print_track())
