"""Generated from Smithy shape ``com.amazonaws.drs#DescribeJobLogItemsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.job_id
    import capo_drs.types.pagination_token
    import capo_drs.types.strictly_positive_integer


class DescribeJobLogItemsRequest(TypedDict, closed=True):
    job_id: "capo_drs.types.job_id.JobID"
    """<p>The ID of the Job for which Job log items will be retrieved.</p>"""
    max_results: NotRequired[
        "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
    ]
    """<p>Maximum number of Job log items to retrieve.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next Job log items to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobLogItemsRequest) -> dict:
    out: dict = {}
    out["jobID"] = value["job_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeJobLogItemsRequest:
    out: DescribeJobLogItemsRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobID") is not None:
        out["job_id"] = data["jobID"]
    else:
        out["job_id"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
