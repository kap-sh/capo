"""Generated from Smithy shape ``com.amazonaws.proton#ListServiceInstanceProvisionedResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.empty_next_token
    import capo_proton.types.resource_name


class ListServiceInstanceProvisionedResourcesInput(TypedDict, closed=True):
    service_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service that <code>serviceInstanceName</code> is associated to.</p>"""
    service_instance_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service instance whose provisioned resources you want.</p>"""
    next_token: NotRequired["capo_proton.types.empty_next_token.EmptyNextToken"]
    """<p>A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the list of provisioned resources that was previously requested.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServiceInstanceProvisionedResourcesInput) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    out["serviceInstanceName"] = value["service_instance_name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListServiceInstanceProvisionedResourcesInput:
    out: ListServiceInstanceProvisionedResourcesInput = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        out["service_name"] = ""
    if data.get("serviceInstanceName") is not None:
        out["service_instance_name"] = data["serviceInstanceName"]
    else:
        out["service_instance_name"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
