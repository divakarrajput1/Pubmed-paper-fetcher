# PubMed Paper Fetcher
This Python program fetches research papers from PubMed based on a user-specified query. It identifies papers with at least one author affiliated with a pharmaceutical or biotech company and returns the results as a CSV file.
Code Organization
The project is organized as follows:

pubmed-paper-fetcher/                                                                                                                                                  
├── pubmed_fetcher/              
│   ├── __init__.py              
│   └── fetcher.py              
├── get_papers_list.py          
├── README.md                    
├── pyproject.toml               
└── .git/                        

# Installation
## Prerequisites
    (i) Python 3.8 or higher
    (ii) Poetry for dependency management


## Steps
   ### 1. Clone the Repository
    git clone https://github.com/your-username/pubmed-paper-fetcher.git
    cd pubmed-paper-fetcher
   ### 2. Install Dependencies
    poetry install

# Usage
 ## 1. Fetch papers using a PubMed query:
        poetry run get_papers_list "cancer AND 2023" -f output.csv
 ## 2. Command-line Options
            query: The PubMed query string (required).
            -d or --debug: Enable debug mode to print additional information.
            -f or --file: Specify the output CSV file. If not provided, results are printed to the console.

           poetry run get_papers_list "cancer AND 2023" -d -f output.csv
           Output:
           The program generates a CSV file with the following columns:

                PubmedID: Unique identifier for the paper.
                Title: Title of the paper.
                Publication Date: Date the paper was published.                
                Non-academic Author(s): Names of authors affiliated with non-academic institutions.                
                Company Affiliation(s): Names of pharmaceutical/biotech companies.
                Corresponding Author Email: Email address of the corresponding author.

# Tools and Libraries Used
   ## Libraries
      (i) Biopython: Used to interact with the PubMed API.
      (ii) argparse: Used to handle command-line arguments.
      (iii) Poetry: Used for dependency management and packaging.
   ## External Tools
      (i) PubMed API: Used to fetch research papers.
      (ii) Git: Used for version control.
      (iii) GitHub: Hosts the repository.

# Development
Running Tests
To test the program, run it with different queries and verify the output:

poetry run get_papers_list "diabetes AND 2023" -f diabetes_papers.csv
Debugging: Enable debug mode to see additional information:

poetry run get_papers_list "cancer AND 2023" -d
# Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

This README.md file provides all the necessary information for users and developers to understand, install, and use your program. Let me know if you need further assistance!

