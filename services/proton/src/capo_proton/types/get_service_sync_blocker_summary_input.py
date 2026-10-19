"""Generated from Smithy shape ``com.amazonaws.proton#GetServiceSyncBlockerSummaryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.resource_name


class GetServiceSyncBlockerSummaryInput(TypedDict, closed=True):
    service_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service that you want to get the service sync blocker summary for. If given only the service name, all instances are blocked.</p>"""
    service_instance_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of the service instance that you want to get the service sync blocker summary for. If given bothe the instance name and the service name, only the instance is blocked.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetServiceSyncBlockerSummaryInput) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    if "service_instance_name" in value:
        out["serviceInstanceName"] = value["service_instance_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetServiceSyncBlockerSummaryInput:
    out: GetServiceSyncBlockerSummaryInput = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        out["service_name"] = ""
    if data.get("serviceInstanceName") is not None:
        out["service_instance_name"] = data["serviceInstanceName"]
    return out
