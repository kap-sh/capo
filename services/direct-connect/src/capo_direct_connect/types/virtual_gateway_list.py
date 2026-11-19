"""Generated from Smithy shape ``com.amazonaws.directconnect#VirtualGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.virtual_gateway

VirtualGatewayList: TypeAlias = list[
    "capo_direct_connect.types.virtual_gateway.VirtualGateway"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VirtualGatewayList) -> list:
    import capo_direct_connect.types.virtual_gateway

    out: list = []
    for item in value:
        out.append(
            capo_direct_connect.types.virtual_gateway.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VirtualGatewayList:
    import capo_direct_connect.types.virtual_gateway

    out: VirtualGatewayList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_direct_connect.types.virtual_gateway.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VirtualGatewayList) -> list:
    import capo_direct_connect.types.virtual_gateway

    out: list = []
    for item in value:
        out.append(capo_direct_connect.types.virtual_gateway.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> VirtualGatewayList:
    import capo_direct_connect.types.virtual_gateway

    out: VirtualGatewayList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_direct_connect.types.virtual_gateway.deserialize_cbor(item))
    return out
