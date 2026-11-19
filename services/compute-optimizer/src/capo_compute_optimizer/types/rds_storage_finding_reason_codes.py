"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSStorageFindingReasonCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.rds_storage_finding_reason_code

RDSStorageFindingReasonCodes: TypeAlias = list[
    "capo_compute_optimizer.types.rds_storage_finding_reason_code.RDSStorageFindingReasonCode"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSStorageFindingReasonCodes) -> list:
    import capo_compute_optimizer.types.rds_storage_finding_reason_code

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.rds_storage_finding_reason_code.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RDSStorageFindingReasonCodes:
    import capo_compute_optimizer.types.rds_storage_finding_reason_code

    out: RDSStorageFindingReasonCodes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.rds_storage_finding_reason_code.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RDSStorageFindingReasonCodes) -> list:
    import capo_compute_optimizer.types.rds_storage_finding_reason_code

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.rds_storage_finding_reason_code.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> RDSStorageFindingReasonCodes:
    import capo_compute_optimizer.types.rds_storage_finding_reason_code

    out: RDSStorageFindingReasonCodes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.rds_storage_finding_reason_code.deserialize_cbor(
                item
            )
        )
    return out
