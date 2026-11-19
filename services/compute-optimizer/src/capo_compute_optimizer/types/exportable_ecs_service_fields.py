"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableECSServiceFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.exportable_ecs_service_field

ExportableECSServiceFields: TypeAlias = list[
    "capo_compute_optimizer.types.exportable_ecs_service_field.ExportableECSServiceField"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableECSServiceFields) -> list:
    import capo_compute_optimizer.types.exportable_ecs_service_field

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.exportable_ecs_service_field.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExportableECSServiceFields:
    import capo_compute_optimizer.types.exportable_ecs_service_field

    out: ExportableECSServiceFields = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.exportable_ecs_service_field.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportableECSServiceFields) -> list:
    import capo_compute_optimizer.types.exportable_ecs_service_field

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.exportable_ecs_service_field.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> ExportableECSServiceFields:
    import capo_compute_optimizer.types.exportable_ecs_service_field

    out: ExportableECSServiceFields = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.exportable_ecs_service_field.deserialize_cbor(
                item
            )
        )
    return out
