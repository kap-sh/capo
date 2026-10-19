"""Generated from Smithy shape ``com.amazonaws.glue#ListCrawlsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.crawls_filter_list
    import capo_glue.types.name_string
    import capo_glue.types.page_size
    import capo_glue.types.token


class ListCrawlsRequest(TypedDict, closed=True):
    crawler_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the crawler whose runs you want to retrieve.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum number of results to return. The default is 20, and maximum is 100.</p>"""
    filters: NotRequired["capo_glue.types.crawls_filter_list.CrawlsFilterList"]
    """<p>Filters the crawls by the criteria you specify in a list of <code>CrawlsFilter</code> objects.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCrawlsRequest) -> dict:
    out: dict = {}
    out["CrawlerName"] = value["crawler_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import capo_glue.types.crawls_filter_list

        out["Filters"] = capo_glue.types.crawls_filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCrawlsRequest:
    out: ListCrawlsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CrawlerName") is not None:
        out["crawler_name"] = data["CrawlerName"]
    else:
        out["crawler_name"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Filters") is not None:
        import capo_glue.types.crawls_filter_list

        out["filters"] = capo_glue.types.crawls_filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
