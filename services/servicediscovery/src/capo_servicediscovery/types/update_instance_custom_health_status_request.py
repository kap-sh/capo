"""Generated from Smithy shape ``com.amazonaws.servicediscovery#UpdateInstanceCustomHealthStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.arn
    import capo_servicediscovery.types.custom_health_status
    import capo_servicediscovery.types.resource_id


class UpdateInstanceCustomHealthStatusRequest(TypedDict, closed=True):
    service_id: "capo_servicediscovery.types.arn.Arn"
    """<p>The ID or Amazon Resource Name (ARN) of the service that includes the configuration for the custom health check that you want to change the status for. For services created in a shared namespace, specify the service ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""
    instance_id: "capo_servicediscovery.types.resource_id.ResourceId"
    """<p>The ID of the instance that you want to change the health status for.</p>"""
    status: "capo_servicediscovery.types.custom_health_status.CustomHealthStatus"
    """<p>The new status of the instance, <code>HEALTHY</code> or <code>UNHEALTHY</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateInstanceCustomHealthStatusRequest) -> dict:
    out: dict = {}
    out["ServiceId"] = value["service_id"]
    out["InstanceId"] = value["instance_id"]
    import capo_servicediscovery.types.custom_health_status

    out["Status"] = (
        capo_servicediscovery.types.custom_health_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateInstanceCustomHealthStatusRequest:
    out: UpdateInstanceCustomHealthStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceId") is not None:
        out["service_id"] = data["ServiceId"]
    else:
        raise DeserializationError(
            "UpdateInstanceCustomHealthStatusRequest.service_id required"
        )
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "UpdateInstanceCustomHealthStatusRequest.instance_id required"
        )
    if data.get("Status") is not None:
        import capo_servicediscovery.types.custom_health_status

        out["status"] = (
            capo_servicediscovery.types.custom_health_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateInstanceCustomHealthStatusRequest.status required"
        )
    return out
