"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTrafficMirrorTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.network_interface_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.vpc_endpoint_id


class CreateTrafficMirrorTargetRequest(TypedDict, closed=True):
    network_interface_id: NotRequired[
        "capo_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The network interface ID that is associated with the target.</p>"""
    network_load_balancer_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Network Load Balancer that is associated with the target.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the Traffic Mirror target.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the Traffic Mirror target.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">How to ensure idempotency</a>.</p>"""
    gateway_load_balancer_endpoint_id: NotRequired[
        "capo_ec2.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>The ID of the Gateway Load Balancer endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTrafficMirrorTargetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "network_load_balancer_arn" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkLoadBalancerArn",
                str(value["network_load_balancer_arn"]),
            )
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "gateway_load_balancer_endpoint_id" in value:
        pairs.append(
            (
                f"{key_prefix}GatewayLoadBalancerEndpointId",
                str(value["gateway_load_balancer_endpoint_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> CreateTrafficMirrorTargetRequest:
    out: CreateTrafficMirrorTargetRequest = {}  # type: ignore[typeddict-item]
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_network_load_balancer_arn = el.find("NetworkLoadBalancerArn")
    if child_network_load_balancer_arn is not None:
        out["network_load_balancer_arn"] = str(
            child_network_load_balancer_arn.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_gateway_load_balancer_endpoint_id = el.find("GatewayLoadBalancerEndpointId")
    if child_gateway_load_balancer_endpoint_id is not None:
        out["gateway_load_balancer_endpoint_id"] = str(
            child_gateway_load_balancer_endpoint_id.text or ""
        )
    return out
