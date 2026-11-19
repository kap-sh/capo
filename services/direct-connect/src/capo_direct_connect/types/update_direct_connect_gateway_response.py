"""Generated from Smithy shape ``com.amazonaws.directconnect#UpdateDirectConnectGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway


class UpdateDirectConnectGatewayResponse(TypedDict, closed=True):
    direct_connect_gateway: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway.DirectConnectGateway"
    ]
    """<p>Informaiton about a Direct Connect gateway, which enables you to connect virtual interfaces and virtual private gateways or transit gateways.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDirectConnectGatewayResponse) -> dict:
    out: dict = {}
    if "direct_connect_gateway" in value:
        import capo_direct_connect.types.direct_connect_gateway

        out["directConnectGateway"] = (
            capo_direct_connect.types.direct_connect_gateway.serialize_aws_json_1_1(
                value["direct_connect_gateway"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDirectConnectGatewayResponse:
    out: UpdateDirectConnectGatewayResponse = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGateway") is not None:
        import capo_direct_connect.types.direct_connect_gateway

        out["direct_connect_gateway"] = (
            capo_direct_connect.types.direct_connect_gateway.deserialize_aws_json_1_1(
                data["directConnectGateway"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateDirectConnectGatewayResponse) -> dict:
    out: dict = {}
    if "direct_connect_gateway" in value:
        import capo_direct_connect.types.direct_connect_gateway

        out["directConnectGateway"] = (
            capo_direct_connect.types.direct_connect_gateway.serialize_cbor(
                value["direct_connect_gateway"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateDirectConnectGatewayResponse:
    out: UpdateDirectConnectGatewayResponse = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGateway") is not None:
        import capo_direct_connect.types.direct_connect_gateway

        out["direct_connect_gateway"] = (
            capo_direct_connect.types.direct_connect_gateway.deserialize_cbor(
                data["directConnectGateway"]
            )
        )
    return out
