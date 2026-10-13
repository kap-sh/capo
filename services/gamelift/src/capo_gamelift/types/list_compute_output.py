"""Generated from Smithy shape ``com.amazonaws.gamelift#ListComputeOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.compute_list
    import capo_gamelift.types.non_zero_and_max_string


class ListComputeOutput(TypedDict, closed=True):
    compute_list: NotRequired["capo_gamelift.types.compute_list.ComputeList"]
    """<p>A list of compute resources in the specified fleet.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListComputeOutput) -> dict:
    out: dict = {}
    if "compute_list" in value:
        import capo_gamelift.types.compute_list

        out["ComputeList"] = capo_gamelift.types.compute_list.serialize_aws_json_1_1(
            value["compute_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListComputeOutput:
    out: ListComputeOutput = {}  # type: ignore[typeddict-item]
    if data.get("ComputeList") is not None:
        import capo_gamelift.types.compute_list

        out["compute_list"] = capo_gamelift.types.compute_list.deserialize_aws_json_1_1(
            data["ComputeList"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListComputeOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "compute_list" in value:
        import capo_gamelift.types.compute_list

        out["compute_list"] = capo_gamelift.types.compute_list.redact_sensitive(
            value["compute_list"]
        )
    return out
