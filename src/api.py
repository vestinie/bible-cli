"""
API functions for interacting with bible-api.com
"""
import requests
import time


BASE_URL = "https://bible-api.com"
RATE_LIMIT_DELAY = 2  # seconds between requests


def get_verse(reference, translation="kjv"):
    """
    Fetch a specific Bible verse
    
    Args:
        reference (str): Bible verse reference (e.g., "John 3:16")
        translation (str): Bible translation code (default: "kjv")
    
    Returns:
        dict: Verse data with 'reference', 'text', and 'translation'
    
    Raises:
        requests.RequestException: If API request fails
        ValueError: If verse not found
    """
    url = f"{BASE_URL}/{reference}"
    params = {'translation': translation} if translation != 'kjv' else {}
    
    time.sleep(RATE_LIMIT_DELAY)  # Rate limiting
    response = requests.get(url, params=params, timeout=10)
    
    if response.status_code == 404:
        raise ValueError(f"Verse '{reference}' not found")
    
    response.raise_for_status()
    data = response.json()
    
    return {
        'reference': data.get('reference', reference),
        'text': data.get('text', '').strip(),
        'translation': data.get('translation_name', translation.upper())
    }


def get_random_verse(translation="kjv"):
    """
    Fetch a random Bible verse
    
    Args:
        translation (str): Bible translation code (default: "kjv")
    
    Returns:
        dict: Verse data with 'reference', 'text', and 'translation'
    
    Raises:
        requests.RequestException: If API request fails
    """
    url = f"{BASE_URL}/?random=verse"
    params = {'translation': translation} if translation != 'kjv' else {}
    
    time.sleep(RATE_LIMIT_DELAY)
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    
    return {
        'reference': data.get('reference', 'Unknown'),
        'text': data.get('text', '').strip(),
        'translation': data.get('translation_name', translation.upper())
    }


def get_chapter(reference, translation="kjv"):
    """
    Fetch an entire Bible chapter
    
    Args:
        reference (str): Chapter reference (e.g., "Psalm 23", "John 1")
        translation (str): Bible translation code (default: "kjv")
    
    Returns:
        dict: Chapter data with 'reference', 'text', and 'translation'
    
    Raises:
        requests.RequestException: If API request fails
        ValueError: If chapter not found
    """
    url = f"{BASE_URL}/{reference}"
    params = {'translation': translation} if translation != 'kjv' else {}
    
    time.sleep(RATE_LIMIT_DELAY)
    response = requests.get(url, params=params, timeout=10)
    
    if response.status_code == 404:
        raise ValueError(f"Chapter '{reference}' not found")
    
    response.raise_for_status()
    data = response.json()
    
    # Format verses in the chapter
    verses = data.get('verses', [])
    if verses:
        text = '\n\n'.join([f"[{v['verse']}] {v['text'].strip()}" for v in verses])
    else:
        text = data.get('text', '').strip()
    
    return {
        'reference': data.get('reference', reference),
        'text': text,
        'translation': data.get('translation_name', translation.upper())
    }


def search_verses(keyword, limit=5):
    """
    Search for verses containing a keyword
    Note: This is a simulated search using well-known verses
    The free API doesn't have a search endpoint
    
    Args:
        keyword (str): Keyword to search for
        limit (int): Maximum number of results
    
    Returns:
        list: List of verse dictionaries
    """
    # Common verses for demonstration
    # In a real app, you'd need a paid API or local database for search
    search_map = {
        'love': ['1 Corinthians 13:4-7', 'John 3:16', '1 John 4:8'],
        'faith': ['Hebrews 11:1', 'Romans 10:17', 'James 2:17'],
        'hope': ['Romans 15:13', 'Jeremiah 29:11', 'Hebrews 6:19'],
        'peace': ['John 14:27', 'Philippians 4:7', 'Romans 15:13'],
        'strength': ['Philippians 4:13', 'Isaiah 40:31', 'Psalm 46:1'],
        'joy': ['Nehemiah 8:10', 'Psalm 16:11', 'James 1:2'],
        'god': ['Genesis 1:1', 'John 3:16', 'Romans 8:28']
    }
    
    keyword_lower = keyword.lower()
    references = search_map.get(keyword_lower, [])
    
    results = []
    for ref in references[:limit]:
        try:
            verse = get_verse(ref)
            results.append(verse)
        except Exception:
            continue
    
    return results