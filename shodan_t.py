import shodan
import os
import json
import click

# Reemplaza 'Your_Shodan_API_Key_Here' con tu clave de API de Shodan
api_key = 'Key'
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
@click.option('-o', '--output', default='results.json', help='El nombre del archivo donde guardar los resultados. Por defecto es "results.json".')
def main(endpoint, value, output):
    """Shodan Hunter
    ---------------
    Este script interactúa con la API de Shodan para obtener información sobre hosts, búsqueda de hosts, y operaciones DNS.
    
    /shodan/host/{ip}: Retorna todos los servicios encontrados en la IP del host proporcionada. 
    Parámetros:
    - ip: [String] Dirección IP del host.
    - history (opcional): [Boolean] Verdadero si se deben retornar todos los banners históricos (predeterminado: Falso).
    - minify (opcional): [Boolean] Verdadero para solo retornar la lista de puertos y la información general del host, sin banners (predeterminado: Falso).
    
    /shodan/host/search: Busca en Shodan usando la misma sintaxis de consulta que en el sitio web y utiliza facets para obtener información resumida de diferentes propiedades.
    Parámetros:
    - query: [String] Consulta de búsqueda en Shodan.
    - facets (opcional): [String] Lista separada por comas de propiedades para obtener información resumida.
    - page (opcional): [Integer] Número de página para paginar resultados 100 a la vez (predeterminado: 1).
    - minify (opcional): [Boolean] Verdadero o Falso; si truncar o no algunos de los campos más grandes (predeterminado: Verdadero).
    
    /dns/resolve: Busca la dirección IP para la lista proporcionada de nombres de host.
    Parámetros:
    - hostnames: [String] Lista de nombres de host separados por comas; ejemplo "google.com,bing.com".
    
    /dns/domain/{domain}: Obtiene todos los subdominios y otras entradas DNS para el dominio dado.
    Parámetros:
    - domain: [String] Nombre de dominio a consultar; ejemplo "cnn.com".
    - history (opcional): [Boolean] Verdadero si se debe incluir datos DNS históricos en los resultados (predeterminado: Falso).
    - type (opcional): [String] Tipo de DNS, los valores posibles son: A, AAAA, CNAME, NS, SOA, MX, TXT.
    - page (opcional): [Integer] Número de página para paginar resultados 100 a la vez (predeterminado: 1).
    
    /dns/reverse: Busca los nombres de host que se han definido para la lista proporcionada de direcciones IP.
    Parámetros:
    - ips: [String] Lista de direcciones IP separadas por comas; ejemplo "74.125.227.230,204.79.197.200".
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