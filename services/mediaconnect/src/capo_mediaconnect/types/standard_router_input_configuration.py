"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StandardRouterInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_protocol
    import capo_mediaconnect.types.router_input_protocol_configuration
    import capo_mediaconnect.types.router_network_interface_arn


class StandardRouterInputConfiguration(TypedDict, closed=True):
    network_interface_arn: (
        "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the network interface associated with the standard router input.</p>"""
    protocol_configuration: "capo_mediaconnect.types.router_input_protocol_configuration.RouterInputProtocolConfiguration"
    """<p>The configuration settings for the protocol used by the standard router input.</p>"""
    protocol: NotRequired[
        "capo_mediaconnect.types.router_input_protocol.RouterInputProtocol"
    ]
    """<p>The protocol used by the standard router input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardRouterInputConfiguration) -> dict:
    out: dict = {}
    out["networkInterfaceArn"] = value["network_interface_arn"]
    import capo_mediaconnect.types.router_input_protocol_configuration

    out["protocolConfiguration"] = (
        capo_mediaconnect.types.router_input_protocol_configuration.serialize_json(
            value["protocol_configuration"]
        )
    )
    if "protocol" in value:
        import capo_mediaconnect.types.router_input_protocol

        out["protocol"] = capo_mediaconnect.types.router_input_protocol.serialize_json(
            value["protocol"]
        )
    return out


def deserialize_json(data: dict) -> StandardRouterInputConfiguration:
    out: StandardRouterInputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("networkInterfaceArn") is not None:
        out["network_interface_arn"] = data["networkInterfaceArn"]
    else:
        out["network_interface_arn"] = ""
    if data.get("protocolConfiguration") is not None:
        import capo_mediaconnect.types.router_input_protocol_configuration

        out["protocol_configuration"] = (
            capo_mediaconnect.types.router_input_protocol_configuration.deserialize_json(
                data["protocolConfiguration"]
            )
        )
    else:
        import capo_mediaconnect.types._unknown

        out["protocol_configuration"] = (
            capo_mediaconnect.types._unknown.UnknownUnionMember("")
        )
    if data.get("protocol") is not None:
        import capo_mediaconnect.types.router_input_protocol

        out["protocol"] = (
            capo_mediaconnect.types.router_input_protocol.deserialize_json(
                data["protocol"]
            )
        )
    return out
