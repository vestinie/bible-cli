"""
Tests for API functions with mocked requests
"""
import pytest
from unittest.mock import patch, Mock
from src.api import get_verse, get_random_verse, get_chapter, search_verses


class TestGetVerse:
    """Tests for get_verse function"""
    
    @patch('src.api.requests.get')
    @patch('src.api.time.sleep')
    def test_get_verse_success(self, mock_sleep, mock_get):
        """Test successful verse retrieval"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'reference': 'John 3:16',
            'text': 'For God so loved the world...',
            'translation_name': 'King James Version'
        }
        mock_get.return_value = mock_response
        
        result = get_verse('John 3:16')
        
        assert result['reference'] == 'John 3:16'
        assert 'For God so loved the world' in result['text']
        assert result['translation'] == 'King James Version'
        mock_sleep.assert_called_once()
    
    @patch('src.api.requests.get')
    @patch('src.api.time.sleep')
    def test_get_verse_not_found(self, mock_sleep, mock_get):
        """Test verse not found"""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        with pytest.raises(ValueError, match="not found"):
            get_verse('Invalid 99:99')
    
    @patch('src.api.requests.get')
    @patch('src.api.time.sleep')
    def test_get_verse_with_translation(self, mock_sleep, mock_get):
        """Test verse with custom translation"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'reference': 'John 3:16',
            'text': 'For God so loved the world...',
            'translation_name': 'New International Version'
        }
        mock_get.return_value = mock_response
        
        result = get_verse('John 3:16', 'niv')
        
        assert result['translation'] == 'New International Version'
        mock_get.assert_called_once()


class TestGetRandomVerse:
    """Tests for get_random_verse function"""
    
    @patch('src.api.requests.get')
    @patch('src.api.time.sleep')
    def test_get_random_verse_success(self, mock_sleep, mock_get):
        """Test successful random verse retrieval"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'reference': 'Psalm 23:1',
            'text': 'The Lord is my shepherd...',
            'translation_name': 'King James Version'
        }
        mock_get.return_value = mock_response
        
        result = get_random_verse()
        
        assert 'reference' in result
        assert 'text' in result
        assert 'translation' in result
        mock_sleep.assert_called_once()
    
    @patch('src.api.requests.get')
    @patch('src.api.time.sleep')
    def test_get_random_verse_with_translation(self, mock_sleep, mock_get):
        """Test random verse with custom translation"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'reference': 'John 1:1',
            'text': 'In the beginning...',
            'translation_name': 'New International Version'
        }
        mock_get.return_value = mock_response
        
        result = get_random_verse('niv')
        
        assert result['translation'] == 'New International Version'


class TestGetChapter:
    """Tests for get_chapter function"""
    
    @patch('src.api.requests.get')
    @patch('src.api.time.sleep')
    def test_get_chapter_success(self, mock_sleep, mock_get):
        """Test successful chapter retrieval"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'reference': 'Psalm 23:1-6',
            'verses': [
                {'verse': 1, 'text': 'The Lord is my shepherd...'},
                {'verse': 2, 'text': 'He maketh me to lie down...'}
            ],
            'translation_name': 'King James Version'
        }
        mock_get.return_value = mock_response
        
        result = get_chapter('Psalm 23')
        
        assert result['reference'] == 'Psalm 23:1-6'
        assert '[1]' in result['text']
        assert '[2]' in result['text']
        mock_sleep.assert_called_once()
    
    @patch('src.api.requests.get')
    @patch('src.api.time.sleep')
    def test_get_chapter_not_found(self, mock_sleep, mock_get):
        """Test chapter not found"""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        with pytest.raises(ValueError, match="not found"):
            get_chapter('Invalid 99')


class TestSearchVerses:
    """Tests for search_verses function"""
    
    @patch('src.api.get_verse')
    def test_search_verses_love(self, mock_get_verse):
        """Test searching for 'love' verses"""
        mock_get_verse.return_value = {
            'reference': 'John 3:16',
            'text': 'For God so loved the world...',
            'translation': 'KJV'
        }
        
        results = search_verses('love', limit=1)
        
        assert len(results) >= 1
        assert results[0]['reference'] == 'John 3:16'
    
    @patch('src.api.get_verse')
    def test_search_verses_faith(self, mock_get_verse):
        """Test searching for 'faith' verses"""
        mock_get_verse.return_value = {
            'reference': 'Hebrews 11:1',
            'text': 'Now faith is...',
            'translation': 'KJV'
        }
        
        results = search_verses('faith', limit=2)
        
        assert len(results) >= 1
    
    def test_search_verses_no_results(self):
        """Test search with no matching keyword"""
        results = search_verses('nonexistentkeyword123')
        
        assert results == []
    
    @patch('src.api.get_verse')
    def test_search_verses_limit(self, mock_get_verse):
        """Test search respects limit parameter"""
        mock_get_verse.return_value = {
            'reference': 'Test',
            'text': 'Test text',
            'translation': 'KJV'
        }
        
        results = search_verses('love', limit=2)
        
        assert len(results) <= 2