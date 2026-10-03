"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayAttachedAppliance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.nat_gateway_appliance_modify_state
    import capo_ec2.types.nat_gateway_appliance_state
    import capo_ec2.types.nat_gateway_appliance_type
    import capo_ec2.types.string


class NatGatewayAttachedAppliance(TypedDict, closed=True):
    type: NotRequired[
        "capo_ec2.types.nat_gateway_appliance_type.NatGatewayApplianceType"
    ]
    """<p>The type of appliance attached to the NAT Gateway. For network firewall proxy functionality, this will be "network-firewall-proxy".</p>"""
    appliance_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the attached appliance, identifying the specific proxy or security appliance resource.</p>"""
    vpc_endpoint_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The VPC endpoint ID used to route traffic from application VPCs to the proxy for inspection and filtering.</p>"""
    attachment_state: NotRequired[
        "capo_ec2.types.nat_gateway_appliance_state.NatGatewayApplianceState"
    ]
    """<p>The current attachment state of the appliance.</p>"""
    modification_state: NotRequired[
        "capo_ec2.types.nat_gateway_appliance_modify_state.NatGatewayApplianceModifyState"
    ]
    """<p>The current modification state of the appliance.</p>"""
    failure_code: NotRequired["capo_ec2.types.string.String"]
    """<p>The failure code if the appliance attachment or modification operation failed.</p>"""
    failure_message: NotRequired["capo_ec2.types.string.String"]
    """<p>A descriptive message explaining the failure if the appliance attachment or modification operation failed.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NatGatewayAttachedAppliance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type" in value:
        import capo_ec2.types.nat_gateway_appliance_type

        capo_ec2.types.nat_gateway_appliance_type.serialize_ec2_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "appliance_arn" in value:
        pairs.append((f"{key_prefix}ApplianceArn", str(value["appliance_arn"])))
    if "vpc_endpoint_id" in value:
        pairs.append((f"{key_prefix}VpcEndpointId", str(value["vpc_endpoint_id"])))
    if "attachment_state" in value:
        import capo_ec2.types.nat_gateway_appliance_state

        capo_ec2.types.nat_gateway_appliance_state.serialize_ec2_query(
            value["attachment_state"], pairs, f"{key_prefix}AttachmentState"
        )
    if "modification_state" in value:
        import capo_ec2.types.nat_gateway_appliance_modify_state

        capo_ec2.types.nat_gateway_appliance_modify_state.serialize_ec2_query(
            value["modification_state"], pairs, f"{key_prefix}ModificationState"
        )
    if "failure_code" in value:
        pairs.append((f"{key_prefix}FailureCode", str(value["failure_code"])))
    if "failure_message" in value:
        pairs.append((f"{key_prefix}FailureMessage", str(value["failure_message"])))


def deserialize_ec2_query(el: Element) -> NatGatewayAttachedAppliance:
    out: NatGatewayAttachedAppliance = {}  # type: ignore[typeddict-item]
    child_type = el.find("type")
    if child_type is not None:
        import capo_ec2.types.nat_gateway_appliance_type

        out["type"] = capo_ec2.types.nat_gateway_appliance_type.deserialize_ec2_query(
            child_type
        )
    child_appliance_arn = el.find("applianceArn")
    if child_appliance_arn is not None:
        out["appliance_arn"] = str(child_appliance_arn.text or "")
    child_vpc_endpoint_id = el.find("vpcEndpointId")
    if child_vpc_endpoint_id is not None:
        out["vpc_endpoint_id"] = str(child_vpc_endpoint_id.text or "")
    child_attachment_state = el.find("attachmentState")
    if child_attachment_state is not None:
        import capo_ec2.types.nat_gateway_appliance_state

        out["attachment_state"] = (
            capo_ec2.types.nat_gateway_appliance_state.deserialize_ec2_query(
                child_attachment_state
            )
        )
    child_modification_state = el.find("modificationState")
    if child_modification_state is not None:
        import capo_ec2.types.nat_gateway_appliance_modify_state

        out["modification_state"] = (
            capo_ec2.types.nat_gateway_appliance_modify_state.deserialize_ec2_query(
                child_modification_state
            )
        )
    child_failure_code = el.find("failureCode")
    if child_failure_code is not None:
        out["failure_code"] = str(child_failure_code.text or "")
    child_failure_message = el.find("failureMessage")
    if child_failure_message is not None:
        out["failure_message"] = str(child_failure_message.text or "")
    return out
