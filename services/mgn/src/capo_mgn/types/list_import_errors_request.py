"""Generated from Smithy shape ``com.amazonaws.mgn#ListImportErrorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.import_id
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token


class ListImportErrorsRequest(TypedDict, closed=True):
    import_id: "capo_mgn.types.import_id.ImportID"
    """<p>List import errors request import id.</p>"""
    max_results: NotRequired["capo_mgn.types.max_results_type.MaxResultsType"]
    """<p>List import errors request max results.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>List import errors request next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportErrorsRequest) -> dict:
    out: dict = {}
    out["importID"] = value["import_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImportErrorsRequest:
    out: ListImportErrorsRequest = {}  # type: ignore[typeddict-item]
    if data.get("importID") is not None:
        out["import_id"] = data["importID"]
    else:
        out["import_id"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
