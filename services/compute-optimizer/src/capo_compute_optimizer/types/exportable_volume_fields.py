"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableVolumeFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.exportable_volume_field

ExportableVolumeFields: TypeAlias = list[
    "capo_compute_optimizer.types.exportable_volume_field.ExportableVolumeField"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableVolumeFields) -> list:
    import capo_compute_optimizer.types.exportable_volume_field

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.exportable_volume_field.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExportableVolumeFields:
    import capo_compute_optimizer.types.exportable_volume_field

    out: ExportableVolumeFields = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.exportable_volume_field.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportableVolumeFields) -> list:
    import capo_compute_optimizer.types.exportable_volume_field

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.exportable_volume_field.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ExportableVolumeFields:
    import capo_compute_optimizer.types.exportable_volume_field

    out: ExportableVolumeFields = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.exportable_volume_field.deserialize_cbor(item)
        )
    return out
