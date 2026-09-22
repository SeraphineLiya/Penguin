"""
Stub scraper showing the expected shape: fetch -> parse -> return list[Item].

This module is a placeholder. It does not hit a real data source.
Copy this file's shape for each real source you add (one module per source).
"""

from datetime import datetime, timezone

from scrapers.base import Item

SOURCE_NAME = "example_source"
FAKE_URL = "https://example.invalid/fake-listings"  # not a real endpoint


def fetch():
    """
    Fetch raw data from the source.

    TODO: replace this with a real request, e.g.:
        response = requests.get(FAKE_URL, timeout=10)
        response.raise_for_status()
        return response.json()  # or response.text for HTML

    For now this returns fake in-memory data so the pipeline can run end to end.
    """
    return [
        {"id": "fake-1", "title": "Fake Listing 1", "url": f"{FAKE_URL}/1"},
        {"id": "fake-2", "title": "Fake Listing 2", "url": f"{FAKE_URL}/2"},
    ]


def parse(raw_data) -> list[Item]:
    """
    Turn raw fetched data into a list of Item objects.

    TODO: replace this with real parsing logic once you know the actual
    response shape (JSON keys, or HTML structure if using BeautifulSoup).
    """
    items = []
    for entry in raw_data:
        items.append(
            Item(
                id=entry["id"],
                title=entry["title"],
                url=entry["url"],
                source=SOURCE_NAME,
                created_at=datetime.now(timezone.utc),
            )
        )
    return items


def scrape() -> list[Item]:
    """Entry point called by the pipeline."""
    raw_data = fetch()
    return parse(raw_data)
