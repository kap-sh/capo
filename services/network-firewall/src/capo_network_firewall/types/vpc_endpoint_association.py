"""Generated from Smithy shape ``com.amazonaws.networkfirewall#VpcEndpointAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.description
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_id
    import capo_network_firewall.types.subnet_mapping
    import capo_network_firewall.types.tag_list
    import capo_network_firewall.types.vpc_id


class VpcEndpointAssociation(TypedDict, closed=True):
    vpc_endpoint_association_id: NotRequired[
        "capo_network_firewall.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the VPC endpoint association. </p>"""
    vpc_endpoint_association_arn: "capo_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of a VPC endpoint association.</p>"""
    firewall_arn: "capo_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the firewall.</p>"""
    vpc_id: "capo_network_firewall.types.vpc_id.VpcId"
    """<p>The unique identifier of the VPC for the endpoint association. </p>"""
    subnet_mapping: "capo_network_firewall.types.subnet_mapping.SubnetMapping"
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the VPC endpoint association. </p>"""
    tags: NotRequired["capo_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpointAssociation) -> dict:
    out: dict = {}
    if "vpc_endpoint_association_id" in value:
        out["VpcEndpointAssociationId"] = value["vpc_endpoint_association_id"]
    out["VpcEndpointAssociationArn"] = value["vpc_endpoint_association_arn"]
    out["FirewallArn"] = value["firewall_arn"]
    out["VpcId"] = value["vpc_id"]
    import capo_network_firewall.types.subnet_mapping

    out["SubnetMapping"] = (
        capo_network_firewall.types.subnet_mapping.serialize_aws_json_1_0(
            value["subnet_mapping"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VpcEndpointAssociation:
    out: VpcEndpointAssociation = {}  # type: ignore[typeddict-item]
    if data.get("VpcEndpointAssociationId") is not None:
        out["vpc_endpoint_association_id"] = data["VpcEndpointAssociationId"]
    if data.get("VpcEndpointAssociationArn") is not None:
        out["vpc_endpoint_association_arn"] = data["VpcEndpointAssociationArn"]
    else:
        out["vpc_endpoint_association_arn"] = ""
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    else:
        out["firewall_arn"] = ""
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("SubnetMapping") is not None:
        import capo_network_firewall.types.subnet_mapping

        out["subnet_mapping"] = (
            capo_network_firewall.types.subnet_mapping.deserialize_aws_json_1_0(
                data["SubnetMapping"]
            )
        )
    else:
        raise DeserializationError("VpcEndpointAssociation.subnet_mapping required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
