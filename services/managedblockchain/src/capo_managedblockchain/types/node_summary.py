"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NodeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.arn_string
    import capo_managedblockchain.types.availability_zone_string
    import capo_managedblockchain.types.instance_type_string
    import capo_managedblockchain.types.node_status
    import capo_managedblockchain.types.resource_id_string
    import capo_managedblockchain.types.timestamp


class NodeSummary(TypedDict, closed=True):
    id: NotRequired["capo_managedblockchain.types.resource_id_string.ResourceIdString"]
    """<p>The unique identifier of the node.</p>"""
    status: NotRequired["capo_managedblockchain.types.node_status.NodeStatus"]
    """<p>The status of the node.</p>"""
    creation_date: NotRequired["capo_managedblockchain.types.timestamp.Timestamp"]
    """<p>The date and time that the node was created.</p>"""
    availability_zone: NotRequired[
        "capo_managedblockchain.types.availability_zone_string.AvailabilityZoneString"
    ]
    """<p>The Availability Zone in which the node exists.</p>"""
    instance_type: NotRequired[
        "capo_managedblockchain.types.instance_type_string.InstanceTypeString"
    ]
    """<p>The EC2 instance type for the node.</p>"""
    arn: NotRequired["capo_managedblockchain.types.arn_string.ArnString"]
    """<p>The Amazon Resource Name (ARN) of the node. For more information about ARNs and their format, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "status" in value:
        import capo_managedblockchain.types.node_status

        out["Status"] = capo_managedblockchain.types.node_status.serialize_json(
            value["status"]
        )
    if "creation_date" in value:
        import capo_managedblockchain.types.timestamp

        out["CreationDate"] = capo_managedblockchain.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> NodeSummary:
    out: NodeSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Status") is not None:
        import capo_managedblockchain.types.node_status

        out["status"] = capo_managedblockchain.types.node_status.deserialize_json(
            data["Status"]
        )
    if data.get("CreationDate") is not None:
        import capo_managedblockchain.types.timestamp

        out["creation_date"] = capo_managedblockchain.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
