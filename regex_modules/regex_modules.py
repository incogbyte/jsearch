
REGEX_PATT = {
    "AMAZON_URL":r"https?://[^\"\\'> ]+",
    "AMAZON_URL_1":r"[a-z0-9.-]+\.s3-[a-z0-9-]\\.amazonaws\.com",
    "AMAZON_URL_2":r"[a-z0-9.-]+\.s3-website[.-](eu|ap|us|ca|sa|cn)",
    "AMAZON_URL_3":r"s3\\.amazonaws\.com/[a-z0-9._-]+",
    "AMAZON_URL_4":r"s3-[a-z0-9-]+\.amazonaws\\.com/[a-z0-9._-]+",
    "URLS":r"https?://[^\"\\'> ]+",
    "AMAZON_KEY":r"([^A-Z0-9]|^)(AKIA|A3T|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{12,}",
    "UPLOAD_FIELDS":r"\u003cinput[^\u003e]+type=[\"']?file[\"']?"
}