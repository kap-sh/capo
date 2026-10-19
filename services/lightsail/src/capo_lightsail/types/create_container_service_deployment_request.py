"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateContainerServiceDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.container_map
    import capo_lightsail.types.container_service_name
    import capo_lightsail.types.endpoint_request


class CreateContainerServiceDeploymentRequest(TypedDict, closed=True):
    service_name: "capo_lightsail.types.container_service_name.ContainerServiceName"
    """<p>The name of the container service for which to create the deployment.</p>"""
    containers: NotRequired["capo_lightsail.types.container_map.ContainerMap"]
    """<p>An object that describes the settings of the containers that will be launched on the container service.</p>"""
    public_endpoint: NotRequired[
        "capo_lightsail.types.endpoint_request.EndpointRequest"
    ]
    """<p>An object that describes the settings of the public endpoint for the container service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContainerServiceDeploymentRequest) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    if "containers" in value:
        import capo_lightsail.types.container_map

        out["containers"] = capo_lightsail.types.container_map.serialize_aws_json_1_1(
            value["containers"]
        )
    if "public_endpoint" in value:
        import capo_lightsail.types.endpoint_request

        out["publicEndpoint"] = (
            capo_lightsail.types.endpoint_request.serialize_aws_json_1_1(
                value["public_endpoint"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContainerServiceDeploymentRequest:
    out: CreateContainerServiceDeploymentRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        out["service_name"] = ""
    if data.get("containers") is not None:
        import capo_lightsail.types.container_map

        out["containers"] = capo_lightsail.types.container_map.deserialize_aws_json_1_1(
            data["containers"]
        )
    if data.get("publicEndpoint") is not None:
        import capo_lightsail.types.endpoint_request

        out["public_endpoint"] = (
            capo_lightsail.types.endpoint_request.deserialize_aws_json_1_1(
                data["publicEndpoint"]
            )
        )
    return out
