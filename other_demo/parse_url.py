def parse_url_params(url: str) -> dict:
    param = {}

    # 取出?后面的字符串
    query = url.split("?", 1)[1] if "?" in url else ""

    if not query:
        return param

    for item in query.split("&"):
        key, sep, value = item.partition("=")
        param[key] = value

    return param

if __name__ == "__main__":
    url = "https://example.com/search?keyword=python&page=2&tag=AI&tag=Agent"
    print(parse_url_params(url))