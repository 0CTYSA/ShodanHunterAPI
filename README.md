# Shodan Hunter

Este script interactúa con la API de Shodan para obtener información sobre hosts, búsqueda de hosts, y operaciones DNS.

## Instalación

1. Clona el repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.

## Uso

Para ejecutar el script con argumentos puedes usaarlo en modo de línea de comandos. Ejemplo:

```bash
python shodan_t.py /shodan/host/ 8.8.8.8
```

### Comandos y Parámetros

- `/shodan/host/{ip}`:

  - `ip`: Dirección IP del host.
  - `history` (opcional): Verdadero si se deben retornar todos los banners históricos (predeterminado: Falso).
  - `minify` (opcional): Verdadero para solo retornar la lista de puertos y la información general del host, sin banners (predeterminado: Falso).

- `/shodan/host/search`:

  - `query`: Consulta de búsqueda en Shodan.
  - `facets` (opcional): Lista separada por comas de propiedades para obtener información resumida.
  - `page` (opcional): Número de página para paginar resultados 100 a la vez (predeterminado: 1).
  - `minify` (opcional): Verdadero o Falso; si truncar o no algunos de los campos más grandes (predeterminado: Verdadero).

- `/dns/resolve`:

  - `hostnames`: Lista de nombres de host separados por comas; ejemplo "google.com,bing.com".

- `/dns/domain/{domain}`:

  - `domain`: Nombre de dominio a consultar; ejemplo "cnn.com".
  - `history` (opcional): Verdadero si se debe incluir datos DNS históricos en los resultados (predeterminado: Falso).
  - `type` (opcional): Tipo de DNS, los valores posibles son: A, AAAA, CNAME, NS, SOA, MX, TXT.
  - `page` (opcional): Número de página para paginar resultados 100 a la vez (predeterminado: 1).

- `/dns/reverse`:
  - `ips`: Lista de direcciones IP separadas por comas; ejemplo "74.125.227.230,204.79.197.200".

## Documentación de la API de Shodan

Este script utiliza la API de Shodan. Puedes encontrar más información sobre la API en [la documentación oficial de Shodan](https://developer.shodan.io/api).
