"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetCrawlersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.crawler_name_list


class BatchGetCrawlersRequest(TypedDict, closed=True):
    crawler_names: "capo_glue.types.crawler_name_list.CrawlerNameList"
    """<p>A list of crawler names, which might be the names returned from the <code>ListCrawlers</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetCrawlersRequest) -> dict:
    out: dict = {}
    import capo_glue.types.crawler_name_list

    out["CrawlerNames"] = capo_glue.types.crawler_name_list.serialize_aws_json_1_1(
        value["crawler_names"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetCrawlersRequest:
    out: BatchGetCrawlersRequest = {}  # type: ignore[typeddict-item]
    if data.get("CrawlerNames") is not None:
        import capo_glue.types.crawler_name_list

        out["crawler_names"] = (
            capo_glue.types.crawler_name_list.deserialize_aws_json_1_1(
                data["CrawlerNames"]
            )
        )
    else:
        out["crawler_names"] = []
    return out
