"""Generated from Smithy shape ``com.amazonaws.fms#PolicySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.policy_summary

PolicySummaryList: TypeAlias = list["capo_fms.types.policy_summary.PolicySummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicySummaryList) -> list:
    import capo_fms.types.policy_summary

    out: list = []
    for item in value:
        out.append(capo_fms.types.policy_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PolicySummaryList:
    import capo_fms.types.policy_summary

    out: PolicySummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.policy_summary.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PolicySummaryList) -> list:
    import capo_fms.types.policy_summary

    out: list = []
    for item in value:
        out.append(capo_fms.types.policy_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> PolicySummaryList:
    import capo_fms.types.policy_summary

    out: PolicySummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.policy_summary.deserialize_cbor(item))
    return out
