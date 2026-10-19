"""Generated from Smithy shape ``com.amazonaws.proton#ListServiceInstanceOutputsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.deployment_id
    import capo_proton.types.empty_next_token
    import capo_proton.types.resource_name


class ListServiceInstanceOutputsInput(TypedDict, closed=True):
    service_instance_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service instance whose outputs you want.</p>"""
    service_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service that <code>serviceInstanceName</code> is associated to.</p>"""
    next_token: NotRequired["capo_proton.types.empty_next_token.EmptyNextToken"]
    """<p>A token that indicates the location of the next output in the array of outputs, after the list of outputs that was previously requested.</p>"""
    deployment_id: NotRequired["capo_proton.types.deployment_id.DeploymentId"]
    """<p>The ID of the deployment whose outputs you want.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServiceInstanceOutputsInput) -> dict:
    out: dict = {}
    out["serviceInstanceName"] = value["service_instance_name"]
    out["serviceName"] = value["service_name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServiceInstanceOutputsInput:
    out: ListServiceInstanceOutputsInput = {}  # type: ignore[typeddict-item]
    if data.get("serviceInstanceName") is not None:
        out["service_instance_name"] = data["serviceInstanceName"]
    else:
        out["service_instance_name"] = ""
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        out["service_name"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    return out
