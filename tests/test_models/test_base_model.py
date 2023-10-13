#!/usr/bin/python3
"""import usefuly models"""
import unittest
from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """unnit test class

    Args:
        unittest (test): inherites uniitest
    """
    def setUp(self):
        """set up class run for each test"""
        self.base_class = BaseModel()
    
    def test_variables(self):
        """check if variable is created"""
        self.assertIsNotNone(self.base_class.id)
        self.assertIsNotNone(self.base_class.created_at)
        self.assertIsNotNone(self.base_class.updated_at)

    def test_function(self):
        """test functions
        """
        self.base_class.name = "BaseModel"
        self.base_class.id = str(uuid4())
        exact_string = f"[{self.base_class.name}] ({self.base_class.id}) {self.base_class.__dict__}"
        self.assertEqual(str(self.base_class), exact_string)
        checkupdate = self.base_class.updated_at

        self.base_class.save()
        self.assertTrue(self.base_class.updated_at > checkupdate)
    
    def test_return_type(self):
        """test return type"""
        self.assertIsInstance(self.base_class.id, str)
        self.assertIsInstance(self.base_class.created_at, datetime)
        self.assertIsInstance(self.base_class.updated_at, datetime)
        self.assertIsInstance(self.base_class.to_dict(), dict)

        self.assertIsNone(self.base_class.save())
        self.assertIsNotNone(self.base_class.to_dict())
    
    def test_arguments(self):
        """check attributes"""
        self.assertTrue(hasattr(self.base_class, "id"))
        self.assertTrue(hasattr(self.base_class, 'created_at'))
        self.assertTrue(hasattr(self.base_class, 'updated_at'))
    
    def test_formate(self):
        """test formate"""
        self.assertEqual(self.base_class.to_dict(), self.base_class.__dict__)
        dummy_dict = {
            "id": "111000",
            "classs": "dummy",
            "created_at": "2017-09-28T21:03:54.052298",
            "updated_at": "2017-09-28T21:03:54.052302"
        }
        dummy_model = BaseModel(**dummy_dict)
        self.assertEqual(dummy_dict["id"], dummy_model.id)
        self.assertNotEqual(dummy_dict["created_at"], dummy_model.created_at)
        self.assertNotEqual(dummy_dict["updated_at"], dummy_model.updated_at)
        self.assertEqual(dummy_dict["classs"], dummy_model.classs)
    
    def test_models(self):
        """test models with created model"""
        self.base_class.name = "My_Base"
        self.base_class.my_number = 89
        
        my_base_json = self.base_class.to_dict()
        my_new_model = BaseModel(**my_base_json)

        self.assertEqual(self.base_class.name, my_new_model.name)
        self.assertEqual(self.base_class.my_number, my_new_model.my_number)


class TestBaseModelStorage(unittest.TestCase):
    """test base model storage liner"""    
    ...


if __name__=="__main__":
    unittest.main()