from Bio import Entrez
from typing import List, Dict
import xml.etree.ElementTree as ET

# Set your email for PubMed API access
Entrez.email = "divakarrajput5818@gmail.com"

def fetch_papers(query: str, max_results: int = 10, debug: bool = False) -> List[Dict]:
    """
    Fetch papers from PubMed based on a query.
    """

    print(f"Debug parameter in fetch_papers: {debug}")
    if debug:
        print(f"Fetching papers for query: {query}")
        print(f"Max results to fetch: {max_results}")

    try:
        # Search PubMed
        if debug:
            print("Searching PubMed...")
        handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
        record = Entrez.read(handle)
        handle.close()

        # Get PubMed IDs
        id_list = record["IdList"]
        if not id_list:
            if debug:
                print("No papers found for the query.")
            return []

        if debug:
            print(f"Found {len(id_list)} papers. Fetching details...")

        # Fetch details for each paper
        handle = Entrez.efetch(db="pubmed", id=",".join(id_list), retmode="xml")
        papers = handle.read()
        handle.close()

        # Parse XML and extract relevant information
        root = ET.fromstring(papers)
        papers_data = []
        for article in root.findall(".//PubmedArticle"):
            paper = {}
            paper["PubmedID"] = article.find(".//PMID").text
            paper["Title"] = article.find(".//ArticleTitle").text
            paper["PublicationDate"] = article.find(".//PubDate/Year").text

            # Extract authors and affiliations
            authors = []
            affiliations = []
            for author in article.findall(".//Author"):
                last_name = author.find("LastName").text if author.find("LastName") is not None else ""
                fore_name = author.find("ForeName").text if author.find("ForeName") is not None else ""
                authors.append(f"{fore_name} {last_name}".strip())

                # Extract affiliations
                aff = author.find("AffiliationInfo/Affiliation")
                if aff is not None:
                    affiliations.append(aff.text)

            paper["Authors"] = authors
            paper["Affiliations"] = affiliations

            papers_data.append(paper)

        if debug:
            print(f"Successfully fetched {len(papers_data)} papers.")

        return papers_data

    except Exception as e:
        if debug:
            print(f"Error fetching papers: {e}")
        return []