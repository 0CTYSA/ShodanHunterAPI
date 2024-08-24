# Shodan Hunter

This script interacts with the Shodan API to retrieve information about hosts, host searches, and DNS operations.

## Installation

1. Clone the repository.
2. Install the dependencies with `pip install -r requirements.txt`.

## Usage

To run the script with arguments, you can use it in command-line mode. Example:

```bash
python shodan_t.py /shodan/host/ 8.8.8.8
```

### Commands and Parameters

- `/shodan/host/{ip}`:

  - `ip`: IP address of the host.
  - `history` (optional): True if all historical banners should be returned (default: False).
  - `minify` (optional): True to return only the list of ports and general host information without banners (default: False).

- `/shodan/host/search`:

  - `query`: Search query in Shodan.
  - `facets` (optional): Comma-separated list of properties to get summary information.
  - `page` (optional): Page number to paginate results 100 at a time (default: 1).
  - `minify` (optional): True or False; whether to truncate some of the larger fields (default: True).

- `/dns/resolve`:

  - `hostnames`: Comma-separated list of hostnames; e.g., "google.com,bing.com".

- `/dns/domain/{domain}`:

  - `domain`: Domain name to query; e.g., "cnn.com".
  - `history` (optional): True if historical DNS data should be included in the results (default: False).
  - `type` (optional): DNS type, possible values are: A, AAAA, CNAME, NS, SOA, MX, TXT.
  - `page` (optional): Page number to paginate results 100 at a time (default: 1).

- `/dns/reverse`:
  - `ips`: Comma-separated list of IP addresses; e.g., "74.125.227.230,204.79.197.200".

## Shodan API Documentation

This script uses the Shodan API. You can find more information about the API in the [official Shodan documentation](https://developer.shodan.io/api).
