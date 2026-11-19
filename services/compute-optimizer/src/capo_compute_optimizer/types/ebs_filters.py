"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EBSFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.ebs_filter

EBSFilters: TypeAlias = list["capo_compute_optimizer.types.ebs_filter.EBSFilter"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EBSFilters) -> list:
    import capo_compute_optimizer.types.ebs_filter

    out: list = []
    for item in value:
        out.append(capo_compute_optimizer.types.ebs_filter.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> EBSFilters:
    import capo_compute_optimizer.types.ebs_filter

    out: EBSFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.ebs_filter.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EBSFilters) -> list:
    import capo_compute_optimizer.types.ebs_filter

    out: list = []
    for item in value:
        out.append(capo_compute_optimizer.types.ebs_filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EBSFilters:
    import capo_compute_optimizer.types.ebs_filter

    out: EBSFilters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_compute_optimizer.types.ebs_filter.deserialize_cbor(item))
    return out
