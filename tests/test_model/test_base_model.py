""" unittest for BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ Test cases for BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """
            Setup BaseModel instance for all test cases
            ---------------
           
            Parameters
            ---------------
            class: curent class
        """
        cls.testModel = BaseModel()

    def setUp(self):
        """ setUp test module"""
        pass
    def tearDown(self):
        """ tearDown test module"""
        pass

    def test_class_doc(self):
        """
            Check for class docstring
            ---------------
           
            Parameters
            ---------------
            self: unittest instance
        """
        self.assertGreater(len(self.testModel.__doc__), 0)

    def test_methods_doc(self):
        """
            Check for class method docstring
            ---------------
           
            Parameters
            ---------------
            self: unittest instance
        """
        for func in dir(BaseModel):
            self.assertGreater(len(func.__doc__), 0)

    def test_instanciation(self):
        """
            Test intantiation of class
            ---------------

            Parameters
            ---------------
            self: unittest instance
        """
        self.assertEqual(str(type(self.testModel)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(self.testModel, BaseModel)
        self.assertTrue(issubclass(type(self.testModel), BaseModel))

    def test_unique_id(self):
        """
            Test of object unique_id arttribute
            ---------------

            Parameters
            ---------------
            self: unittest instance
        """
        self.assertEqual(str, type(self.testModel.id))
    def test_created_at(self):
        """
            Test of object created_at arttribute
            ---------------

            Parameters
            ---------------
            self: unittest instance
        """
        self.assertEqual(datetime.now(), self.testModel.created_at)
        self.assertEqual(datetime, type(self.testModel.created_at))

    def test_updated_at(self):
        """
            Test of object updated_at arttribute
            ---------------

            Parameters
            ---------------
            self: unittest instance
        """
        self.assertEqual(datetime, type(self.testModel.updated_at))

    def test_to_dict(self):
        """
            Test of object to_dict method
            ---------------

            Parameters
            ---------------
            self: unittest instance
        """
        new_dict = self.testModel.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue("to_dict" in dir(self.testModel))

    @classmethod
    def tearDownClass(cls):
        """ Remove all test instances """
        pass

