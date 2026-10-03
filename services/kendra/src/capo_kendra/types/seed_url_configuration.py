"""Generated from Smithy shape ``com.amazonaws.kendra#SeedUrlConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.seed_url_list
    import capo_kendra.types.web_crawler_mode


class SeedUrlConfiguration(TypedDict, closed=True):
    seed_urls: "capo_kendra.types.seed_url_list.SeedUrlList"
    """<p>The list of seed or starting point URLs of the websites you want to crawl.</p> <p>The list can include a maximum of 100 seed URLs.</p>"""
    web_crawler_mode: NotRequired["capo_kendra.types.web_crawler_mode.WebCrawlerMode"]
    """<p>You can choose one of the following modes:</p> <ul> <li> <p> <code>HOST_ONLY</code>—crawl only the website host names. For example, if the seed URL is "abc.example.com", then only URLs with host name "abc.example.com" are crawled.</p> </li> <li> <p> <code>SUBDOMAINS</code>—crawl the website host names with subdomains. For example, if the seed URL is "abc.example.com", then "a.abc.example.com" and "b.abc.example.com" are also crawled.</p> </li> <li> <p> <code>EVERYTHING</code>—crawl the website host names with subdomains and other domains that the web pages link to.</p> </li> </ul> <p>The default mode is set to <code>HOST_ONLY</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SeedUrlConfiguration) -> dict:
    out: dict = {}
    import capo_kendra.types.seed_url_list

    out["SeedUrls"] = capo_kendra.types.seed_url_list.serialize_aws_json_1_1(
        value["seed_urls"]
    )
    if "web_crawler_mode" in value:
        import capo_kendra.types.web_crawler_mode

        out["WebCrawlerMode"] = (
            capo_kendra.types.web_crawler_mode.serialize_aws_json_1_1(
                value["web_crawler_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SeedUrlConfiguration:
    out: SeedUrlConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SeedUrls") is not None:
        import capo_kendra.types.seed_url_list

        out["seed_urls"] = capo_kendra.types.seed_url_list.deserialize_aws_json_1_1(
            data["SeedUrls"]
        )
    else:
        raise DeserializationError("SeedUrlConfiguration.seed_urls required")
    if data.get("WebCrawlerMode") is not None:
        import capo_kendra.types.web_crawler_mode

        out["web_crawler_mode"] = (
            capo_kendra.types.web_crawler_mode.deserialize_aws_json_1_1(
                data["WebCrawlerMode"]
            )
        )
    return out
