"""Generated from Smithy shape ``com.amazonaws.glue#StartCrawlerScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string


class StartCrawlerScheduleRequest(TypedDict, closed=True):
    crawler_name: "capo_glue.types.name_string.NameString"
    """<p>Name of the crawler to schedule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCrawlerScheduleRequest) -> dict:
    out: dict = {}
    out["CrawlerName"] = value["crawler_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCrawlerScheduleRequest:
    out: StartCrawlerScheduleRequest = {}  # type: ignore[typeddict-item]
    if data.get("CrawlerName") is not None:
        out["crawler_name"] = data["CrawlerName"]
    else:
        out["crawler_name"] = ""
    return out
