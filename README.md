# app_shorter

This is a simple URL shortening service built with Flask. It provides three main routes for shortening URLs, redirecting shortened URLs, and getting statistics about shortened URLs.

# Usage
## Installation

Clone the repository:

```

git clone https://github.com/Karmendes/app_shorter.git

```
## Running with docker compose

Make sure you have docker and docker compose installed. Its will run Flask Service and Postgres Service

```

docker-compose up -d

```

# Routes

POST /shorten

Shortens a URL. The request body should have the following format:

```

{
    "url": "https://www.example.com/",
    "shortcode": "ex123"
}

```

When no shortcode is provided, it creates a random shortcode for the provided URL. The shortcode has a length of 6 characters and will contain only alphanumeric characters or underscores.

Returns HTTP status 201 with the following body:

```

{
    "shortcode": "ex123"
}


```


GET /<shortcode>
Redirects to the original URL associated with the provided shortcode.

Returns HTTP status 302 with the Location header containing the original URL.

GET /<shortcode>/stats
Gets statistics for a specific shortcode.

Returns HTTP status 200 with the following body:

```

{
    "created": "2017-05-10T20:45:00.000Z",
    "lastRedirect": "2018-05-16T10:16:24.666Z",
    "redirectCount": 6
}

```

created contains the creation datetime of the shortcode (in ISO8601).

lastRedirect contains the datetime of the last usage of the shortcode (in ISO8601).

redirectCount indicates the number of times the shortcode has been used.

# Tests

For to assure about unit tests, can you use below

```

pip install pytest
pytest

```

There is a call.py script for testing responses purposes, for use it, just run below on root directory

```
pip install requests 
python call.py

```