"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ReasonCodeSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.reason_code_summary

ReasonCodeSummaries: TypeAlias = list[
    "capo_compute_optimizer.types.reason_code_summary.ReasonCodeSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReasonCodeSummaries) -> list:
    import capo_compute_optimizer.types.reason_code_summary

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.reason_code_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ReasonCodeSummaries:
    import capo_compute_optimizer.types.reason_code_summary

    out: ReasonCodeSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.reason_code_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReasonCodeSummaries) -> list:
    import capo_compute_optimizer.types.reason_code_summary

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.reason_code_summary.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ReasonCodeSummaries:
    import capo_compute_optimizer.types.reason_code_summary

    out: ReasonCodeSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.reason_code_summary.deserialize_cbor(item)
        )
    return out
