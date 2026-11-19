"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#UtilizationPreferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.utilization_preference

UtilizationPreferences: TypeAlias = list[
    "capo_compute_optimizer.types.utilization_preference.UtilizationPreference"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UtilizationPreferences) -> list:
    import capo_compute_optimizer.types.utilization_preference

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.utilization_preference.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> UtilizationPreferences:
    import capo_compute_optimizer.types.utilization_preference

    out: UtilizationPreferences = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.utilization_preference.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UtilizationPreferences) -> list:
    import capo_compute_optimizer.types.utilization_preference

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.utilization_preference.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> UtilizationPreferences:
    import capo_compute_optimizer.types.utilization_preference

    out: UtilizationPreferences = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.utilization_preference.deserialize_cbor(item)
        )
    return out
