"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway_association

DirectConnectGatewayAssociationList: TypeAlias = list[
    "capo_direct_connect.types.direct_connect_gateway_association.DirectConnectGatewayAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectConnectGatewayAssociationList) -> list:
    import capo_direct_connect.types.direct_connect_gateway_association

    out: list = []
    for item in value:
        out.append(
            capo_direct_connect.types.direct_connect_gateway_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DirectConnectGatewayAssociationList:
    import capo_direct_connect.types.direct_connect_gateway_association

    out: DirectConnectGatewayAssociationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_direct_connect.types.direct_connect_gateway_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectConnectGatewayAssociationList) -> list:
    import capo_direct_connect.types.direct_connect_gateway_association

    out: list = []
    for item in value:
        out.append(
            capo_direct_connect.types.direct_connect_gateway_association.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> DirectConnectGatewayAssociationList:
    import capo_direct_connect.types.direct_connect_gateway_association

    out: DirectConnectGatewayAssociationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_direct_connect.types.direct_connect_gateway_association.deserialize_cbor(
                item
            )
        )
    return out
