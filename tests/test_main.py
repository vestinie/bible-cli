"""
Tests for CLI main module
"""
import pytest
from unittest.mock import patch, Mock
import sys
from io import StringIO
from src.main import main


class TestCLIVerse:
    """Tests for verse command"""
    
    @patch('src.main.get_verse')
    @patch('sys.argv', ['main.py', 'verse', 'John 3:16'])
    def test_verse_command_success(self, mock_get_verse):
        """Test verse command with valid reference"""
        mock_get_verse.return_value = {
            'reference': 'John 3:16',
            'text': 'For God so loved the world...',
            'translation': 'KJV'
        }
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            
        assert 'John 3:16' in output
        assert 'For God so loved the world' in output
        mock_get_verse.assert_called_once_with('John 3:16', 'kjv')
    
    @patch('src.main.get_verse')
    @patch('sys.argv', ['main.py', 'verse', 'Psalm 23:1', '-t', 'niv'])
    def test_verse_command_with_translation(self, mock_get_verse):
        """Test verse command with custom translation"""
        mock_get_verse.return_value = {
            'reference': 'Psalm 23:1',
            'text': 'The Lord is my shepherd...',
            'translation': 'NIV'
        }
        
        with patch('sys.stdout', new=StringIO()):
            main()
            
        mock_get_verse.assert_called_once_with('Psalm 23:1', 'niv')
    
    @patch('src.main.get_verse')
    @patch('sys.argv', ['main.py', 'verse', 'Invalid 99:99'])
    def test_verse_command_error(self, mock_get_verse):
        """Test verse command with error"""
        mock_get_verse.side_effect = ValueError("Verse not found")
        
        with pytest.raises(SystemExit) as exc_info:
            with patch('sys.stderr', new=StringIO()):
                main()
        
        assert exc_info.value.code == 1


class TestCLIRandom:
    """Tests for random command"""
    
    @patch('src.main.get_random_verse')
    @patch('sys.argv', ['main.py', 'random'])
    def test_random_command_success(self, mock_random):
        """Test random command"""
        mock_random.return_value = {
            'reference': 'Proverbs 3:5',
            'text': 'Trust in the Lord...',
            'translation': 'KJV'
        }
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            
        assert 'Proverbs 3:5' in output
        mock_random.assert_called_once_with('kjv')
    
    @patch('src.main.get_random_verse')
    @patch('sys.argv', ['main.py', 'random', '--translation', 'niv'])
    def test_random_command_with_translation(self, mock_random):
        """Test random command with custom translation"""
        mock_random.return_value = {
            'reference': 'John 1:1',
            'text': 'In the beginning...',
            'translation': 'NIV'
        }
        
        with patch('sys.stdout', new=StringIO()):
            main()
            
        mock_random.assert_called_once_with('niv')


class TestCLIChapter:
    """Tests for chapter command"""
    
    @patch('src.main.get_chapter')
    @patch('sys.argv', ['main.py', 'chapter', 'Psalm 23'])
    def test_chapter_command_success(self, mock_chapter):
        """Test chapter command"""
        mock_chapter.return_value = {
            'reference': 'Psalm 23:1-6',
            'text': '[1] The Lord is my shepherd...\n\n[2] He maketh me...',
            'translation': 'KJV'
        }
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            
        assert 'Psalm 23' in output
        assert 'The Lord is my shepherd' in output
        mock_chapter.assert_called_once_with('Psalm 23', 'kjv')


class TestCLISearch:
    """Tests for search command"""
    
    @patch('src.main.search_verses')
    @patch('sys.argv', ['main.py', 'search', 'love'])
    def test_search_command_with_results(self, mock_search):
        """Test search command with results"""
        mock_search.return_value = [
            {
                'reference': 'John 3:16',
                'text': 'For God so loved the world...',
                'translation': 'KJV'
            }
        ]
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            
        assert 'John 3:16' in output
        assert 'love' in output
        mock_search.assert_called_once_with('love', 5)
    
    @patch('src.main.search_verses')
    @patch('sys.argv', ['main.py', 'search', 'love', '--limit', '3'])
    def test_search_command_with_limit(self, mock_search):
        """Test search command with custom limit"""
        mock_search.return_value = []
        
        with patch('sys.stdout', new=StringIO()):
            main()
            
        mock_search.assert_called_once_with('love', 3)
    
    @patch('src.main.search_verses')
    @patch('sys.argv', ['main.py', 'search', 'nonexistent'])
    def test_search_command_no_results(self, mock_search):
        """Test search command with no results"""
        mock_search.return_value = []
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            
        assert 'No verses found' in output


class TestCLIHelp:
    """Tests for help command"""
    
    @patch('sys.argv', ['main.py'])
    def test_no_command_shows_help(self):
        """Test that running with no command shows help"""
        with pytest.raises(SystemExit) as exc_info:
            with patch('sys.stdout', new=StringIO()):
                main()
        
        assert exc_info.value.code == 1
    
    @patch('sys.argv', ['main.py', '--help'])
    def test_help_flag(self):
        """Test --help flag"""
        with pytest.raises(SystemExit) as exc_info:
            with patch('sys.stdout', new=StringIO()):
                main()
        
        assert exc_info.value.code == 0