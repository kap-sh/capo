"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#AwsSupportedService``."""

from typing_extensions import TypedDict


class AwsSupportedService(TypedDict, closed=True):
    supported_service_type: "str"
    """<p>The machine-readable identifier of the supported service.</p>"""
    display_name: "str"
    """<p>The human-readable name of the supported service.</p>"""
    description: "str"
    """<p>A description of the supported service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsSupportedService) -> dict:
    out: dict = {}
    out["supportedServiceType"] = value["supported_service_type"]
    out["displayName"] = value["display_name"]
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AwsSupportedService:
    out: AwsSupportedService = {}  # type: ignore[typeddict-item]
    if data.get("supportedServiceType") is not None:
        out["supported_service_type"] = data["supportedServiceType"]
    else:
        out["supported_service_type"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    return out
