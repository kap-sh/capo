"""Generated from Smithy shape ``com.amazonaws.mailmanager#PolicyConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.policy_condition

PolicyConditions: TypeAlias = list[
    "capo_mailmanager.types.policy_condition.PolicyCondition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyConditions) -> list:
    import capo_mailmanager.types.policy_condition

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.policy_condition.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> PolicyConditions:
    import capo_mailmanager.types.policy_condition

    out: PolicyConditions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mailmanager.types.policy_condition.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PolicyConditions) -> list:
    import capo_mailmanager.types.policy_condition

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.policy_condition.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> PolicyConditions:
    import capo_mailmanager.types.policy_condition

    out: PolicyConditions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mailmanager.types.policy_condition.deserialize_cbor(item))
    return out
