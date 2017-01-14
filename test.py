# -*- coding: utf-8 -*-
import unittest

from datetime import timedelta
from talk import Talk


class TestTalks(unittest.TestCase):

    def setUp(self):
        """Start unittest attributes"""
        self.task = Talk(["Writing Fast Tests Against Enterprise Rails 60min",
                          "Overdoing it in Python 45min",
                          "Rails for Python Developers lightning"])

    def test_task_objects(self):
        tasks = [{"title": "Writing Fast Tests Against Enterprise Rails 60min",
                  "minute": timedelta(minutes=60)},
                 {"title": "Overdoing it in Python 45min",
                  "minute": timedelta(minutes=45)}]
        self.task.create_talk_objects()
        self.assertListEqual(self.task.objects, tasks)

if __name__ == '__main__':

    # run tests
    unittest.main(verbosity=2)
