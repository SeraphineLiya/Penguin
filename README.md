# Penguin

Discord bot skeleton: scrape a data source → dedupe against a database →
post new items to Discord (on-demand for now, scheduled later). Posts
volunteering/job listings to different servers by major.

This is a structured skeleton, not a finished bot. No real scraping,
filtering, or scheduling logic is implemented yet — see the TODOs below.

## Local setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Fill in `DISCORD_TOKEN` in `.env`, then run:

```bash
python bot.py
```

In Discord, use `!check` to manually trigger a pipeline run.

## Where to fill in the real logic

- [scrapers/example_source.py](scrapers/example_source.py) — replace `fetch()`
  and `parse()` with a real request + parsing for your actual source. Add one
  new module per source, following this shape.
- [scrapers/base.py](scrapers/base.py) — extend the `Item` dataclass once you
  know your real data shape (e.g. major, deadline, org name).
- [pipeline.py](pipeline.py) — `filter_items()` is a pass-through stub; add
  your real filter criteria there, and call any new scraper modules in
  `run_pipeline()`.
- [db.py](db.py) — add more columns to the `items` table schema once you know
  your real data shape.
- [cogs/commands.py](cogs/commands.py) — has a commented-out APScheduler job
  stub for wiring up automatic scheduled runs once `!check` works well.
