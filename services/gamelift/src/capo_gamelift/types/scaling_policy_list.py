"""Generated from Smithy shape ``com.amazonaws.gamelift#ScalingPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.scaling_policy

ScalingPolicyList: TypeAlias = list["capo_gamelift.types.scaling_policy.ScalingPolicy"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPolicyList) -> list:
    import capo_gamelift.types.scaling_policy

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.scaling_policy.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ScalingPolicyList:
    import capo_gamelift.types.scaling_policy

    out: ScalingPolicyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.scaling_policy.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScalingPolicyList) -> list:
    import capo_gamelift.types.scaling_policy

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.scaling_policy.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ScalingPolicyList:
    import capo_gamelift.types.scaling_policy

    out: ScalingPolicyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.scaling_policy.deserialize_cbor(item))
    return out
