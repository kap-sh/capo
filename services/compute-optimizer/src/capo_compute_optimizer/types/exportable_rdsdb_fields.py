"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableRDSDBFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.exportable_rdsdb_field

ExportableRDSDBFields: TypeAlias = list[
    "capo_compute_optimizer.types.exportable_rdsdb_field.ExportableRDSDBField"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableRDSDBFields) -> list:
    import capo_compute_optimizer.types.exportable_rdsdb_field

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.exportable_rdsdb_field.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExportableRDSDBFields:
    import capo_compute_optimizer.types.exportable_rdsdb_field

    out: ExportableRDSDBFields = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.exportable_rdsdb_field.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportableRDSDBFields) -> list:
    import capo_compute_optimizer.types.exportable_rdsdb_field

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.exportable_rdsdb_field.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ExportableRDSDBFields:
    import capo_compute_optimizer.types.exportable_rdsdb_field

    out: ExportableRDSDBFields = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.exportable_rdsdb_field.deserialize_cbor(item)
        )
    return out
