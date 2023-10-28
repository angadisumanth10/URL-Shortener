# Python URL Shortener

A simple URL shortener implemented in Python. This project allows you to create shortened versions of long URLs programmatically.

## Features

- Shorten long URLs into concise and memorable links.
- Retrieve original URLs from shortened links.
- Customizable short link formats and characters.
- Statistics tracking for each shortened URL (clicks, creation date, etc.).

## Usage

To use this URL shortener in your Python application, follow these simple steps:

1. Clone this repository to your project directory.
2. Import the `url_shortener` module.
3. Call the relevant functions to shorten and expand URLs within your code.

Example usage:

```python
import url_shortener

# Shorten a URL
short_url = url_shortener.shorten_url("https://example.com")

# Expand a short URL
original_url = url_shortener.expand_url(short_url)
