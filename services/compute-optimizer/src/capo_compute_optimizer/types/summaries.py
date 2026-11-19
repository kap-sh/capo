"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Summaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.summary

Summaries: TypeAlias = list["capo_compute_optimizer.types.summary.Summary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Summaries) -> list:
    import capo_compute_optimizer.types.summary

    out: list = []
    for item in value:
        out.append(capo_compute_optimizer.types.summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Summaries:
    import capo_compute_optimizer.types.summary

    out: Summaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_compute_optimizer.types.summary.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Summaries) -> list:
    import capo_compute_optimizer.types.summary

    out: list = []
    for item in value:
        out.append(capo_compute_optimizer.types.summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Summaries:
    import capo_compute_optimizer.types.summary

    out: Summaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_compute_optimizer.types.summary.deserialize_cbor(item))
    return out
