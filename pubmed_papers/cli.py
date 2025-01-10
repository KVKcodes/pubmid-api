"""Command-line interface for PubMed papers tool."""

import logging
import sys
from pathlib import Path
from typing import Optional
import click

from rich.console import Console
from rich.logging import RichHandler
from rich.progress import Progress, SpinnerColumn, TextColumn

from . import __version__
from .core import PubMedFetcher, create_output_dataframe

# Initialize console
console = Console()

def setup_logging(debug: bool) -> None:
    """Configure logging with appropriate level and formatting."""
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(message)s",
        handlers=[RichHandler(rich_tracebacks=True)]
    )

def ensure_file_path(file_path: Optional[str]) -> Optional[Path]:
    """Convert string path to Path object and ensure directory exists."""
    if not file_path:
        return None
    try:
        path = Path(str(file_path))  # Convert to string first to handle any path-like object
        path.parent.mkdir(parents=True, exist_ok=True)
        return path
    except Exception as e:
        raise click.BadParameter(f"Invalid file path: {e}")

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('query')
@click.option('--file', '-f', help="Output CSV file path. If not provided, prints to console")
@click.option('--debug', '-d', is_flag=True, help="Enable debug logging")
@click.option('--test', '-t', is_flag=True, help="Test mode: only fetch first 10 papers")
@click.option('--email', default="pubmed.papers@example.com",
              help="Email to use for NCBI API (required by their terms of service)")
def main(query: str, file: Optional[str], debug: bool, test: bool, email: str) -> None:
    """
    Fetch research papers from PubMed and identify those with company affiliations.
    
    The search uses PubMed's query syntax and returns papers that have at least
    one author affiliated with a pharmaceutical or biotech company.
    """
    # Setup logging
    setup_logging(debug)
    logger = logging.getLogger(__name__)
    
    try:
        # Initialize fetcher
        fetcher = PubMedFetcher(email)

        # Show progress while fetching
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task_desc = "Fetching papers from PubMed (test mode - first 10 papers)..." if test else "Fetching papers from PubMed..."
            task = progress.add_task(task_desc, total=None)
            
            logger.debug(f"Search query: {query}")
            papers = list(fetcher.search_papers(query, max_results=10 if test else None))

        # Create DataFrame (will be empty if no papers found)
        df = create_output_dataframe(papers)

        # Convert file path if provided
        output_path = ensure_file_path(file) if file else None

        if df.empty:
            console.print("[yellow]No papers found with company affiliations.[/yellow]")
            if output_path:  # Still create the empty CSV if requested
                df.to_csv(output_path, index=False)
                console.print(f"[yellow]Empty results file created at {output_path}[/yellow]")
            sys.exit(0)

        # Output results
        if output_path:
            df.to_csv(output_path, index=False)
            console.print(f"[green]Results saved to {output_path} ({len(df)} papers found)[/green]")
        else:
            console.print(df.to_string())
            console.print(f"\n[green]Found {len(df)} papers with company affiliations[/green]")

    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=debug)
        sys.exit(1)

if __name__ == "__main__":
    main() 