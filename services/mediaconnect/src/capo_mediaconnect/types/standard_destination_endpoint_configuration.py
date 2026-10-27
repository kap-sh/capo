"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StandardDestinationEndpointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_endpoint_networking_type
    import capo_mediaconnect.types.destination_endpoint_protocol
    import capo_mediaconnect.types.standard_destination_endpoint_networking_configuration
    import capo_mediaconnect.types.standard_destination_endpoint_protocol_configuration


class StandardDestinationEndpointConfiguration(TypedDict, closed=True):
    name: "str"
    """<p>The name of the destination endpoint.</p>"""
    destination_networking_configuration: "capo_mediaconnect.types.standard_destination_endpoint_networking_configuration.StandardDestinationEndpointNetworkingConfiguration"
    """<p>The networking configuration for the destination endpoint, which determines whether it is publicly accessible or in a virtual private cloud (VPC).</p>"""
    protocol_configuration: "capo_mediaconnect.types.standard_destination_endpoint_protocol_configuration.StandardDestinationEndpointProtocolConfiguration"
    """<p>The protocol configuration for the destination endpoint.</p>"""
    destination_networking_type: NotRequired[
        "capo_mediaconnect.types.destination_endpoint_networking_type.DestinationEndpointNetworkingType"
    ]
    """<p>The networking type of the destination endpoint. Valid values include the following:</p> <ul> <li> <p> <code>PUBLIC</code> – The destination endpoint is publicly accessible.</p> </li> <li> <p> <code>VPC</code> – The destination endpoint is in a virtual private cloud (VPC).</p> </li> </ul>"""
    protocol: NotRequired[
        "capo_mediaconnect.types.destination_endpoint_protocol.DestinationEndpointProtocol"
    ]
    """<p>The protocol used by the destination endpoint. Valid values include the following:</p> <ul> <li> <p> <code>RTP</code> – Real-time Transport Protocol.</p> </li> <li> <p> <code>RIST</code> – Reliable Internet Stream Transport.</p> </li> <li> <p> <code>SRT_CALLER</code> – Secure Reliable Transport (SRT) in caller mode.</p> </li> <li> <p> <code>SRT_LISTENER</code> – Secure Reliable Transport (SRT) in listener mode.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardDestinationEndpointConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_mediaconnect.types.standard_destination_endpoint_networking_configuration

    out["destinationNetworkingConfiguration"] = (
        capo_mediaconnect.types.standard_destination_endpoint_networking_configuration.serialize_json(
            value["destination_networking_configuration"]
        )
    )
    import capo_mediaconnect.types.standard_destination_endpoint_protocol_configuration

    out["protocolConfiguration"] = (
        capo_mediaconnect.types.standard_destination_endpoint_protocol_configuration.serialize_json(
            value["protocol_configuration"]
        )
    )
    if "destination_networking_type" in value:
        import capo_mediaconnect.types.destination_endpoint_networking_type

        out["destinationNetworkingType"] = (
            capo_mediaconnect.types.destination_endpoint_networking_type.serialize_json(
                value["destination_networking_type"]
            )
        )
    if "protocol" in value:
        import capo_mediaconnect.types.destination_endpoint_protocol

        out["protocol"] = (
            capo_mediaconnect.types.destination_endpoint_protocol.serialize_json(
                value["protocol"]
            )
        )
    return out


def deserialize_json(data: dict) -> StandardDestinationEndpointConfiguration:
    out: StandardDestinationEndpointConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("destinationNetworkingConfiguration") is not None:
        import capo_mediaconnect.types.standard_destination_endpoint_networking_configuration

        out["destination_networking_configuration"] = (
            capo_mediaconnect.types.standard_destination_endpoint_networking_configuration.deserialize_json(
                data["destinationNetworkingConfiguration"]
            )
        )
    else:
        out["destination_networking_configuration"] = {"$unknown": {"name": ""}}
    if data.get("protocolConfiguration") is not None:
        import capo_mediaconnect.types.standard_destination_endpoint_protocol_configuration

        out["protocol_configuration"] = (
            capo_mediaconnect.types.standard_destination_endpoint_protocol_configuration.deserialize_json(
                data["protocolConfiguration"]
            )
        )
    else:
        out["protocol_configuration"] = {"$unknown": {"name": ""}}
    if data.get("destinationNetworkingType") is not None:
        import capo_mediaconnect.types.destination_endpoint_networking_type

        out["destination_networking_type"] = (
            capo_mediaconnect.types.destination_endpoint_networking_type.deserialize_json(
                data["destinationNetworkingType"]
            )
        )
    if data.get("protocol") is not None:
        import capo_mediaconnect.types.destination_endpoint_protocol

        out["protocol"] = (
            capo_mediaconnect.types.destination_endpoint_protocol.deserialize_json(
                data["protocol"]
            )
        )
    return out
