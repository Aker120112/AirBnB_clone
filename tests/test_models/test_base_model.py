import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_initialization(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_method(self):
        model = BaseModel()
        self.assertEqual(str(model), f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}")

    def test_save_method(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        model = BaseModel()
        dict_rep = model.to_dict()
        self.assertEqual(dict_rep['__class__'], 'BaseModel')
        self.assertEqual(dict_rep['created_at'], model.created_at.isoformat())
        self.assertEqual(dict_rep['updated_at'], model.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()

