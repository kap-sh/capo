"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EnrollmentFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.enrollment_filter

EnrollmentFilters: TypeAlias = list[
    "capo_compute_optimizer.types.enrollment_filter.EnrollmentFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnrollmentFilters) -> list:
    import capo_compute_optimizer.types.enrollment_filter

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.enrollment_filter.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EnrollmentFilters:
    import capo_compute_optimizer.types.enrollment_filter

    out: EnrollmentFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.enrollment_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnrollmentFilters) -> list:
    import capo_compute_optimizer.types.enrollment_filter

    out: list = []
    for item in value:
        out.append(capo_compute_optimizer.types.enrollment_filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EnrollmentFilters:
    import capo_compute_optimizer.types.enrollment_filter

    out: EnrollmentFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.enrollment_filter.deserialize_cbor(item)
        )
    return out
