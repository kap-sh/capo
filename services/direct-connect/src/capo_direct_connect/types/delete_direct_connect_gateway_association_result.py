"""Generated from Smithy shape ``com.amazonaws.directconnect#DeleteDirectConnectGatewayAssociationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway_association


class DeleteDirectConnectGatewayAssociationResult(TypedDict, closed=True):
    direct_connect_gateway_association: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_association.DirectConnectGatewayAssociation"
    ]
    """<p>Information about the deleted association.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDirectConnectGatewayAssociationResult) -> dict:
    out: dict = {}
    if "direct_connect_gateway_association" in value:
        import capo_direct_connect.types.direct_connect_gateway_association

        out["directConnectGatewayAssociation"] = (
            capo_direct_connect.types.direct_connect_gateway_association.serialize_aws_json_1_1(
                value["direct_connect_gateway_association"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDirectConnectGatewayAssociationResult:
    out: DeleteDirectConnectGatewayAssociationResult = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayAssociation") is not None:
        import capo_direct_connect.types.direct_connect_gateway_association

        out["direct_connect_gateway_association"] = (
            capo_direct_connect.types.direct_connect_gateway_association.deserialize_aws_json_1_1(
                data["directConnectGatewayAssociation"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteDirectConnectGatewayAssociationResult) -> dict:
    out: dict = {}
    if "direct_connect_gateway_association" in value:
        import capo_direct_connect.types.direct_connect_gateway_association

        out["directConnectGatewayAssociation"] = (
            capo_direct_connect.types.direct_connect_gateway_association.serialize_cbor(
                value["direct_connect_gateway_association"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DeleteDirectConnectGatewayAssociationResult:
    out: DeleteDirectConnectGatewayAssociationResult = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayAssociation") is not None:
        import capo_direct_connect.types.direct_connect_gateway_association

        out["direct_connect_gateway_association"] = (
            capo_direct_connect.types.direct_connect_gateway_association.deserialize_cbor(
                data["directConnectGatewayAssociation"]
            )
        )
    return out
