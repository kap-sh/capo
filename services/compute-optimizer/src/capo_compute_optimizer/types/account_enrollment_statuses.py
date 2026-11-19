"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AccountEnrollmentStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_enrollment_status

AccountEnrollmentStatuses: TypeAlias = list[
    "capo_compute_optimizer.types.account_enrollment_status.AccountEnrollmentStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountEnrollmentStatuses) -> list:
    import capo_compute_optimizer.types.account_enrollment_status

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.account_enrollment_status.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AccountEnrollmentStatuses:
    import capo_compute_optimizer.types.account_enrollment_status

    out: AccountEnrollmentStatuses = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.account_enrollment_status.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccountEnrollmentStatuses) -> list:
    import capo_compute_optimizer.types.account_enrollment_status

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.account_enrollment_status.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> AccountEnrollmentStatuses:
    import capo_compute_optimizer.types.account_enrollment_status

    out: AccountEnrollmentStatuses = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.account_enrollment_status.deserialize_cbor(
                item
            )
        )
    return out
