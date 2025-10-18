"""
Bible CLI - Command-line tool for fetching Bible verses
"""
import argparse
import sys
from src.api import get_verse, get_random_verse, get_chapter, search_verses


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Bible CLI - Fetch Bible verses from the command line",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m src.main verse "John 3:16"
  python -m src.main random
  python -m src.main chapter "Psalm 23"
  python -m src.main search "love"
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Verse command
    verse_parser = subparsers.add_parser('verse', help='Get a specific Bible verse')
    verse_parser.add_argument('reference', help='Bible verse reference (e.g., "John 3:16")')
    verse_parser.add_argument('--translation', '-t', default='kjv', 
                             help='Bible translation (default: kjv)')
    
    # Random command
    random_parser = subparsers.add_parser('random', help='Get a random Bible verse')
    random_parser.add_argument('--translation', '-t', default='kjv',
                              help='Bible translation (default: kjv)')
    
    # Chapter command
    chapter_parser = subparsers.add_parser('chapter', help='Get an entire chapter')
    chapter_parser.add_argument('reference', help='Chapter reference (e.g., "Psalm 23")')
    chapter_parser.add_argument('--translation', '-t', default='kjv',
                               help='Bible translation (default: kjv)')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search for verses by keyword')
    search_parser.add_argument('keyword', help='Keyword to search for')
    search_parser.add_argument('--limit', '-l', type=int, default=5,
                              help='Maximum number of results (default: 5)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        if args.command == 'verse':
            result = get_verse(args.reference, args.translation)
            print(f"\n📖 {result['reference']} ({result['translation']})")
            print(f"\n{result['text']}\n")
            
        elif args.command == 'random':
            result = get_random_verse(args.translation)
            print(f"\n📖 {result['reference']} ({result['translation']})")
            print(f"\n{result['text']}\n")
            
        elif args.command == 'chapter':
            result = get_chapter(args.reference, args.translation)
            print(f"\n📖 {result['reference']} ({result['translation']})")
            print(f"\n{result['text']}\n")
            
        elif args.command == 'search':
            results = search_verses(args.keyword, args.limit)
            if results:
                print(f"\n🔍 Found {len(results)} verse(s) containing '{args.keyword}':\n")
                for i, verse in enumerate(results, 1):
                    print(f"{i}. {verse['reference']}")
                    print(f"   {verse['text'][:100]}...\n")
            else:
                print(f"\n❌ No verses found containing '{args.keyword}'\n")
                
    except Exception as e:
        print(f"\n❌ Error: {e}\n", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()