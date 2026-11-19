"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeVpcEndpointAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.vpc_endpoint_association
    import capo_network_firewall.types.vpc_endpoint_association_status


class DescribeVpcEndpointAssociationResponse(TypedDict, closed=True):
    vpc_endpoint_association: NotRequired[
        "capo_network_firewall.types.vpc_endpoint_association.VpcEndpointAssociation"
    ]
    """<p>The configuration settings for the VPC endpoint association. These settings include the firewall and the VPC and subnet to use for the firewall endpoint. </p>"""
    vpc_endpoint_association_status: NotRequired[
        "capo_network_firewall.types.vpc_endpoint_association_status.VpcEndpointAssociationStatus"
    ]
    """<p>Detailed information about the current status of a <a>VpcEndpointAssociation</a>. You can retrieve this by calling <a>DescribeVpcEndpointAssociation</a> and providing the VPC endpoint association ARN.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeVpcEndpointAssociationResponse) -> dict:
    out: dict = {}
    if "vpc_endpoint_association" in value:
        import capo_network_firewall.types.vpc_endpoint_association

        out["VpcEndpointAssociation"] = (
            capo_network_firewall.types.vpc_endpoint_association.serialize_aws_json_1_0(
                value["vpc_endpoint_association"]
            )
        )
    if "vpc_endpoint_association_status" in value:
        import capo_network_firewall.types.vpc_endpoint_association_status

        out["VpcEndpointAssociationStatus"] = (
            capo_network_firewall.types.vpc_endpoint_association_status.serialize_aws_json_1_0(
                value["vpc_endpoint_association_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeVpcEndpointAssociationResponse:
    out: DescribeVpcEndpointAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("VpcEndpointAssociation") is not None:
        import capo_network_firewall.types.vpc_endpoint_association

        out["vpc_endpoint_association"] = (
            capo_network_firewall.types.vpc_endpoint_association.deserialize_aws_json_1_0(
                data["VpcEndpointAssociation"]
            )
        )
    if data.get("VpcEndpointAssociationStatus") is not None:
        import capo_network_firewall.types.vpc_endpoint_association_status

        out["vpc_endpoint_association_status"] = (
            capo_network_firewall.types.vpc_endpoint_association_status.deserialize_aws_json_1_0(
                data["VpcEndpointAssociationStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeVpcEndpointAssociationResponse) -> dict:
    out: dict = {}
    if "vpc_endpoint_association" in value:
        import capo_network_firewall.types.vpc_endpoint_association

        out["VpcEndpointAssociation"] = (
            capo_network_firewall.types.vpc_endpoint_association.serialize_cbor(
                value["vpc_endpoint_association"]
            )
        )
    if "vpc_endpoint_association_status" in value:
        import capo_network_firewall.types.vpc_endpoint_association_status

        out["VpcEndpointAssociationStatus"] = (
            capo_network_firewall.types.vpc_endpoint_association_status.serialize_cbor(
                value["vpc_endpoint_association_status"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeVpcEndpointAssociationResponse:
    out: DescribeVpcEndpointAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("VpcEndpointAssociation") is not None:
        import capo_network_firewall.types.vpc_endpoint_association

        out["vpc_endpoint_association"] = (
            capo_network_firewall.types.vpc_endpoint_association.deserialize_cbor(
                data["VpcEndpointAssociation"]
            )
        )
    if data.get("VpcEndpointAssociationStatus") is not None:
        import capo_network_firewall.types.vpc_endpoint_association_status

        out["vpc_endpoint_association_status"] = (
            capo_network_firewall.types.vpc_endpoint_association_status.deserialize_cbor(
                data["VpcEndpointAssociationStatus"]
            )
        )
    return out
