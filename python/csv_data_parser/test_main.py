import unittest
import tempfile
import os
from solution import parse_csv


class TestCSVDataParser(unittest.TestCase):
    
    def setUp(self):
        """Set up temporary files for testing"""
        self.temp_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        """Clean up temporary files"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def create_temp_csv(self, filename, content):
        """Helper method to create temporary CSV files"""
        filepath = os.path.join(self.temp_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return filepath

    def test_basic_csv_parsing(self):
        """Test basic CSV parsing functionality"""
        csv_content = """name,age,city,salary
John Doe,30,New York,75000
Jane Smith,25,Los Angeles,65000
Bob Johnson,35,Chicago,80000"""
        
        filepath = self.create_temp_csv('test.csv', csv_content)
        result = parse_csv(filepath)
        
        expected = [
            {'name': 'John Doe', 'age': '30', 'city': 'New York', 'salary': '75000'},
            {'name': 'Jane Smith', 'age': '25', 'city': 'Los Angeles', 'salary': '65000'},
            {'name': 'Bob Johnson', 'age': '35', 'city': 'Chicago', 'salary': '80000'}
        ]
        
        self.assertEqual(result, expected)
        self.assertEqual(len(result), 3)

    def test_empty_file(self):
        """Test parsing empty CSV file"""
        filepath = self.create_temp_csv('empty.csv', '')
        result = parse_csv(filepath)
        self.assertEqual(result, [])

    def test_headers_only(self):
        """Test CSV with only headers"""
        csv_content = "name,age,city,salary"
        filepath = self.create_temp_csv('headers_only.csv', csv_content)
        result = parse_csv(filepath)
        self.assertEqual(result, [])

    def test_whitespace_handling(self):
        """Test CSV with extra whitespace"""
        csv_content = """name, age , city,salary
 John Doe , 30 , New York , 75000 
Jane Smith,25,Los Angeles,65000"""
        
        filepath = self.create_temp_csv('whitespace.csv', csv_content)
        result = parse_csv(filepath)
        
        expected = [
            {'name': 'John Doe', 'age': '30', 'city': 'New York', 'salary': '75000'},
            {'name': 'Jane Smith', 'age': '25', 'city': 'Los Angeles', 'salary': '65000'}
        ]
        
        self.assertEqual(result, expected)

    def test_empty_cells(self):
        """Test CSV with empty cells"""
        csv_content = """name,age,city,salary
John Doe,,New York,75000
,25,Los Angeles,
Bob Johnson,35,,80000"""
        
        filepath = self.create_temp_csv('empty_cells.csv', csv_content)
        result = parse_csv(filepath)
        
        expected = [
            {'name': 'John Doe', 'age': '', 'city': 'New York', 'salary': '75000'},
            {'name': '', 'age': '25', 'city': 'Los Angeles', 'salary': ''},
            {'name': 'Bob Johnson', 'age': '35', 'city': '', 'salary': '80000'}
        ]
        
        self.assertEqual(result, expected)

    def test_inconsistent_columns(self):
        """Test CSV with inconsistent column counts"""
        csv_content = """name,age,city,salary
John Doe,30,New York
Jane Smith,25,Los Angeles,65000,Extra
Bob Johnson,35,Chicago,80000"""
        
        filepath = self.create_temp_csv('inconsistent.csv', csv_content)
        result = parse_csv(filepath)
        
        # Should handle missing or extra columns gracefully
        self.assertEqual(len(result), 3)
        self.assertIn('name', result[0])
        self.assertIn('age', result[0])

    def test_file_not_found(self):
        """Test handling of non-existent file"""
        with self.assertRaises(FileNotFoundError):
            parse_csv('/nonexistent/file.csv')

    def test_single_row(self):
        """Test CSV with single data row"""
        csv_content = """name,age,city
John Doe,30,New York"""
        
        filepath = self.create_temp_csv('single_row.csv', csv_content)
        result = parse_csv(filepath)
        
        expected = [
            {'name': 'John Doe', 'age': '30', 'city': 'New York'}
        ]
        
        self.assertEqual(result, expected)

    def test_return_type(self):
        """Test that function returns correct types"""
        csv_content = """name,age
John,30"""
        
        filepath = self.create_temp_csv('types.csv', csv_content)
        result = parse_csv(filepath)
        
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], dict)
        self.assertIsInstance(result[0]['name'], str)
        self.assertIsInstance(result[0]['age'], str)

    def test_empty_lines(self):
        """Test CSV with empty lines"""
        csv_content = """name,age,city

John Doe,30,New York

Jane Smith,25,Los Angeles

"""
        
        filepath = self.create_temp_csv('empty_lines.csv', csv_content)
        result = parse_csv(filepath)
        
        # Should skip empty lines
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'John Doe')
        self.assertEqual(result[1]['name'], 'Jane Smith')

    def test_input_validation(self):
        """Test input validation"""
        with self.assertRaises(TypeError):
            parse_csv(123)
        with self.assertRaises(TypeError):
            parse_csv(None)


if __name__ == "__main__":
    unittest.main()
