"""Generated from Smithy shape ``com.amazonaws.proton#GetServiceInstanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_proton.types.resource_name


class GetServiceInstanceInput(TypedDict, closed=True):
    name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of a service instance that you want to get the detailed data for.</p>"""
    service_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service that you want the service instance input for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetServiceInstanceInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["serviceName"] = value["service_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetServiceInstanceInput:
    out: GetServiceInstanceInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        out["service_name"] = ""
    return out
