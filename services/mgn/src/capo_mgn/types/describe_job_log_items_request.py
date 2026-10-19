"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeJobLogItemsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.job_id
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token


class DescribeJobLogItemsRequest(TypedDict, closed=True):
    job_id: "capo_mgn.types.job_id.JobID"
    """<p>Request to describe Job log job ID.</p>"""
    max_results: NotRequired["capo_mgn.types.max_results_type.MaxResultsType"]
    """<p>Request to describe Job log item maximum results.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>Request to describe Job log next token.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Request to describe Job log Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobLogItemsRequest) -> dict:
    out: dict = {}
    out["jobID"] = value["job_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
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
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    return out
