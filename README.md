# Hacker News Scraper

A beginner-friendly Python web scraping project that extracts live news headlines, article links, and post scores from Hacker News using BeautifulSoup and Requests.

This project was built to practice real-world web scraping concepts such as inspecting HTML structure, identifying repeating containers, extracting text and attributes, and working with loops in Python.

## Features

* Scrapes latest Hacker News posts
* Extracts:

  * News headlines
  * Article links
  * Post scores/points
* Uses BeautifulSoup for HTML parsing
* Uses Requests for fetching webpage data
* Demonstrates real-world scraping workflow

## Technologies Used

* Python
* BeautifulSoup4
* Requests

## Concepts Practiced

* HTTP requests
* HTML inspection
* Parsing webpage content
* `find()` and `find_all()`
* Extracting attributes (`href`)
* Looping through scraped data
* Handling nested HTML tags

## Example Output

```text
Valve releases Steam Controller CAD files under Creative Commons license
Link: https://www.digitalfoundry.net/news/...

1208 points
------------------------------
```

## Future Improvements

* Save scraped data to CSV
* Add pagination support
* Sort posts by score
* Export data to JSON
* Build a simple GUI or web interface

## Purpose

This project was created as part of learning Python automation and web scraping fundamentals before moving toward more advanced backend and AI-related development.
