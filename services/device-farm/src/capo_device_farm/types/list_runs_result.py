"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListRunsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.pagination_token
    import capo_device_farm.types.runs


class ListRunsResult(TypedDict, closed=True):
    runs: NotRequired["capo_device_farm.types.runs.Runs"]
    """<p>Information about the runs.</p>"""
    next_token: NotRequired["capo_device_farm.types.pagination_token.PaginationToken"]
    """<p>If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRunsResult) -> dict:
    out: dict = {}
    if "runs" in value:
        import capo_device_farm.types.runs

        out["runs"] = capo_device_farm.types.runs.serialize_aws_json_1_1(value["runs"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRunsResult:
    out: ListRunsResult = {}  # type: ignore[typeddict-item]
    if data.get("runs") is not None:
        import capo_device_farm.types.runs

        out["runs"] = capo_device_farm.types.runs.deserialize_aws_json_1_1(data["runs"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListRunsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "runs" in value:
        import capo_device_farm.types.runs

        out["runs"] = capo_device_farm.types.runs.redact_sensitive(value["runs"])
    return out
