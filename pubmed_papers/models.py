"""Data models for PubMed paper information."""

from dataclasses import dataclass
from datetime import date
from typing import List, Optional, Set


@dataclass
class Author:
    """Represents a paper author with affiliation information."""
    name: str
    email: Optional[str]
    affiliations: List[str]
    is_corresponding: bool = False
    is_non_academic: bool = False

    @staticmethod
    def _get_academic_keywords() -> Set[str]:
        """Get keywords that indicate academic/non-company affiliations."""
        return {
            'university', 'college', 'institute', 'laboratory', 'hospital',
            'clinic', 'school', 'centre', 'center', 'medical', 'health',
            'research', 'academy', 'department', 'faculty', 'foundation',
            'consortium', 'unit', 'national', 'federal', 'ministry',
            'council', 'association'
        }

    @staticmethod
    def _get_company_keywords() -> Set[str]:
        """Get keywords that indicate company affiliations."""
        return {
            'inc', 'corp', 'ltd', 'llc', 'limited', 'corporation',
            'company', 'co', 'pharmaceutical', 'pharmaceuticals',
            'pharma','pharm', 'biotech', 'therapeutics', 'biosciences',
            'technologies', 'labs', 'laboratories', 'ag', 'gmbh',
            'sa', 'bv', 'nv', 'plc'
        }

    def has_company_affiliation(self) -> bool:
        """
        Check if the author has any company affiliations.
        
        Returns True if any affiliation contains company-related keywords
        and doesn't contain academic/healthcare keywords.
        """
        academic_keywords = self._get_academic_keywords()
        company_keywords = self._get_company_keywords()
        
        for affil in self.affiliations:
            affil_lower = affil.lower()
            words = set(word.strip('.,()[]{}') for word in affil_lower.split())
            
            # Check if it has any company indicators
            has_company_keyword = any(
                keyword in words or keyword in affil_lower
                for keyword in company_keywords
            )
            
            # Check if it's not an academic/healthcare institution
            is_not_academic = not any(
                keyword in words or keyword in affil_lower
                for keyword in academic_keywords
            )
            
            if has_company_keyword and is_not_academic:
                return True
        
        return False


@dataclass
class Paper:
    """Represents a research paper from PubMed."""
    pubmed_id: str
    title: str
    publication_date: date
    authors: List[Author]

    @property
    def non_academic_authors(self) -> List[Author]:
        """Get all authors with company affiliations."""
        return [author for author in self.authors if author.has_company_affiliation()]

    @property
    def company_affiliations(self) -> List[str]:
        """Get unique company affiliations from all authors."""
        affiliations = set()
        for author in self.non_academic_authors:
            affiliations.update(
                affil for affil in author.affiliations 
                if author.has_company_affiliation()
            )
        return sorted(affiliations)

    @property
    def corresponding_author_email(self) -> Optional[str]:
        """Get the email of the corresponding author."""
        for author in self.authors:
            if author.is_corresponding and author.email:
                return author.email
        return None 