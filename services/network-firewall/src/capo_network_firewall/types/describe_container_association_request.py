"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeContainerAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class DescribeContainerAssociationRequest(TypedDict, closed=True):
    container_association_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the container association.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    container_association_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the container association.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeContainerAssociationRequest) -> dict:
    out: dict = {}
    if "container_association_name" in value:
        out["ContainerAssociationName"] = value["container_association_name"]
    if "container_association_arn" in value:
        out["ContainerAssociationArn"] = value["container_association_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeContainerAssociationRequest:
    out: DescribeContainerAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContainerAssociationName") is not None:
        out["container_association_name"] = data["ContainerAssociationName"]
    if data.get("ContainerAssociationArn") is not None:
        out["container_association_arn"] = data["ContainerAssociationArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeContainerAssociationRequest) -> dict:
    out: dict = {}
    if "container_association_name" in value:
        out["ContainerAssociationName"] = value["container_association_name"]
    if "container_association_arn" in value:
        out["ContainerAssociationArn"] = value["container_association_arn"]
    return out


def deserialize_cbor(data: dict) -> DescribeContainerAssociationRequest:
    out: DescribeContainerAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContainerAssociationName") is not None:
        out["container_association_name"] = data["ContainerAssociationName"]
    if data.get("ContainerAssociationArn") is not None:
        out["container_association_arn"] = data["ContainerAssociationArn"]
    return out
