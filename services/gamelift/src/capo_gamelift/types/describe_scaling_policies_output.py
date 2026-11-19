"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeScalingPoliciesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.scaling_policy_list


class DescribeScalingPoliciesOutput(TypedDict, closed=True):
    scaling_policies: NotRequired[
        "capo_gamelift.types.scaling_policy_list.ScalingPolicyList"
    ]
    """<p>A collection of objects containing the scaling policies matching the request.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeScalingPoliciesOutput) -> dict:
    out: dict = {}
    if "scaling_policies" in value:
        import capo_gamelift.types.scaling_policy_list

        out["ScalingPolicies"] = (
            capo_gamelift.types.scaling_policy_list.serialize_aws_json_1_1(
                value["scaling_policies"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeScalingPoliciesOutput:
    out: DescribeScalingPoliciesOutput = {}  # type: ignore[typeddict-item]
    if data.get("ScalingPolicies") is not None:
        import capo_gamelift.types.scaling_policy_list

        out["scaling_policies"] = (
            capo_gamelift.types.scaling_policy_list.deserialize_aws_json_1_1(
                data["ScalingPolicies"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeScalingPoliciesOutput) -> dict:
    out: dict = {}
    if "scaling_policies" in value:
        import capo_gamelift.types.scaling_policy_list

        out["ScalingPolicies"] = capo_gamelift.types.scaling_policy_list.serialize_cbor(
            value["scaling_policies"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeScalingPoliciesOutput:
    out: DescribeScalingPoliciesOutput = {}  # type: ignore[typeddict-item]
    if data.get("ScalingPolicies") is not None:
        import capo_gamelift.types.scaling_policy_list

        out["scaling_policies"] = (
            capo_gamelift.types.scaling_policy_list.deserialize_cbor(
                data["ScalingPolicies"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
