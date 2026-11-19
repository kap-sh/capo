"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Filters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.filter

Filters: TypeAlias = list["capo_compute_optimizer.types.filter.Filter"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Filters) -> list:
    import capo_compute_optimizer.types.filter

    out: list = []
    for item in value:
        out.append(capo_compute_optimizer.types.filter.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Filters:
    import capo_compute_optimizer.types.filter

    out: Filters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_compute_optimizer.types.filter.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Filters) -> list:
    import capo_compute_optimizer.types.filter

    out: list = []
    for item in value:
        out.append(capo_compute_optimizer.types.filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Filters:
    import capo_compute_optimizer.types.filter

    out: Filters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_compute_optimizer.types.filter.deserialize_cbor(item))
    return out
