"""Generated from Smithy shape ``com.amazonaws.lightsail#AttachInstancesToLoadBalancerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.resource_name_list


class AttachInstancesToLoadBalancerRequest(TypedDict, closed=True):
    load_balancer_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the load balancer.</p>"""
    instance_names: "capo_lightsail.types.resource_name_list.ResourceNameList"
    """<p>An array of strings representing the instance name(s) you want to attach to your load balancer.</p> <p>An instance must be <code>running</code> before you can attach it to your load balancer.</p> <p>There are no additional limits on the number of instances you can attach to your load balancer, aside from the limit of Lightsail instances you can create in your account (20).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachInstancesToLoadBalancerRequest) -> dict:
    out: dict = {}
    out["loadBalancerName"] = value["load_balancer_name"]
    import capo_lightsail.types.resource_name_list

    out["instanceNames"] = (
        capo_lightsail.types.resource_name_list.serialize_aws_json_1_1(
            value["instance_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachInstancesToLoadBalancerRequest:
    out: AttachInstancesToLoadBalancerRequest = {}  # type: ignore[typeddict-item]
    if data.get("loadBalancerName") is not None:
        out["load_balancer_name"] = data["loadBalancerName"]
    else:
        out["load_balancer_name"] = ""
    if data.get("instanceNames") is not None:
        import capo_lightsail.types.resource_name_list

        out["instance_names"] = (
            capo_lightsail.types.resource_name_list.deserialize_aws_json_1_1(
                data["instanceNames"]
            )
        )
    else:
        out["instance_names"] = []
    return out
