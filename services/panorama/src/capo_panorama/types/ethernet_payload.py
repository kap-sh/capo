"""Generated from Smithy shape ``com.amazonaws.panorama#EthernetPayload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.connection_type
    import capo_panorama.types.static_ip_connection_info


class EthernetPayload(TypedDict, closed=True):
    connection_type: "capo_panorama.types.connection_type.ConnectionType"
    """<p>How the device gets an IP address.</p>"""
    static_ip_connection_info: NotRequired[
        "capo_panorama.types.static_ip_connection_info.StaticIpConnectionInfo"
    ]
    """<p>Network configuration for a static IP connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EthernetPayload) -> dict:
    out: dict = {}
    out["ConnectionType"] = value["connection_type"]
    if "static_ip_connection_info" in value:
        import capo_panorama.types.static_ip_connection_info

        out["StaticIpConnectionInfo"] = (
            capo_panorama.types.static_ip_connection_info.serialize_json(
                value["static_ip_connection_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> EthernetPayload:
    out: EthernetPayload = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionType") is not None:
        out["connection_type"] = data["ConnectionType"]
    else:
        out["connection_type"] = ""
    if data.get("StaticIpConnectionInfo") is not None:
        import capo_panorama.types.static_ip_connection_info

        out["static_ip_connection_info"] = (
            capo_panorama.types.static_ip_connection_info.deserialize_json(
                data["StaticIpConnectionInfo"]
            )
        )
    return out
