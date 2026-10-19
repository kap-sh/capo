"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetResourceExplorerSetupInput``."""

from typing_extensions import NotRequired, TypedDict


class GetResourceExplorerSetupInput(TypedDict, closed=True):
    task_id: "str"
    """<p>The unique identifier of the setup task to retrieve status information for. This ID is returned by <code>CreateResourceExplorerSetup</code> or <code>DeleteResourceExplorerSetup</code> operations.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of Region status results to return in a single response. Valid values are between <code>1</code> and <code>100</code>.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token from a previous <code>GetResourceExplorerSetup</code> response. Use this token to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceExplorerSetupInput) -> dict:
    out: dict = {}
    out["TaskId"] = value["task_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetResourceExplorerSetupInput:
    out: GetResourceExplorerSetupInput = {}  # type: ignore[typeddict-item]
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    else:
        out["task_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
