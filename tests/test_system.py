# tests/test_system.py

import unittest
from app import TaskManager

class TestSystem(unittest.TestCase):
    def test_complete_and_remove_task(self):
        manager = TaskManager()
        manager.add_task("Read book", "Finish the novel")
        manager.complete_task(0)
        manager.remove_task(0)
        self.assertEqual(len(manager.tasks), 0)

    def test_invalid_task_removal(self):
        manager = TaskManager()
        with self.assertRaises(ValueError):
            manager.remove_task(0)

if __name__ == "__main__":
    unittest.main()
