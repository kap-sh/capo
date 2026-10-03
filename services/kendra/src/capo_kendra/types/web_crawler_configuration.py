"""Generated from Smithy shape ``com.amazonaws.kendra#WebCrawlerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.authentication_configuration
    import capo_kendra.types.crawl_depth
    import capo_kendra.types.data_source_inclusions_exclusions_strings
    import capo_kendra.types.max_content_size_per_page_in_mega_bytes
    import capo_kendra.types.max_links_per_page
    import capo_kendra.types.max_urls_per_minute_crawl_rate
    import capo_kendra.types.proxy_configuration
    import capo_kendra.types.urls


class WebCrawlerConfiguration(TypedDict, closed=True):
    urls: "capo_kendra.types.urls.Urls"
    """<p>Specifies the seed or starting point URLs of the websites or the sitemap URLs of the websites you want to crawl.</p> <p>You can include website subdomains. You can list up to 100 seed URLs and up to three sitemap URLs.</p> <p>You can only crawl websites that use the secure communication protocol, Hypertext Transfer Protocol Secure (HTTPS). If you receive an error when crawling a website, it could be that the website is blocked from crawling.</p> <p> <i>When selecting websites to index, you must adhere to the <a href="https://aws.amazon.com/aup/">Amazon Acceptable Use Policy</a> and all other Amazon terms. Remember that you must only use Amazon Kendra Web Crawler to index your own web pages, or web pages that you have authorization to index.</i> </p>"""
    crawl_depth: NotRequired["capo_kendra.types.crawl_depth.CrawlDepth"]
    """<p>The 'depth' or number of levels from the seed level to crawl. For example, the seed URL page is depth 1 and any hyperlinks on this page that are also crawled are depth 2.</p>"""
    max_links_per_page: NotRequired[
        "capo_kendra.types.max_links_per_page.MaxLinksPerPage"
    ]
    """<p>The maximum number of URLs on a web page to include when crawling a website. This number is per web page.</p> <p>As a website’s web pages are crawled, any URLs the web pages link to are also crawled. URLs on a web page are crawled in order of appearance.</p> <p>The default maximum links per page is 100.</p>"""
    max_content_size_per_page_in_mega_bytes: NotRequired[
        "capo_kendra.types.max_content_size_per_page_in_mega_bytes.MaxContentSizePerPageInMegaBytes"
    ]
    """<p>The maximum size (in MB) of a web page or attachment to crawl.</p> <p>Files larger than this size (in MB) are skipped/not crawled.</p> <p>The default maximum size of a web page or attachment is set to 50 MB.</p>"""
    max_urls_per_minute_crawl_rate: NotRequired[
        "capo_kendra.types.max_urls_per_minute_crawl_rate.MaxUrlsPerMinuteCrawlRate"
    ]
    """<p>The maximum number of URLs crawled per website host per minute.</p> <p>A minimum of one URL is required.</p> <p>The default maximum number of URLs crawled per website host per minute is 300.</p>"""
    url_inclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to include certain URLs to crawl. URLs that match the patterns are included in the index. URLs that don't match the patterns are excluded from the index. If a URL matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the URL file isn't included in the index.</p>"""
    url_exclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to exclude certain URLs to crawl. URLs that match the patterns are excluded from the index. URLs that don't match the patterns are included in the index. If a URL matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the URL file isn't included in the index.</p>"""
    proxy_configuration: NotRequired[
        "capo_kendra.types.proxy_configuration.ProxyConfiguration"
    ]
    """<p>Configuration information required to connect to your internal websites via a web proxy.</p> <p>You must provide the website host name and port number. For example, the host name of https://a.example.com/page1.html is "a.example.com" and the port is 443, the standard port for HTTPS.</p> <p>Web proxy credentials are optional and you can use them to connect to a web proxy server that requires basic authentication. To store web proxy credentials, you use a secret in <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html">Secrets Manager</a>.</p>"""
    authentication_configuration: NotRequired[
        "capo_kendra.types.authentication_configuration.AuthenticationConfiguration"
    ]
    """<p>Configuration information required to connect to websites using authentication.</p> <p>You can connect to websites using basic authentication of user name and password. You use a secret in <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html">Secrets Manager</a> to store your authentication credentials.</p> <p>You must provide the website host name and port number. For example, the host name of https://a.example.com/page1.html is "a.example.com" and the port is 443, the standard port for HTTPS.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebCrawlerConfiguration) -> dict:
    out: dict = {}
    import capo_kendra.types.urls

    out["Urls"] = capo_kendra.types.urls.serialize_aws_json_1_1(value["urls"])
    if "crawl_depth" in value:
        out["CrawlDepth"] = value["crawl_depth"]
    if "max_links_per_page" in value:
        out["MaxLinksPerPage"] = value["max_links_per_page"]
    if "max_content_size_per_page_in_mega_bytes" in value:
        out["MaxContentSizePerPageInMegaBytes"] = (
            "NaN"
            if value["max_content_size_per_page_in_mega_bytes"]
            != value["max_content_size_per_page_in_mega_bytes"]
            else "Infinity"
            if value["max_content_size_per_page_in_mega_bytes"] == float("inf")
            else "-Infinity"
            if value["max_content_size_per_page_in_mega_bytes"] == float("-inf")
            else value["max_content_size_per_page_in_mega_bytes"]
        )
    if "max_urls_per_minute_crawl_rate" in value:
        out["MaxUrlsPerMinuteCrawlRate"] = value["max_urls_per_minute_crawl_rate"]
    if "url_inclusion_patterns" in value:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["UrlInclusionPatterns"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.serialize_aws_json_1_1(
                value["url_inclusion_patterns"]
            )
        )
    if "url_exclusion_patterns" in value:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["UrlExclusionPatterns"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.serialize_aws_json_1_1(
                value["url_exclusion_patterns"]
            )
        )
    if "proxy_configuration" in value:
        import capo_kendra.types.proxy_configuration

        out["ProxyConfiguration"] = (
            capo_kendra.types.proxy_configuration.serialize_aws_json_1_1(
                value["proxy_configuration"]
            )
        )
    if "authentication_configuration" in value:
        import capo_kendra.types.authentication_configuration

        out["AuthenticationConfiguration"] = (
            capo_kendra.types.authentication_configuration.serialize_aws_json_1_1(
                value["authentication_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WebCrawlerConfiguration:
    out: WebCrawlerConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Urls") is not None:
        import capo_kendra.types.urls

        out["urls"] = capo_kendra.types.urls.deserialize_aws_json_1_1(data["Urls"])
    else:
        raise DeserializationError("WebCrawlerConfiguration.urls required")
    if data.get("CrawlDepth") is not None:
        out["crawl_depth"] = data["CrawlDepth"]
    if data.get("MaxLinksPerPage") is not None:
        out["max_links_per_page"] = data["MaxLinksPerPage"]
    if data.get("MaxContentSizePerPageInMegaBytes") is not None:
        out["max_content_size_per_page_in_mega_bytes"] = float(
            data["MaxContentSizePerPageInMegaBytes"]
        )
    if data.get("MaxUrlsPerMinuteCrawlRate") is not None:
        out["max_urls_per_minute_crawl_rate"] = data["MaxUrlsPerMinuteCrawlRate"]
    if data.get("UrlInclusionPatterns") is not None:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["url_inclusion_patterns"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.deserialize_aws_json_1_1(
                data["UrlInclusionPatterns"]
            )
        )
    if data.get("UrlExclusionPatterns") is not None:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["url_exclusion_patterns"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.deserialize_aws_json_1_1(
                data["UrlExclusionPatterns"]
            )
        )
    if data.get("ProxyConfiguration") is not None:
        import capo_kendra.types.proxy_configuration

        out["proxy_configuration"] = (
            capo_kendra.types.proxy_configuration.deserialize_aws_json_1_1(
                data["ProxyConfiguration"]
            )
        )
    if data.get("AuthenticationConfiguration") is not None:
        import capo_kendra.types.authentication_configuration

        out["authentication_configuration"] = (
            capo_kendra.types.authentication_configuration.deserialize_aws_json_1_1(
                data["AuthenticationConfiguration"]
            )
        )
    return out
