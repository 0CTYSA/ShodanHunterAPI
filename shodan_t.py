import shodan
import os
import json
import click

# Replace 'Your_Shodan_API_Key_Here' with your actual Shodan API key
api_key = 'Your_Shodan_API_Key_Here'
api = shodan.Shodan(api_key)

def save_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(content, file, ensure_ascii=False, indent=4)

def get_file_name(value):
    return f'{value}.json'

def host_info(ip):
    try:
        result = api.host(ip)
        save_to_file(get_file_name(ip), result)
    except shodan.APIError as e:
        save_to_file(get_file_name(ip), {'error': str(e)})


def host_search(query):
    try:
        results = api.search(query)
        save_to_file(get_file_name(query), results)
    except shodan.APIError as e:
        save_to_file(get_file_name(query), {'error': str(e)})

def dns_resolve(names):
    try:
        result = api.dns_resolve(names)
        save_to_file(get_file_name(names), result)
    except shodan.APIError as e:
        save_to_file(get_file_name(names), {'error': str(e)})

def dns_domain_info(domain):
    try:
        result = api.dns_domain_info(domain)
        save_to_file(get_file_name(domain), result)
    except shodan.APIError as e:
        save_to_file(get_file_name(domain), {'error': str(e)})

def dns_reverse(ips):
    try:
        result = api.dns_reverse(ips)
        save_to_file(get_file_name(ips), result)
    except shodan.APIError as e:
        save_to_file(get_file_name(ips), {'error': str(e)})

@click.command()
@click.argument('endpoint', type=click.Choice(['/shodan/host/', '/shodan/host/search', '/dns/resolve', '/dns/domain/', '/dns/reverse']))
@click.argument('value')
@click.option('-o', '--output', default='results.json', help='The name of the file where results will be saved. The default is "results.json".')
def main(endpoint, value, output):
    """Shodan Hunter
    ---------------
    This script interacts with the Shodan API to retrieve information about hosts, host searches, and DNS operations.
    
    /shodan/host/{ip}: Returns all services found on the provided host IP address. 
    Parameters:
    - ip: [String] IP address of the host.
    - history (optional): [Boolean] True to return all historical banners (default: False).
    - minify (optional): [Boolean] True to return only the list of ports and general host information, without banners (default: False).
    
    /shodan/host/search: Searches Shodan using the same query syntax as the website and uses facets to get summary information on different properties.
    Parameters:
    - query: [String] Search query in Shodan.
    - facets (optional): [String] Comma-separated list of properties to get summary information.
    - page (optional): [Integer] Page number to paginate results 100 at a time (default: 1).
    - minify (optional): [Boolean] True or False; whether to truncate some of the larger fields (default: True).
    
    /dns/resolve: Looks up the IP address for the provided list of hostnames.
    Parameters:
    - hostnames: [String] Comma-separated list of hostnames; e.g., "google.com,bing.com".
    
    /dns/domain/{domain}: Retrieves all subdomains and other DNS entries for the given domain.
    Parameters:
    - domain: [String] Domain name to query; e.g., "cnn.com".
    - history (optional): [Boolean] True if historical DNS data should be included in the results (default: False).
    - type (optional): [String] DNS type, possible values are: A, AAAA, CNAME, NS, SOA, MX, TXT.
    - page (optional): [Integer] Page number to paginate results 100 at a time (default: 1).
    
    /dns/reverse: Looks up the hostnames that have been set for the provided list of IP addresses.
    Parameters:
    - ips: [String] Comma-separated list of IP addresses; e.g., "74.125.227.230,204.79.197.200".
    """
    output_filename = get_file_name(value) if output == 'results.json' else output

    if endpoint == '/shodan/host/':
        host_info(value)
    elif endpoint == '/shodan/host/search':
        host_search(value)
    elif endpoint == '/dns/resolve':
        dns_resolve(value)
    elif endpoint == '/dns/domain/':
        dns_domain_info(value)
    elif endpoint == '/dns/reverse':
        dns_reverse(value)

    click.echo(f'Results saved to: {os.path.abspath(output_filename)}')

if __name__ == "__main__":
    main()
