# tests/test_unit.py

import unittest
from models import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Study", "Study for the exam")
        self.assertEqual(task.title, "Study")
        self.assertEqual(task.description, "Study for the exam")
        self.assertFalse(task.completed)

    def test_mark_completed(self):
        task = Task("Exercise", "Go for a run")
        task.mark_completed()
        self.assertTrue(task.completed)

if __name__ == "__main__":
    unittest.main()
