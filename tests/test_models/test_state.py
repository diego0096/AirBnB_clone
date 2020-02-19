#!usr/bin/python3
"""
Unittest for State Class.
"""
from models.base_model import BaseModel
from models.state import State
import unittest
from datetime import datetime


class TestState(unittest.TestCase):
    """Tests cases for State Class. """

    def test_empty(self):
        m1 = State()

    def test_if_base_model(self):
        m1 = State()
        self.assertTrue(isinstance(m1, BaseModel))

    def test_id_unique(self):
        m1 = State()
        m2 = State()
        self.assertNotEqual(m1.id, m2.id)

    def test_id_type(self):
        m1 = State()
        self.assertEqual(type(m1.id), str)

    def test_change_id(self):
        m1 = State()
        m2 = State()
        m1.id = m2.id
        self.assertEqual(m1.id, m2.id)

    def test_type_created_at(self):
        m1 = State()
        self.assertEqual(type(m1.created_at), datetime)

    def test_type_updated_at(self):
        m1 = State()
        self.assertEqual(type(m1.updated_at), datetime)

    def test_created_updated_compared(self):
        m1 = State()
        self.assertEqual(m1.updated_at, m1.created_at)
        m1.save()
        date1 = m1.created_at
        date2 = m1.updated_at
        self.assertLess(date1, date2)

    def test_createdat_two_objects(self):
        m1 = State()
        m2 = State()
        date1 = m1.created_at
        date2 = m2.created_at
        self.assertLess(date1, date2)

    def test_str_return(self):
        m1 = State()
        class_name = "State"
        m1_id = str(m1.id)
        m1_dict = str(m1.__dict__)
        str_m1 = "[{}] ({}) {}".format(class_name, m1_id, m1_dict)
        self.assertEqual(str_m1, str(m1))

    def test_str_return_new_id(self):
        m1 = State()
        class_name = "State"
        m1.id = "1"
        m1_dict = str(m1.__dict__)
        str_m1 = "[{}] (1) {}".format(class_name, m1_dict)
        self.assertEqual(str_m1, str(m1))

    def test_save(self):
        m1 = State()
        date1 = m1.created_at
        m1.save()
        date2 = m1.updated_at
        self.assertGreater(date2, date1)

    def test_to_dict(self):
        m1 = State()
        class_dict = {"id": m1.id, "__class__": "State"}
        self.assertTrue(set(class_dict.items()).issubset(
                        set(m1.to_dict().items())))

    def test_to_dict_createdupdated(self):
        m1 = State()
        date1 = m1.updated_at.isoformat()
        date2 = m1.created_at.isoformat()
        class_dict = {"updated_at": date1, "created_at": date2}
        self.assertTrue(set(class_dict.items()).issubset(
                        set(m1.to_dict().items())))

    def test_copy_from_dict(self):
        m1 = State()
        m2 = State(**m1.to_dict())
        self.assertTrue(set(m1.__dict__.items()).issubset(
                        set(m2.__dict__.items())))

    def test_copy_kwargs_none(self):
        m1 = State()
        testing = {}
        m2 = State(**testing)
        self.assertFalse(set(m1.__dict__.items()).issubset(
            set(m2.__dict__.items())))

    def test_name(self):
        self.assertEqual(type(State.name), str)
