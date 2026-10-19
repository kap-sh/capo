"""Generated from Smithy shape ``com.amazonaws.securityir#ListCaseEditsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.case_id


class ListCaseEditsRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>An optional string that, if supplied, must be copied from the output of a previous call to ListCaseEdits. When provided in this manner, the API fetches the next page of results. </p>"""
    max_results: NotRequired["int"]
    """<p>Optional element to identify how many results to obtain. There is a maximum value of 25.</p>"""
    case_id: "capo_security_ir.types.case_id.CaseId"
    """<p>Required element used with ListCaseEdits to identify the case to query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCaseEditsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListCaseEditsRequest:
    out: ListCaseEditsRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
