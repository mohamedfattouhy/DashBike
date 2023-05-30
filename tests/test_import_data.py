#  MANAGEMENT ENVIRONMENT
from src.preprocess.import_data import create_folder, load_json_files
import unittest
import os


# TESTS
class TestImportData(unittest.TestCase):

    def setUp(self):
        # variable configuration
        self.invalid_filenames_list = [
                "MMM_EcoCompt_19070220_archive.json"
                ]

        self.invalid_type_filenames = [
                "MMM_EcoCompt_19070220_archive.csv"
                ]

        self.invalid_filenames_str = "MMM_EcoCompt_19070220_archive.json"

        # Folder and sub-folder name
        self.dirpath_name = "test_dir"
        self.subdir_names = ["test_subdir1", "test_subdir2"]

    def test_create_folder_success(self):

        # Create test_dir folder
        create_folder(self.dirpath_name, self.subdir_names)

        # Assert
        self.assertTrue(os.path.exists(self.dirpath_name))
        self.assertTrue(os.path.exists(
                os.path.join(self.dirpath_name, self.subdir_names[0])
                ))
        self.assertTrue(os.path.exists(
                os.path.join(self.dirpath_name, self.subdir_names[1])
                ))

    def test_load_json_files(self):

        # Checks if a function generates an AttributeError
        with self.assertRaises(AttributeError):
            load_json_files(file_names=self.invalid_filenames_list)

        with self.assertRaises(AttributeError):
            load_json_files(file_names=self.invalid_type_filenames)

        with self.assertRaises(AttributeError):
            load_json_files(file_names=self.invalid_filenames_str)


if __name__ == '__main__':
    unittest.main()
