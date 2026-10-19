"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetWorkUnitsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.get_work_units_request_query_id_string
    import capo_lakeformation.types.token


class GetWorkUnitsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_lakeformation.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""
    page_size: NotRequired["int"]
    """<p>The size of each page to get in the Amazon Web Services service call. This does not affect the number of items returned in the command's output. Setting a smaller page size results in more calls to the Amazon Web Services service, retrieving fewer items in each call. This can help prevent the Amazon Web Services service calls from timing out.</p>"""
    query_id: "capo_lakeformation.types.get_work_units_request_query_id_string.GetWorkUnitsRequestQueryIdString"
    """<p>The ID of the plan query operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkUnitsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    out["QueryId"] = value["query_id"]
    return out


def deserialize_json(data: dict) -> GetWorkUnitsRequest:
    out: GetWorkUnitsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    if data.get("QueryId") is not None:
        out["query_id"] = data["QueryId"]
    else:
        out["query_id"] = ""
    return out
