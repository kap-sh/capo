"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListJobsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.jobs
    import capo_device_farm.types.pagination_token


class ListJobsResult(TypedDict, closed=True):
    jobs: NotRequired["capo_device_farm.types.jobs.Jobs"]
    """<p>Information about the jobs.</p>"""
    next_token: NotRequired["capo_device_farm.types.pagination_token.PaginationToken"]
    """<p>If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListJobsResult) -> dict:
    out: dict = {}
    if "jobs" in value:
        import capo_device_farm.types.jobs

        out["jobs"] = capo_device_farm.types.jobs.serialize_aws_json_1_1(value["jobs"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListJobsResult:
    out: ListJobsResult = {}  # type: ignore[typeddict-item]
    if data.get("jobs") is not None:
        import capo_device_farm.types.jobs

        out["jobs"] = capo_device_farm.types.jobs.deserialize_aws_json_1_1(data["jobs"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListJobsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "jobs" in value:
        import capo_device_farm.types.jobs

        out["jobs"] = capo_device_farm.types.jobs.redact_sensitive(value["jobs"])
    return out
