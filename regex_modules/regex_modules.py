
REGEX_PATT = {
    "AMAZON_URL":r"https?://[^\"\\'> ]+",
    "AMAZON_URL_1":r"[a-z0-9.-]+\.s3-[a-z0-9-]\\.amazonaws\.com",
    "AMAZON_URL_2":r"[a-z0-9.-]+\.s3-website[.-](eu|ap|us|ca|sa|cn)",
    "AMAZON_URL_3":r"s3\\.amazonaws\.com/[a-z0-9._-]+",
    "AMAZON_URL_4":r"s3-[a-z0-9-]+\.amazonaws\\.com/[a-z0-9._-]+",
    "URLS":r"https?://[^\"\\'> ]+",
    "AMAZON_KEY":r"([^A-Z0-9]|^)(AKIA|A3T|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{12,}",
    "Authorization":r"^Bearer\s[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$",
    "accessToken":r"^acesstoken=[0-9]{13,17}",
    "vtex-key":r"vtex-api-(appkey|apptoken)",
    "email":r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    
}
