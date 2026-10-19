"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#NetworkInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.interface_name
    import capo_migrationhubstrategy.types.ip_address
    import capo_migrationhubstrategy.types.mac_address
    import capo_migrationhubstrategy.types.net_mask


class NetworkInfo(TypedDict, closed=True):
    interface_name: "capo_migrationhubstrategy.types.interface_name.InterfaceName"
    """<p> Information about the name of the interface of the server for which the assessment was run. </p>"""
    ip_address: "capo_migrationhubstrategy.types.ip_address.IPAddress"
    """<p> Information about the IP address of the server for which the assessment was run. </p>"""
    mac_address: "capo_migrationhubstrategy.types.mac_address.MacAddress"
    """<p> Information about the MAC address of the server for which the assessment was run. </p>"""
    net_mask: "capo_migrationhubstrategy.types.net_mask.NetMask"
    """<p> Information about the subnet mask of the server for which the assessment was run. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInfo) -> dict:
    out: dict = {}
    out["interfaceName"] = value["interface_name"]
    out["ipAddress"] = value["ip_address"]
    out["macAddress"] = value["mac_address"]
    out["netMask"] = value["net_mask"]
    return out


def deserialize_json(data: dict) -> NetworkInfo:
    out: NetworkInfo = {}  # type: ignore[typeddict-item]
    if data.get("interfaceName") is not None:
        out["interface_name"] = data["interfaceName"]
    else:
        out["interface_name"] = ""
    if data.get("ipAddress") is not None:
        out["ip_address"] = data["ipAddress"]
    else:
        out["ip_address"] = ""
    if data.get("macAddress") is not None:
        out["mac_address"] = data["macAddress"]
    else:
        out["mac_address"] = ""
    if data.get("netMask") is not None:
        out["net_mask"] = data["netMask"]
    else:
        out["net_mask"] = ""
    return out
