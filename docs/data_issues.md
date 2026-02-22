# Rental AI – Data Issues Log

## 2026-02-22 – Initial EDA

### 1. Missing descriptions
- (How many percent?) listings have NULL description
- Root cause: some of the
listings have description only in czech.
- Action: update scrape_listings_sync.py

### 3. Missing posted_date
- Column exists but always NULL
- Root cause: not scraped
- Action: remove column until implemented
