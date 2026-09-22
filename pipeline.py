import hashlib

from db import init_db, upsert_item
from scrapers.base import Item
from scrapers.example_source import scrape as scrape_example_source


def make_dedup_hash(item: Item) -> str:
    # TODO: revisit once you know your real data shape — id + source may not
    # be unique/stable enough (or may be more than enough) for your sources.
    raw = f"{item.source}:{item.id}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def filter_items(items: list[Item]) -> list[Item]:
    """
    TODO: filter items down to what's actually relevant (per major, per
    server, keyword matching, etc.). Not invented here since it depends on
    your real data shape and niche — for now, everything passes through.
    """
    return items


def run_pipeline() -> list[Item]:
    """
    Run one full pipeline pass: scrape -> filter -> upsert new items.

    Returns the list of items that were newly inserted (for posting to Discord).
    """
    init_db()

    # TODO: as you add more scrapers, call each one and combine results here
    all_items = scrape_example_source()

    filtered_items = filter_items(all_items)

    new_items = []
    for item in filtered_items:
        dedup_hash = make_dedup_hash(item)
        was_inserted = upsert_item(
            dedup_hash=dedup_hash,
            title=item.title,
            url=item.url,
            source=item.source,
        )
        if was_inserted:
            new_items.append(item)

    return new_items
