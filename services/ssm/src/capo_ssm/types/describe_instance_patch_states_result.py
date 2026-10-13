"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeInstancePatchStatesResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.instance_patch_state_list
    import capo_ssm.types.next_token


class DescribeInstancePatchStatesResult(TypedDict, closed=True):
    instance_patch_states: NotRequired[
        "capo_ssm.types.instance_patch_state_list.InstancePatchStateList"
    ]
    """<p>The high-level patch state for the requested managed nodes.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstancePatchStatesResult) -> dict:
    out: dict = {}
    if "instance_patch_states" in value:
        import capo_ssm.types.instance_patch_state_list

        out["InstancePatchStates"] = (
            capo_ssm.types.instance_patch_state_list.serialize_aws_json_1_1(
                value["instance_patch_states"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInstancePatchStatesResult:
    out: DescribeInstancePatchStatesResult = {}  # type: ignore[typeddict-item]
    if data.get("InstancePatchStates") is not None:
        import capo_ssm.types.instance_patch_state_list

        out["instance_patch_states"] = (
            capo_ssm.types.instance_patch_state_list.deserialize_aws_json_1_1(
                data["InstancePatchStates"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeInstancePatchStatesResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "instance_patch_states" in value:
        import capo_ssm.types.instance_patch_state_list

        out["instance_patch_states"] = (
            capo_ssm.types.instance_patch_state_list.redact_sensitive(
                value["instance_patch_states"]
            )
        )
    return out
