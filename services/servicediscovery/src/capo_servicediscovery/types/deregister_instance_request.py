"""Generated from Smithy shape ``com.amazonaws.servicediscovery#DeregisterInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.arn
    import capo_servicediscovery.types.resource_id


class DeregisterInstanceRequest(TypedDict, closed=True):
    service_id: "capo_servicediscovery.types.arn.Arn"
    """<p>The ID or Amazon Resource Name (ARN) of the service that the instance is associated with. If the namespace associated with the service is shared with your account, specify the service ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""
    instance_id: "capo_servicediscovery.types.resource_id.ResourceId"
    """<p>The value that you specified for <code>Id</code> in the <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html">RegisterInstance</a> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterInstanceRequest) -> dict:
    out: dict = {}
    out["ServiceId"] = value["service_id"]
    out["InstanceId"] = value["instance_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterInstanceRequest:
    out: DeregisterInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceId") is not None:
        out["service_id"] = data["ServiceId"]
    else:
        raise DeserializationError("DeregisterInstanceRequest.service_id required")
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("DeregisterInstanceRequest.instance_id required")
    return out
