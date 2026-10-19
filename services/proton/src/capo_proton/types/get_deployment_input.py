"""Generated from Smithy shape ``com.amazonaws.proton#GetDeploymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.deployment_id
    import capo_proton.types.resource_name


class GetDeploymentInput(TypedDict, closed=True):
    id: "capo_proton.types.deployment_id.DeploymentId"
    """<p>The ID of the deployment that you want to get the detailed data for.</p>"""
    environment_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of a environment that you want to get the detailed data for.</p>"""
    service_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of the service associated with the given deployment ID.</p>"""
    service_instance_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of the service instance associated with the given deployment ID. <code>serviceName</code> must be specified to identify the service instance.</p>"""
    component_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of a component that you want to get the detailed data for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDeploymentInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "environment_name" in value:
        out["environmentName"] = value["environment_name"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_instance_name" in value:
        out["serviceInstanceName"] = value["service_instance_name"]
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDeploymentInput:
    out: GetDeploymentInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("serviceInstanceName") is not None:
        out["service_instance_name"] = data["serviceInstanceName"]
    if data.get("componentName") is not None:
        out["component_name"] = data["componentName"]
    return out
