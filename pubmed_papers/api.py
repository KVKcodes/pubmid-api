"""PubMed Papers API - Core functionality for PubMed paper analysis."""

from typing import Iterator, Optional
from .core import PubMedFetcher, Paper
from .models import Author

class PubMedAPI:
    """Main API interface for PubMed paper analysis."""
    
    def __init__(self, email: str):
        """Initialize the API with NCBI email."""
        self._fetcher = PubMedFetcher(email)
    
    def search_company_papers(
        self, 
        query: str, 
        max_results: Optional[int] = None
    ) -> Iterator[Paper]:
        """
        Search for papers with company affiliations.
        
        Args:
            query: PubMed search query
            max_results: Maximum number of results to return
            
        Returns:
            Iterator of Paper objects with company affiliations
        """
        return self._fetcher.search_papers(query, max_results)
    
    @staticmethod
    def is_company_affiliation(affiliation: str) -> bool:
        """
        Check if an affiliation is from a company.
        
        Args:
            affiliation: Author affiliation string
            
        Returns:
            True if the affiliation is from a company
        """
        author = Author(
            name="Test",
            email=None,
            affiliations=[affiliation]
        )
        return author.has_company_affiliation()
    
    @staticmethod
    def get_company_keywords() -> set[str]:
        """Get the set of keywords used to identify companies."""
        return Author._get_company_keywords()
    
    @staticmethod
    def get_academic_keywords() -> set[str]:
        """Get the set of keywords used to identify academic institutions."""
        return Author._get_academic_keywords() 