"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.tag

Tags: TypeAlias = list["capo_compute_optimizer.types.tag.Tag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Tags) -> list:
    import capo_compute_optimizer.types.tag

    out: list = []
    for item in value:
        out.append(capo_compute_optimizer.types.tag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Tags:
    import capo_compute_optimizer.types.tag

    out: Tags = []
    for item in data:
        if item is None:
            continue
        out.append(capo_compute_optimizer.types.tag.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Tags) -> list:
    import capo_compute_optimizer.types.tag

    out: list = []
    for item in value:
        out.append(capo_compute_optimizer.types.tag.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Tags:
    import capo_compute_optimizer.types.tag

    out: Tags = []
    for item in data:
        if item is None:
            continue
        out.append(capo_compute_optimizer.types.tag.deserialize_cbor(item))
    return out
