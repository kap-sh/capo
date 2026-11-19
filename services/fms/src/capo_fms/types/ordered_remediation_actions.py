"""Generated from Smithy shape ``com.amazonaws.fms#OrderedRemediationActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.remediation_action_with_order

OrderedRemediationActions: TypeAlias = list[
    "capo_fms.types.remediation_action_with_order.RemediationActionWithOrder"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrderedRemediationActions) -> list:
    import capo_fms.types.remediation_action_with_order

    out: list = []
    for item in value:
        out.append(
            capo_fms.types.remediation_action_with_order.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrderedRemediationActions:
    import capo_fms.types.remediation_action_with_order

    out: OrderedRemediationActions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_fms.types.remediation_action_with_order.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrderedRemediationActions) -> list:
    import capo_fms.types.remediation_action_with_order

    out: list = []
    for item in value:
        out.append(capo_fms.types.remediation_action_with_order.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> OrderedRemediationActions:
    import capo_fms.types.remediation_action_with_order

    out: OrderedRemediationActions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.remediation_action_with_order.deserialize_cbor(item))
    return out
