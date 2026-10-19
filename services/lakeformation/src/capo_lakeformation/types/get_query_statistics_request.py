"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetQueryStatisticsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.get_query_statistics_request_query_id_string


class GetQueryStatisticsRequest(TypedDict, closed=True):
    query_id: "capo_lakeformation.types.get_query_statistics_request_query_id_string.GetQueryStatisticsRequestQueryIdString"
    """<p>The ID of the plan query operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryStatisticsRequest) -> dict:
    out: dict = {}
    out["QueryId"] = value["query_id"]
    return out


def deserialize_json(data: dict) -> GetQueryStatisticsRequest:
    out: GetQueryStatisticsRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueryId") is not None:
        out["query_id"] = data["QueryId"]
    else:
        out["query_id"] = ""
    return out
