"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableIdleFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.exportable_idle_field

ExportableIdleFields: TypeAlias = list[
    "capo_compute_optimizer.types.exportable_idle_field.ExportableIdleField"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableIdleFields) -> list:
    import capo_compute_optimizer.types.exportable_idle_field

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.exportable_idle_field.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExportableIdleFields:
    import capo_compute_optimizer.types.exportable_idle_field

    out: ExportableIdleFields = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.exportable_idle_field.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportableIdleFields) -> list:
    import capo_compute_optimizer.types.exportable_idle_field

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.exportable_idle_field.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ExportableIdleFields:
    import capo_compute_optimizer.types.exportable_idle_field

    out: ExportableIdleFields = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.exportable_idle_field.deserialize_cbor(item)
        )
    return out
