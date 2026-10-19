"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#EksAddOnOperatingSystem``."""

from typing_extensions import TypedDict


class EksAddOnOperatingSystem(TypedDict, closed=True):
    operating_system_family_name: "str"
    """<p>The operating system family, such as Linux.</p>"""
    operating_system_name: "str"
    """<p>The specific operating system name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksAddOnOperatingSystem) -> dict:
    out: dict = {}
    out["operatingSystemFamilyName"] = value["operating_system_family_name"]
    out["operatingSystemName"] = value["operating_system_name"]
    return out


def deserialize_json(data: dict) -> EksAddOnOperatingSystem:
    out: EksAddOnOperatingSystem = {}  # type: ignore[typeddict-item]
    if data.get("operatingSystemFamilyName") is not None:
        out["operating_system_family_name"] = data["operatingSystemFamilyName"]
    else:
        out["operating_system_family_name"] = ""
    if data.get("operatingSystemName") is not None:
        out["operating_system_name"] = data["operatingSystemName"]
    else:
        out["operating_system_name"] = ""
    return out
