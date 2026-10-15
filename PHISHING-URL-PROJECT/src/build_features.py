import pandas as pd
import ipaddress


# ---------------- FEATURE EXTRACTION ----------------

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

    # Count total URL characters
    length = len(url)

    # Count dots
    dot_count = url.count(".")

    # Count hyphens
    hyphen_count = url.count("-")

    # Count digits
    digit_count = sum(c.isdigit() for c in url)

    # Check for @ symbol
    at_symbol = "@" in url

    # Check if host is an IP address
    try:
        ipaddress.ip_address(host)
        is_ip = True
    except ValueError:
        is_ip = False

    # Check if HTTPS is used
    is_https = url.startswith("https://")

    # Estimate subdomains
    subdomain_count = url.count(".") - 1

    # Get path
    path = (
        "/" + url.split("//")[1].split("/", 1)[1]
        if "/" in url.split("//")[1]
        else ""
    )

    # Path depth
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

    # Check for suspicious words
    suspicious = any(
        term in url.lower()
        for term in suspicious_terms
    )

    # ---------------- NEW FEATURES ----------------

    # Length of the domain
    domain_length = len(host)

    # Length of the path
    path_length = len(path)

    # Get the URL query parameters
    query = url.split("?", 1)[1] if "?" in url else ""

    # Length of query parameters
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


# ---------------- LOAD DATASET ----------------

df = pd.read_csv("../datasets/PhiUSIIL_Phishing_URL_Dataset.csv")

print("Dataset loaded")
print("Number of rows:", len(df))


# ---------------- BUILD FEATURES FOR ALL URLs ----------------

feature_rows = []

for url in df["URL"]:
    features = extract_features(url)
    feature_rows.append(features)

print("Number of feature rows:", len(feature_rows))


# Create column names for our 16 features
feature_names = [
    "URLLength",
    "DotCount",
    "HyphenCount",
    "DigitCount",
    "AtSymbol",
    "SubdomainCount",
    "IsIP",
    "IsHTTPS",
    "PathDepth",
    "SuspiciousTerms",
    "DomainLength",
    "PathLength",
    "QueryLength",
    "SpecialCharCount",
    "SlashCount",
    "EqualsCount"
]


# Create a new table from our extracted features
features_df = pd.DataFrame(
    feature_rows,
    columns=feature_names
)


# Add the original label
features_df["label"] = df["label"].values


print(features_df.head())


# Save the processed feature dataset
features_df.to_csv(
    "../datasets/processed_features.csv",
    index=False
)

print("Processed dataset saved")