# -*- coding: utf-8 -*-
import unittest

from datetime import timedelta, datetime
from talk import Talk
from schedule import Schedule
from track import Track

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
        self.talk = Talk(["Writing Fast Tests Against Enterprise Rails 60min",
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
        self.talk_objects = [{"title": "Writing Fast Tests Against Enterprise"
                                       " Rails 60min",
                              "minute": timedelta(minutes=60)},
                             {"title": "Overdoing it in Python 45min",
                              "minute": timedelta(minutes=45)},
                             {"title": "Lua for the Masses 30min",
                              "minute": timedelta(minutes=30)},
                             {"title": "Ruby Errors from Mismatched Gem"
                                       " Versions 45min",
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
                             {"title": "Ruby on Rails: Why We Should Move On"
                                       " 60min",
                              "minute": timedelta(minutes=60)},
                             {"title": "Clojure Ate Scala (on my project)"
                                       " 45min",
                              "minute": timedelta(minutes=45)},
                             {"title": "Programming in the Boondocks of"
                                       " Seattle 30min",
                              "minute": timedelta(minutes=30)},
                             {"title": "Ruby vs. Clojure for Back-End"
                                       " Development 30min",
                              "minute": timedelta(minutes=30)},
                             {"title": "Ruby on Rails Legacy App Maintenance"
                                       " 60min",
                              "minute": timedelta(minutes=60)},
                             {"title": "A World Without HackerNews 30min",
                              "minute": timedelta(minutes=30)},
                             {"title": "User Interface CSS in Rails Apps"
                                       " 30min",
                              "minute": timedelta(minutes=30)}]

    def test_talk_objects(self):
        self.assertListEqual(self.talk.objects, self.talk_objects)

    def test_talk_raise(self):
        with self.assertRaises(Exception):
            Talk(["A World Without HackerNews 450min"])


class TestSchedule(unittest.TestCase):

    def setUp(self):
        """Start unittest attributes"""
        self.talk_objects = TALK_OBJECTS
        self.schedule = Schedule(self.talk_objects)

    def test_chunks(self):
        self.assertEqual(len(self.schedule.not_time), 1)
        self.assertEqual(len(self.schedule.list_slice), 2)
        count = len(self.schedule.list_slice[0]) + \
            len(self.schedule.list_slice[1])
        self.assertEqual(count, len(self.talk_objects))
        new_list = self.talk_objects[:]
        new_list.append({"title": "Rails for Python Developers lightning",
                         "minute": ""})
        schedule = Schedule(new_list)
        self.assertEqual(len(schedule.not_time), 2)
        count = len(schedule.list_slice[0]) + len(schedule.list_slice[1])
        self.assertEqual(count, len(new_list))

    def test_str_track(self):
        str_s = self.schedule.print_track()
        self.assertIsNotNone(str_s)
        self.assertTrue("Track 1" and "Track 2" in str_s)

    def test_two_talk(self):
        talks = [{"title": "Writing Fast Tests Against Enterprise"
                           " Rails 60min",
                  "minute": timedelta(minutes=60)},
                 {"title": "Overdoing it in Python 45min",
                  "minute": timedelta(minutes=45)}]
        schedule = Schedule(talks)
        self.assertEqual(len(schedule.not_time), 0)
        str_s = schedule.print_track()
        str_title = "09:00AM Writing Fast Tests Against Enterprise"
        self.assertTrue(str_title in str_s)


class TestTrack(unittest.TestCase):

    def setUp(self):
        """Start unittest attributes"""
        self.talk_objects = TALK_OBJECTS
        self.schedule = Schedule(self.talk_objects)
        self.track = Track(self.schedule.list_slice[0])

    def test_combination(self):
        self.track.get_list_track()

    def test_mount_str(self):
        time = datetime.now().replace(hour=12, minute=0)
        str_mount = self.track.mount_str(time, "Lunch")
        self.assertEqual(str_mount, "12:00PM Lunch \n")

if __name__ == '__main__':

    # run tests
    unittest.main(verbosity=2)
