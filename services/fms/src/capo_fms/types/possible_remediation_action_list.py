"""Generated from Smithy shape ``com.amazonaws.fms#PossibleRemediationActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.possible_remediation_action

PossibleRemediationActionList: TypeAlias = list[
    "capo_fms.types.possible_remediation_action.PossibleRemediationAction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PossibleRemediationActionList) -> list:
    import capo_fms.types.possible_remediation_action

    out: list = []
    for item in value:
        out.append(
            capo_fms.types.possible_remediation_action.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PossibleRemediationActionList:
    import capo_fms.types.possible_remediation_action

    out: PossibleRemediationActionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_fms.types.possible_remediation_action.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PossibleRemediationActionList) -> list:
    import capo_fms.types.possible_remediation_action

    out: list = []
    for item in value:
        out.append(capo_fms.types.possible_remediation_action.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> PossibleRemediationActionList:
    import capo_fms.types.possible_remediation_action

    out: PossibleRemediationActionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.possible_remediation_action.deserialize_cbor(item))
    return out
