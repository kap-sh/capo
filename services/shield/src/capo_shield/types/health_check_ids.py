"""Generated from Smithy shape ``com.amazonaws.shield#HealthCheckIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.health_check_id

HealthCheckIds: TypeAlias = list["capo_shield.types.health_check_id.HealthCheckId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HealthCheckIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> HealthCheckIds:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HealthCheckIds) -> list:
    return list(value)


def deserialize_cbor(data: list) -> HealthCheckIds:
    return [item for item in data if item is not None]
