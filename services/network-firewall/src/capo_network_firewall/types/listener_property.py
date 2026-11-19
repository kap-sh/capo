"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListenerProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.listener_property_type
    import capo_network_firewall.types.nat_gateway_port


class ListenerProperty(TypedDict, closed=True):
    port: NotRequired["capo_network_firewall.types.nat_gateway_port.NatGatewayPort"]
    """<p>Port for processing traffic.</p>"""
    type: NotRequired[
        "capo_network_firewall.types.listener_property_type.ListenerPropertyType"
    ]
    """<p>Selection of HTTP or HTTPS traffic.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListenerProperty) -> dict:
    out: dict = {}
    if "port" in value:
        out["Port"] = value["port"]
    if "type" in value:
        import capo_network_firewall.types.listener_property_type

        out["Type"] = (
            capo_network_firewall.types.listener_property_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListenerProperty:
    out: ListenerProperty = {}  # type: ignore[typeddict-item]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("Type") is not None:
        import capo_network_firewall.types.listener_property_type

        out["type"] = (
            capo_network_firewall.types.listener_property_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListenerProperty) -> dict:
    out: dict = {}
    if "port" in value:
        out["Port"] = value["port"]
    if "type" in value:
        import capo_network_firewall.types.listener_property_type

        out["Type"] = capo_network_firewall.types.listener_property_type.serialize_cbor(
            value["type"]
        )
    return out


def deserialize_cbor(data: dict) -> ListenerProperty:
    out: ListenerProperty = {}  # type: ignore[typeddict-item]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("Type") is not None:
        import capo_network_firewall.types.listener_property_type

        out["type"] = (
            capo_network_firewall.types.listener_property_type.deserialize_cbor(
                data["Type"]
            )
        )
    return out
