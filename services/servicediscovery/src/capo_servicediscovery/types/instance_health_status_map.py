"""Generated from Smithy shape ``com.amazonaws.servicediscovery#InstanceHealthStatusMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_servicediscovery.types.health_status
    import capo_servicediscovery.types.resource_id

InstanceHealthStatusMap: TypeAlias = dict[
    "capo_servicediscovery.types.resource_id.ResourceId",
    "capo_servicediscovery.types.health_status.HealthStatus",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: InstanceHealthStatusMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_servicediscovery.types.health_status

        out[key] = capo_servicediscovery.types.health_status.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceHealthStatusMap:
    out: InstanceHealthStatusMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_servicediscovery.types.health_status

        out[key] = capo_servicediscovery.types.health_status.deserialize_aws_json_1_1(
            value
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: InstanceHealthStatusMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_servicediscovery.types.health_status

        out[key] = capo_servicediscovery.types.health_status.serialize_cbor(value)
    return out


def deserialize_cbor(data: dict) -> InstanceHealthStatusMap:
    out: InstanceHealthStatusMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_servicediscovery.types.health_status

        out[key] = capo_servicediscovery.types.health_status.deserialize_cbor(value)
    return out
