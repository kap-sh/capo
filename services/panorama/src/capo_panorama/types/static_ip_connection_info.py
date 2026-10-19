"""Generated from Smithy shape ``com.amazonaws.panorama#StaticIpConnectionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.default_gateway
    import capo_panorama.types.dns_list
    import capo_panorama.types.ip_address
    import capo_panorama.types.mask


class StaticIpConnectionInfo(TypedDict, closed=True):
    ip_address: "capo_panorama.types.ip_address.IpAddress"
    """<p>The connection's IP address.</p>"""
    mask: "capo_panorama.types.mask.Mask"
    """<p>The connection's DNS mask.</p>"""
    dns: "capo_panorama.types.dns_list.DnsList"
    """<p>The connection's DNS address.</p>"""
    default_gateway: "capo_panorama.types.default_gateway.DefaultGateway"
    """<p>The connection's default gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StaticIpConnectionInfo) -> dict:
    out: dict = {}
    out["IpAddress"] = value["ip_address"]
    out["Mask"] = value["mask"]
    import capo_panorama.types.dns_list

    out["Dns"] = capo_panorama.types.dns_list.serialize_json(value["dns"])
    out["DefaultGateway"] = value["default_gateway"]
    return out


def deserialize_json(data: dict) -> StaticIpConnectionInfo:
    out: StaticIpConnectionInfo = {}  # type: ignore[typeddict-item]
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    else:
        out["ip_address"] = ""
    if data.get("Mask") is not None:
        out["mask"] = data["Mask"]
    else:
        out["mask"] = ""
    if data.get("Dns") is not None:
        import capo_panorama.types.dns_list

        out["dns"] = capo_panorama.types.dns_list.deserialize_json(data["Dns"])
    else:
        out["dns"] = []
    if data.get("DefaultGateway") is not None:
        out["default_gateway"] = data["DefaultGateway"]
    else:
        out["default_gateway"] = ""
    return out
