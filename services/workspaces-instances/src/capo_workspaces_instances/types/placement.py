"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#Placement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.arn
    import capo_workspaces_instances.types.availability_zone
    import capo_workspaces_instances.types.host_id
    import capo_workspaces_instances.types.non_negative_integer
    import capo_workspaces_instances.types.placement_group_id
    import capo_workspaces_instances.types.string64
    import capo_workspaces_instances.types.tenancy_enum


class Placement(TypedDict, closed=True):
    affinity: NotRequired["capo_workspaces_instances.types.string64.String64"]
    """<p>Specifies host affinity for dedicated instances.</p>"""
    availability_zone: NotRequired[
        "capo_workspaces_instances.types.availability_zone.AvailabilityZone"
    ]
    """<p>Identifies the specific AWS availability zone.</p>"""
    group_id: NotRequired[
        "capo_workspaces_instances.types.placement_group_id.PlacementGroupId"
    ]
    """<p>Unique identifier for placement group.</p>"""
    group_name: NotRequired["capo_workspaces_instances.types.string64.String64"]
    """<p>Name of the placement group.</p>"""
    host_id: NotRequired["capo_workspaces_instances.types.host_id.HostId"]
    """<p>Identifies the specific dedicated host.</p>"""
    host_resource_group_arn: NotRequired["capo_workspaces_instances.types.arn.ARN"]
    """<p>ARN of the host resource group.</p>"""
    partition_number: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Specifies partition number for partition placement groups.</p>"""
    tenancy: NotRequired["capo_workspaces_instances.types.tenancy_enum.TenancyEnum"]
    """<p>Defines instance tenancy configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Placement) -> dict:
    out: dict = {}
    if "affinity" in value:
        out["Affinity"] = value["affinity"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "host_id" in value:
        out["HostId"] = value["host_id"]
    if "host_resource_group_arn" in value:
        out["HostResourceGroupArn"] = value["host_resource_group_arn"]
    if "partition_number" in value:
        out["PartitionNumber"] = value["partition_number"]
    if "tenancy" in value:
        import capo_workspaces_instances.types.tenancy_enum

        out["Tenancy"] = (
            capo_workspaces_instances.types.tenancy_enum.serialize_aws_json_1_0(
                value["tenancy"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Placement:
    out: Placement = {}  # type: ignore[typeddict-item]
    if data.get("Affinity") is not None:
        out["affinity"] = data["Affinity"]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
    if data.get("HostId") is not None:
        out["host_id"] = data["HostId"]
    if data.get("HostResourceGroupArn") is not None:
        out["host_resource_group_arn"] = data["HostResourceGroupArn"]
    if data.get("PartitionNumber") is not None:
        out["partition_number"] = data["PartitionNumber"]
    if data.get("Tenancy") is not None:
        import capo_workspaces_instances.types.tenancy_enum

        out["tenancy"] = (
            capo_workspaces_instances.types.tenancy_enum.deserialize_aws_json_1_0(
                data["Tenancy"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Placement) -> dict:
    out: dict = {}
    if "affinity" in value:
        out["Affinity"] = value["affinity"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "host_id" in value:
        out["HostId"] = value["host_id"]
    if "host_resource_group_arn" in value:
        out["HostResourceGroupArn"] = value["host_resource_group_arn"]
    if "partition_number" in value:
        out["PartitionNumber"] = value["partition_number"]
    if "tenancy" in value:
        import capo_workspaces_instances.types.tenancy_enum

        out["Tenancy"] = capo_workspaces_instances.types.tenancy_enum.serialize_cbor(
            value["tenancy"]
        )
    return out


def deserialize_cbor(data: dict) -> Placement:
    out: Placement = {}  # type: ignore[typeddict-item]
    if data.get("Affinity") is not None:
        out["affinity"] = data["Affinity"]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
    if data.get("HostId") is not None:
        out["host_id"] = data["HostId"]
    if data.get("HostResourceGroupArn") is not None:
        out["host_resource_group_arn"] = data["HostResourceGroupArn"]
    if data.get("PartitionNumber") is not None:
        out["partition_number"] = data["PartitionNumber"]
    if data.get("Tenancy") is not None:
        import capo_workspaces_instances.types.tenancy_enum

        out["tenancy"] = capo_workspaces_instances.types.tenancy_enum.deserialize_cbor(
            data["Tenancy"]
        )
    return out
