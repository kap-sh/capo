"""Generated from Smithy shape ``com.amazonaws.networkfirewall#VpcEndpointAssociationMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn


class VpcEndpointAssociationMetadata(TypedDict, closed=True):
    vpc_endpoint_association_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a VPC endpoint association.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpointAssociationMetadata) -> dict:
    out: dict = {}
    if "vpc_endpoint_association_arn" in value:
        out["VpcEndpointAssociationArn"] = value["vpc_endpoint_association_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VpcEndpointAssociationMetadata:
    out: VpcEndpointAssociationMetadata = {}  # type: ignore[typeddict-item]
    if data.get("VpcEndpointAssociationArn") is not None:
        out["vpc_endpoint_association_arn"] = data["VpcEndpointAssociationArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VpcEndpointAssociationMetadata) -> dict:
    out: dict = {}
    if "vpc_endpoint_association_arn" in value:
        out["VpcEndpointAssociationArn"] = value["vpc_endpoint_association_arn"]
    return out


def deserialize_cbor(data: dict) -> VpcEndpointAssociationMetadata:
    out: VpcEndpointAssociationMetadata = {}  # type: ignore[typeddict-item]
    if data.get("VpcEndpointAssociationArn") is not None:
        out["vpc_endpoint_association_arn"] = data["VpcEndpointAssociationArn"]
    return out
