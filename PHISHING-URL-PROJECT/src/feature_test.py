import ipaddress


def extract_features(url):

    # Get the part after http:// or https://
    rest = url.split("//", 1)[1]

    # Get the host/domain
    host = rest.split("/", 1)[0]

    # Remove www. because it is only a common URL prefix
    if host.startswith("www."):
        host = host[4:]

    # Rebuild the URL without www.
    if "/" in rest:
        url = (
            url.split("//", 1)[0]
            + "//"
            + host
            + "/"
            + rest.split("/", 1)[1]
        )
    else:
        url = url.split("//", 1)[0] + "//" + host

    # Count the total number of characters in the URL
    length = len(url)

    # Count dots in the URL
    dot_count = url.count(".")

    # Count hyphens in the URL
    hyphen_count = url.count("-")

    # Count digits in the URL
    digit_count = sum(c.isdigit() for c in url)

    # Check for @ symbol
    at_symbol = "@" in url

    # Estimate number of subdomains
    subdomain_count = url.count(".") - 1

    # Check whether the host is an IP address
    try:
        ipaddress.ip_address(host)
        is_ip = True
    except ValueError:
        is_ip = False

    # Check whether HTTPS is used
    is_https = url.startswith("https://")

    # Get the path part
    path = (
        "/" + url.split("//")[1].split("/", 1)[1]
        if "/" in url.split("//")[1]
        else ""
    )

    # Count path sections
    path_depth = len([x for x in path.split("/") if x])

    # Suspicious words
    suspicious_terms = [
        "login",
        "verify",
        "account",
        "secure",
        "update",
        "signin",
        "password",
        "confirm",
        "bank",
        "payment"
    ]

    # Check whether a suspicious word exists
    suspicious = any(
        term in url.lower()
        for term in suspicious_terms
    )

    # Length of the domain
    domain_length = len(host)

    # Length of the URL path
    path_length = len(path)

    # Get the query part of the URL
    query = url.split("?", 1)[1] if "?" in url else ""

    # Length of the query
    query_length = len(query)

    # Count special characters
    special_char_count = sum(
        not c.isalnum() and c not in ".:/-"
        for c in url
    )

    # Count slashes
    slash_count = url.count("/")

    # Count equals signs
    equals_count = url.count("=")

    # Return all 16 features
    return [
        length,
        dot_count,
        hyphen_count,
        digit_count,
        at_symbol,
        subdomain_count,
        is_ip,
        is_https,
        path_depth,
        suspicious,
        domain_length,
        path_length,
        query_length,
        special_char_count,
        slash_count,
        equals_count
    ]