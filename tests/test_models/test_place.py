#!usr/bin/python3
"""
Unittest for Place Class.
"""
from models.base_model import BaseModel
from models.place import Place
import unittest
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Tests cases for Place Class. """

    def test_empty(self):
        m1 = Place()

    def test_if_base_model(self):
        m1 = Place()
        self.assertTrue(isinstance(m1, BaseModel))

    def test_id_unique(self):
        m1 = Place()
        m2 = Place()
        self.assertNotEqual(m1.id, m2.id)

    def test_id_type(self):
        m1 = Place()
        self.assertEqual(type(m1.id), str)

    def test_change_id(self):
        m1 = Place()
        m2 = Place()
        m1.id = m2.id
        self.assertEqual(m1.id, m2.id)

    def test_type_created_at(self):
        m1 = Place()
        self.assertEqual(type(m1.created_at), datetime)

    def test_type_updated_at(self):
        m1 = Place()
        self.assertEqual(type(m1.updated_at), datetime)

    def test_created_updated_compared(self):
        m1 = Place()
        self.assertEqual(m1.updated_at, m1.created_at)
        m1.save()
        date1 = m1.created_at
        date2 = m1.updated_at
        self.assertLess(date1, date2)

    def test_createdat_two_objects(self):
        m1 = Place()
        m2 = Place()
        date1 = m1.created_at
        date2 = m2.created_at
        self.assertLess(date1, date2)

    def test_str_return(self):
        m1 = Place()
        class_name = "Place"
        m1_id = str(m1.id)
        m1_dict = str(m1.__dict__)
        str_m1 = "[{}] ({}) {}".format(class_name, m1_id, m1_dict)
        self.assertEqual(str_m1, str(m1))

    def test_str_return_new_id(self):
        m1 = Place()
        class_name = "Place"
        m1.id = "1"
        m1_dict = str(m1.__dict__)
        str_m1 = "[{}] (1) {}".format(class_name, m1_dict)
        self.assertEqual(str_m1, str(m1))

    def test_save(self):
        m1 = Place()
        date1 = m1.created_at
        m1.save()
        date2 = m1.updated_at
        self.assertGreater(date2, date1)

    def test_to_dict(self):
        m1 = Place()
        class_dict = {"id": m1.id, "__class__": "Place"}
        self.assertTrue(set(class_dict.items()).issubset(
                        set(m1.to_dict().items())))

    def test_to_dict_createdupdated(self):
        m1 = Place()
        date1 = m1.updated_at.isoformat()
        date2 = m1.created_at.isoformat()
        class_dict = {"updated_at": date1, "created_at": date2}
        self.assertTrue(set(class_dict.items()).issubset(
                        set(m1.to_dict().items())))

    def test_copy_from_dict(self):
        m1 = Place()
        m2 = Place(**m1.to_dict())
        self.assertTrue(set(m1.__dict__.items()).issubset(
                        set(m2.__dict__.items())))

    def test_copy_kwargs_none(self):
        m1 = Place()
        testing = {}
        m2 = Place(**testing)
        self.assertFalse(set(m1.__dict__.items()).issubset(
            set(m2.__dict__.items())))

    def test_user_id(self):
        self.assertEqual(type(Place.user_id), str)

    def test_city_id(self):
        self.assertEqual(type(Place.city_id), str)

    def test_name(self):
        self.assertEqual(type(Place.name), str)

    def test_description_id(self):
        self.assertEqual(type(Place.description), str)

    def test_number_rooms(self):
        self.assertEqual(type(Place.number_rooms), int)

    def test_number_bathrooms(self):
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_max_guest(self):
        self.assertEqual(type(Place.max_guest), int)

    def test_price_by_night(self):
        self.assertEqual(type(Place.price_by_night), int)

    def test_latitude(self):
        self.assertEqual(type(Place.latitude), float)

    def test_longitude(self):
        self.assertEqual(type(Place.longitude), float)

    def test_amenity_ids(self):
        self.assertEqual(type(Place.amenity_ids), list)
