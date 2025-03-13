import argparse
from pubmed_fetcher.fetcher import fetch_papers, filter_non_academic_authors, generate_csv

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", help="PubMed query string")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-f", "--file", help="Output CSV file")
    args = parser.parse_args()
    
    print(f"Debug mode: {args.debug}")
    # Fetch papers
    papers = fetch_papers(args.query, debug=args.debug)

    # Filter non-academic authors
    filtered_papers = filter_non_academic_authors(papers)

    # Generate CSV or print to console
    generate_csv(filtered_papers, args.file)

if __name__ == "__main__":
    main()