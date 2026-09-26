"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AlbConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.ip_address_type
    import capo_network_security_manager.types.scheme


class AlbConfiguration(TypedDict, closed=True):
    scheme: NotRequired["capo_network_security_manager.types.scheme.Scheme"]
    """<p>The scheme of the Application Load Balancer, either <code>internet-facing</code> or <code>internal</code>.</p>"""
    ip_address_type: NotRequired[
        "capo_network_security_manager.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type of the Application Load Balancer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlbConfiguration) -> dict:
    out: dict = {}
    if "scheme" in value:
        import capo_network_security_manager.types.scheme

        out["scheme"] = capo_network_security_manager.types.scheme.serialize_json(
            value["scheme"]
        )
    if "ip_address_type" in value:
        import capo_network_security_manager.types.ip_address_type

        out["ipAddressType"] = (
            capo_network_security_manager.types.ip_address_type.serialize_json(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> AlbConfiguration:
    out: AlbConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("scheme") is not None:
        import capo_network_security_manager.types.scheme

        out["scheme"] = capo_network_security_manager.types.scheme.deserialize_json(
            data["scheme"]
        )
    if data.get("ipAddressType") is not None:
        import capo_network_security_manager.types.ip_address_type

        out["ip_address_type"] = (
            capo_network_security_manager.types.ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    return out
