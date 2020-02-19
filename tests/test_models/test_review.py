#!/usr/bin/python3
"""
Unittest for Review Class.
"""
import unittest
from datetime import datetime
import models
import json

Review = models.review.Review
BaseModel = models.base_model.BaseModel


class TestReviewDocs(unittest.TestCase):
    """Tests cases for review Class. """

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('.......   Review  Class   .......')
        print('.................................\n\n')

    def test_doc_file(self):
        expected = '\nReview Class from Models Module\n'
        actual = models.review.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        expected = 'Review class handles all application reviews'
        actual = Review.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        expected = 'instantiates a new review'
        actual = Review.__init__.__doc__
        self.assertEqual(expected, actual)


class TestReviewInstances(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('........  Review  Class  ........')
        print('.................................\n\n')

    def setUp(self):
        self.review = Review()

    def test_instantiation(self):
        self.assertIsInstance(self.review, Review)

    def test_to_string(self):
        my_str = str(self.review)
        my_list = ['Review', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        my_str = str(self.review)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    def test_updated_at(self):
        self.review.save()
        actual = type(self.review.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        self.review_json = self.review.to_json()
        actual = 1
        try:
            serialized = json.dumps(self.review_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

    def test_json_class(self):
        self.review_json = self.review.to_json()
        actual = None
        if self.review_json['__class__']:
            actual = self.review_json['__class__']
        expected = 'Review'
        self.assertEqual(expected, actual)

    def test_email_attribute(self):
        self.review.text = "This place smells"
        if hasattr(self.review, 'text'):
            actual = self.review.text
        else:
            acual = ''
        expected = "This place smells"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main
