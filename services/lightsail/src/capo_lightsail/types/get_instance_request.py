"""Generated from Smithy shape ``com.amazonaws.lightsail#GetInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.resource_name


class GetInstanceRequest(TypedDict, closed=True):
    instance_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the instance.</p>"""
    include_health_status: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Specifies whether to include the instance health status checks in the response of your request.</p> <p>When set to <code>true</code>, the response includes the <code>instanceStatus</code> and <code>systemStatus</code> of the instance. When omitted or set to <code>false</code>, the response doesn't include them.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstanceRequest) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    if "include_health_status" in value:
        out["includeHealthStatus"] = value["include_health_status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstanceRequest:
    out: GetInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("instanceName") is not None:
        out["instance_name"] = data["instanceName"]
    else:
        out["instance_name"] = ""
    if data.get("includeHealthStatus") is not None:
        out["include_health_status"] = data["includeHealthStatus"]
    return out
