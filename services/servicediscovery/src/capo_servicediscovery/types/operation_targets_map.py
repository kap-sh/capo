"""Generated from Smithy shape ``com.amazonaws.servicediscovery#OperationTargetsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_servicediscovery.types.operation_target_type
    import capo_servicediscovery.types.resource_id

OperationTargetsMap: TypeAlias = dict[
    "capo_servicediscovery.types.operation_target_type.OperationTargetType",
    "capo_servicediscovery.types.resource_id.ResourceId",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: OperationTargetsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_servicediscovery.types.operation_target_type

        out[
            capo_servicediscovery.types.operation_target_type.serialize_aws_json_1_1(
                key
            )
        ] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> OperationTargetsMap:
    out: OperationTargetsMap = {}
    for key, value in data.items():
        import capo_servicediscovery.types.operation_target_type

        if value is None:
            continue
        out[
            capo_servicediscovery.types.operation_target_type.deserialize_aws_json_1_1(
                key
            )
        ] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: OperationTargetsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_servicediscovery.types.operation_target_type

        out[capo_servicediscovery.types.operation_target_type.serialize_cbor(key)] = (
            value
        )
    return out


def deserialize_cbor(data: dict) -> OperationTargetsMap:
    out: OperationTargetsMap = {}
    for key, value in data.items():
        import capo_servicediscovery.types.operation_target_type

        if value is None:
            continue
        out[capo_servicediscovery.types.operation_target_type.deserialize_cbor(key)] = (
            value
        )
    return out
