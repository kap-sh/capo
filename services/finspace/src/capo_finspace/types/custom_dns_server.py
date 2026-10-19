"""Generated from Smithy shape ``com.amazonaws.finspace#CustomDNSServer``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.valid_hostname
    import capo_finspace.types.valid_ip_address


class CustomDNSServer(TypedDict, closed=True):
    custom_dns_server_name: "capo_finspace.types.valid_hostname.ValidHostname"
    """<p>The name of the DNS server.</p>"""
    custom_dns_server_ip: "capo_finspace.types.valid_ip_address.ValidIPAddress"
    """<p>The IP address of the DNS server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomDNSServer) -> dict:
    out: dict = {}
    out["customDNSServerName"] = value["custom_dns_server_name"]
    out["customDNSServerIP"] = value["custom_dns_server_ip"]
    return out


def deserialize_json(data: dict) -> CustomDNSServer:
    out: CustomDNSServer = {}  # type: ignore[typeddict-item]
    if data.get("customDNSServerName") is not None:
        out["custom_dns_server_name"] = data["customDNSServerName"]
    else:
        out["custom_dns_server_name"] = ""
    if data.get("customDNSServerIP") is not None:
        out["custom_dns_server_ip"] = data["customDNSServerIP"]
    else:
        out["custom_dns_server_ip"] = ""
    return out
