"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#AmazonMachineImageOperatingSystem``."""

from typing_extensions import NotRequired, TypedDict


class AmazonMachineImageOperatingSystem(TypedDict, closed=True):
    operating_system_family_name: "str"
    """<p>The operating system family, such as Linux or Windows.</p>"""
    operating_system_name: "str"
    """<p>The specific operating system name, such as Amazon Linux 2 or Windows Server 2022.</p>"""
    operating_system_version: NotRequired["str"]
    """<p>The version of the operating system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonMachineImageOperatingSystem) -> dict:
    out: dict = {}
    out["operatingSystemFamilyName"] = value["operating_system_family_name"]
    out["operatingSystemName"] = value["operating_system_name"]
    if "operating_system_version" in value:
        out["operatingSystemVersion"] = value["operating_system_version"]
    return out


def deserialize_json(data: dict) -> AmazonMachineImageOperatingSystem:
    out: AmazonMachineImageOperatingSystem = {}  # type: ignore[typeddict-item]
    if data.get("operatingSystemFamilyName") is not None:
        out["operating_system_family_name"] = data["operatingSystemFamilyName"]
    else:
        out["operating_system_family_name"] = ""
    if data.get("operatingSystemName") is not None:
        out["operating_system_name"] = data["operatingSystemName"]
    else:
        out["operating_system_name"] = ""
    if data.get("operatingSystemVersion") is not None:
        out["operating_system_version"] = data["operatingSystemVersion"]
    return out
