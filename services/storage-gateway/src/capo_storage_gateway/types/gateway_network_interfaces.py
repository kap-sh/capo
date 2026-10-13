"""Generated from Smithy shape ``com.amazonaws.storagegateway#GatewayNetworkInterfaces``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.network_interface

GatewayNetworkInterfaces: TypeAlias = list[
    "capo_storage_gateway.types.network_interface.NetworkInterface"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayNetworkInterfaces) -> list:
    import capo_storage_gateway.types.network_interface

    out: list = []
    for item in value:
        out.append(
            capo_storage_gateway.types.network_interface.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GatewayNetworkInterfaces:
    import capo_storage_gateway.types.network_interface

    out: GatewayNetworkInterfaces = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_storage_gateway.types.network_interface.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: GatewayNetworkInterfaces) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
