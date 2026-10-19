"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetArchiveSearchResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.search_id


class GetArchiveSearchResultsRequest(TypedDict, closed=True):
    search_id: "capo_mailmanager.types.search_id.SearchId"
    """<p>The identifier of the completed search job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetArchiveSearchResultsRequest) -> dict:
    out: dict = {}
    out["SearchId"] = value["search_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetArchiveSearchResultsRequest:
    out: GetArchiveSearchResultsRequest = {}  # type: ignore[typeddict-item]
    if data.get("SearchId") is not None:
        out["search_id"] = data["SearchId"]
    else:
        out["search_id"] = ""
    return out
