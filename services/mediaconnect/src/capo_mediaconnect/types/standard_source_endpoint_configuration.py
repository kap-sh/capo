"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StandardSourceEndpointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.source_endpoint_networking_type
    import capo_mediaconnect.types.source_endpoint_protocol
    import capo_mediaconnect.types.standard_source_endpoint_networking_configuration
    import capo_mediaconnect.types.standard_source_endpoint_protocol_configuration


class StandardSourceEndpointConfiguration(TypedDict, closed=True):
    name: "str"
    """<p>The name of the source endpoint.</p>"""
    source_networking_configuration: "capo_mediaconnect.types.standard_source_endpoint_networking_configuration.StandardSourceEndpointNetworkingConfiguration"
    """<p>The networking configuration for the source endpoint, which determines whether it is publicly accessible or in a virtual private cloud (VPC).</p>"""
    protocol_configuration: "capo_mediaconnect.types.standard_source_endpoint_protocol_configuration.StandardSourceEndpointProtocolConfiguration"
    """<p>The protocol configuration for the source endpoint.</p>"""
    source_networking_type: NotRequired[
        "capo_mediaconnect.types.source_endpoint_networking_type.SourceEndpointNetworkingType"
    ]
    """<p>The networking type of the source endpoint. Valid values include the following:</p> <ul> <li> <p> <code>PUBLIC</code> – The source endpoint is publicly accessible.</p> </li> <li> <p> <code>VPC</code> – The source endpoint is in a virtual private cloud (VPC).</p> </li> </ul>"""
    protocol: NotRequired[
        "capo_mediaconnect.types.source_endpoint_protocol.SourceEndpointProtocol"
    ]
    """<p>The protocol used by the source endpoint. Valid values include the following:</p> <ul> <li> <p> <code>RTP</code> – Real-time Transport Protocol.</p> </li> <li> <p> <code>RIST</code> – Reliable Internet Stream Transport.</p> </li> <li> <p> <code>SRT_CALLER</code> – Secure Reliable Transport (SRT) in caller mode.</p> </li> <li> <p> <code>SRT_LISTENER</code> – Secure Reliable Transport (SRT) in listener mode.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardSourceEndpointConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_mediaconnect.types.standard_source_endpoint_networking_configuration

    out["sourceNetworkingConfiguration"] = (
        capo_mediaconnect.types.standard_source_endpoint_networking_configuration.serialize_json(
            value["source_networking_configuration"]
        )
    )
    import capo_mediaconnect.types.standard_source_endpoint_protocol_configuration

    out["protocolConfiguration"] = (
        capo_mediaconnect.types.standard_source_endpoint_protocol_configuration.serialize_json(
            value["protocol_configuration"]
        )
    )
    if "source_networking_type" in value:
        import capo_mediaconnect.types.source_endpoint_networking_type

        out["sourceNetworkingType"] = (
            capo_mediaconnect.types.source_endpoint_networking_type.serialize_json(
                value["source_networking_type"]
            )
        )
    if "protocol" in value:
        import capo_mediaconnect.types.source_endpoint_protocol

        out["protocol"] = (
            capo_mediaconnect.types.source_endpoint_protocol.serialize_json(
                value["protocol"]
            )
        )
    return out


def deserialize_json(data: dict) -> StandardSourceEndpointConfiguration:
    out: StandardSourceEndpointConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("sourceNetworkingConfiguration") is not None:
        import capo_mediaconnect.types.standard_source_endpoint_networking_configuration

        out["source_networking_configuration"] = (
            capo_mediaconnect.types.standard_source_endpoint_networking_configuration.deserialize_json(
                data["sourceNetworkingConfiguration"]
            )
        )
    else:
        out["source_networking_configuration"] = {"$unknown": {"name": ""}}
    if data.get("protocolConfiguration") is not None:
        import capo_mediaconnect.types.standard_source_endpoint_protocol_configuration

        out["protocol_configuration"] = (
            capo_mediaconnect.types.standard_source_endpoint_protocol_configuration.deserialize_json(
                data["protocolConfiguration"]
            )
        )
    else:
        out["protocol_configuration"] = {"$unknown": {"name": ""}}
    if data.get("sourceNetworkingType") is not None:
        import capo_mediaconnect.types.source_endpoint_networking_type

        out["source_networking_type"] = (
            capo_mediaconnect.types.source_endpoint_networking_type.deserialize_json(
                data["sourceNetworkingType"]
            )
        )
    if data.get("protocol") is not None:
        import capo_mediaconnect.types.source_endpoint_protocol

        out["protocol"] = (
            capo_mediaconnect.types.source_endpoint_protocol.deserialize_json(
                data["protocol"]
            )
        )
    return out
