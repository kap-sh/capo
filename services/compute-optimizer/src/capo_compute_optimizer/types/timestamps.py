"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Timestamps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.timestamp

Timestamps: TypeAlias = list["capo_compute_optimizer.types.timestamp.Timestamp"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Timestamps) -> list:
    import capo_compute_optimizer.types.timestamp

    out: list = []
    for item in value:
        out.append(capo_compute_optimizer.types.timestamp.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Timestamps:
    import capo_compute_optimizer.types.timestamp

    out: Timestamps = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.timestamp.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Timestamps) -> list:
    import capo_compute_optimizer.types.timestamp

    out: list = []
    for item in value:
        out.append(capo_compute_optimizer.types.timestamp.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Timestamps:
    import capo_compute_optimizer.types.timestamp

    out: Timestamps = []
    for item in data:
        if item is None:
            continue
        out.append(capo_compute_optimizer.types.timestamp.deserialize_cbor(item))
    return out
