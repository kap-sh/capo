"""Generated from Smithy shape ``com.amazonaws.drs#DescribeJobsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.jobs_list
    import capo_drs.types.pagination_token


class DescribeJobsResponse(TypedDict, closed=True):
    items: NotRequired["capo_drs.types.jobs_list.JobsList"]
    """<p>An array of Jobs.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next Job to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_drs.types.jobs_list

        out["items"] = capo_drs.types.jobs_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeJobsResponse:
    out: DescribeJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_drs.types.jobs_list

        out["items"] = capo_drs.types.jobs_list.deserialize_json(data["items"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: DescribeJobsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_drs.types.jobs_list

        out["items"] = capo_drs.types.jobs_list.redact_sensitive(value["items"])
    return out
