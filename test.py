# -*- coding: utf-8 -*-
import unittest

from datetime import timedelta
from talk import Talk
from schedule import Schedule

TALK_OBJECTS = [{"title": "Writing Fast Tests Against Enterprise Rails 60min",
                 "minute": timedelta(minutes=60)},
                {"title": "Overdoing it in Python 45min",
                 "minute": timedelta(minutes=45)},
                {"title": "Lua for the Masses 30min",
                 "minute": timedelta(minutes=30)},
                {"title": "Ruby Errors from Mismatched Gem Versions 45min",
                 "minute": timedelta(minutes=45)},
                {"title": "Common Ruby Errors 45min",
                 "minute": timedelta(minutes=45)},
                {"title": "Rails for Python Developers lightning",
                 "minute": ""},
                {"title": "Communicating Over Distance 60min",
                 "minute": timedelta(minutes=60)},
                {"title": "Accounting-Driven Development 45min",
                 "minute": timedelta(minutes=45)},
                {"title": "Woah 30min",
                 "minute": timedelta(minutes=30)},
                {"title": "Sit Down and Write 30min",
                 "minute": timedelta(minutes=30)},
                {"title": "Pair Programming vs Noise 45min",
                 "minute": timedelta(minutes=45)},
                {"title": "Rails Magic 60min",
                 "minute": timedelta(minutes=60)},
                {"title": "Ruby on Rails: Why We Should Move On 60min",
                 "minute": timedelta(minutes=60)},
                {"title": "Clojure Ate Scala (on my project) 45min",
                 "minute": timedelta(minutes=45)},
                {"title": "Programming in the Boondocks of Seattle 30min",
                 "minute": timedelta(minutes=30)},
                {"title": "Ruby vs. Clojure for Back-End Development 30min",
                 "minute": timedelta(minutes=30)},
                {"title": "Ruby on Rails Legacy App Maintenance 60min",
                 "minute": timedelta(minutes=60)},
                {"title": "A World Without HackerNews 30min",
                 "minute": timedelta(minutes=30)},
                {"title": "User Interface CSS in Rails Apps 30min",
                 "minute": timedelta(minutes=30)}]


class TestTalks(unittest.TestCase):

    def setUp(self):
        """Start unittest attributes"""
        self.maxDiff = None
        self.task = Talk(["Writing Fast Tests Against Enterprise Rails 60min",
                          "Overdoing it in Python 45min",
                          "Lua for the Masses 30min",
                          "Ruby Errors from Mismatched Gem Versions 45min",
                          "Common Ruby Errors 45min",
                          "Rails for Python Developers lightning",
                          "Communicating Over Distance 60min",
                          "Accounting-Driven Development 45min",
                          "Woah 30min",
                          "Sit Down and Write 30min",
                          "Pair Programming vs Noise 45min",
                          "Rails Magic 60min",
                          "Ruby on Rails: Why We Should Move On 60min",
                          "Clojure Ate Scala (on my project) 45min",
                          "Programming in the Boondocks of Seattle 30min",
                          "Ruby vs. Clojure for Back-End Development 30min",
                          "Ruby on Rails Legacy App Maintenance 60min",
                          "A World Without HackerNews 30min",
                          "User Interface CSS in Rails Apps 30min"])
        self.task_objects = TALK_OBJECTS

    def test_task_objects(self):
        self.task.create_talk_objects()
        self.assertListEqual(self.task.objects, self.task_objects)


class TestSchedule(unittest.TestCase):

    def setUp(self):
        """Start unittest attributes"""
        self.task_objects = TALK_OBJECTS
        self.schedule = Schedule(self.task_objects)

    def test_chunks(self):
        chunks = self.schedule.chunks_talks()
        self.assertEqual(len(chunks['not_time']), 1)
        self.assertEqual(len(chunks['list_talk']), 2)

if __name__ == '__main__':

    # run tests
    unittest.main(verbosity=2)
