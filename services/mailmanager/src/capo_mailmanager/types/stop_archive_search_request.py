"""Generated from Smithy shape ``com.amazonaws.mailmanager#StopArchiveSearchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.search_id


class StopArchiveSearchRequest(TypedDict, closed=True):
    search_id: "capo_mailmanager.types.search_id.SearchId"
    """<p>The identifier of the search job to stop.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopArchiveSearchRequest) -> dict:
    out: dict = {}
    out["SearchId"] = value["search_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StopArchiveSearchRequest:
    out: StopArchiveSearchRequest = {}  # type: ignore[typeddict-item]
    if data.get("SearchId") is not None:
        out["search_id"] = data["SearchId"]
    else:
        out["search_id"] = ""
    return out
