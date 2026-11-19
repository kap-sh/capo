"""Generated from Smithy shape ``com.amazonaws.directconnect#AvailablePortSpeeds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.port_speed

AvailablePortSpeeds: TypeAlias = list["capo_direct_connect.types.port_speed.PortSpeed"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailablePortSpeeds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AvailablePortSpeeds:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AvailablePortSpeeds) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AvailablePortSpeeds:
    return [item for item in data if item is not None]
