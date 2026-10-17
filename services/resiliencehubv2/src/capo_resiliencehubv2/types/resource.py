"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.aws_account_id
    import capo_resiliencehubv2.types.aws_region


class Resource(TypedDict, closed=True):
    identifier: "str"
    """<p>The identifier of the resource.</p>"""
    aws_region: NotRequired["capo_resiliencehubv2.types.aws_region.AwsRegion"]
    """<p>The AWS Region where the resource is located.</p>"""
    aws_account_id: NotRequired[
        "capo_resiliencehubv2.types.aws_account_id.AwsAccountId"
    ]
    """<p>The AWS account ID that owns the resource.</p>"""
    resource_type: NotRequired["str"]
    """<p>The type of the resource.</p>"""
    availability_zone_id: NotRequired["str"]
    """<p>The Availability Zone ID of the Availability Zone that hosts the resource, such as use1-az1. The Availability Zone ID is consistent across Amazon Web Services (AWS) accounts, unlike the Availability Zone name.</p>"""
    availability_zone_name: NotRequired["str"]
    """<p>The name of the Availability Zone that hosts the resource, such as us-west-2a.</p>"""
    containment_parent_id: NotRequired["str"]
    """<p>The identifier of the single parent resource that contains this resource, used to represent containment relationships in the resource topology. A resource has at most one containment parent.</p>"""
    logical_resource_group_id: NotRequired["str"]
    """<p>The identifier of the logical resource group that this resource belongs to. Resources that share this identifier are managed as a single unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "aws_region" in value:
        out["awsRegion"] = value["aws_region"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "availability_zone_name" in value:
        out["availabilityZoneName"] = value["availability_zone_name"]
    if "containment_parent_id" in value:
        out["containmentParentId"] = value["containment_parent_id"]
    if "logical_resource_group_id" in value:
        out["logicalResourceGroupId"] = value["logical_resource_group_id"]
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("Resource.identifier required")
    if data.get("awsRegion") is not None:
        out["aws_region"] = data["awsRegion"]
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("availabilityZoneId") is not None:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if data.get("availabilityZoneName") is not None:
        out["availability_zone_name"] = data["availabilityZoneName"]
    if data.get("containmentParentId") is not None:
        out["containment_parent_id"] = data["containmentParentId"]
    if data.get("logicalResourceGroupId") is not None:
        out["logical_resource_group_id"] = data["logicalResourceGroupId"]
    return out
