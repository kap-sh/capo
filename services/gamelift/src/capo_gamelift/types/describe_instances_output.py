"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeInstancesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.instance_list
    import capo_gamelift.types.non_zero_and_max_string


class DescribeInstancesOutput(TypedDict, closed=True):
    instances: NotRequired["capo_gamelift.types.instance_list.InstanceList"]
    """<p>A collection of objects containing properties for each instance returned.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstancesOutput) -> dict:
    out: dict = {}
    if "instances" in value:
        import capo_gamelift.types.instance_list

        out["Instances"] = capo_gamelift.types.instance_list.serialize_aws_json_1_1(
            value["instances"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInstancesOutput:
    out: DescribeInstancesOutput = {}  # type: ignore[typeddict-item]
    if data.get("Instances") is not None:
        import capo_gamelift.types.instance_list

        out["instances"] = capo_gamelift.types.instance_list.deserialize_aws_json_1_1(
            data["Instances"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeInstancesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "instances" in value:
        import capo_gamelift.types.instance_list

        out["instances"] = capo_gamelift.types.instance_list.redact_sensitive(
            value["instances"]
        )
    return out
