"""Generated from Smithy shape ``com.amazonaws.pcs#ComputeNodeGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pcs.types.compute_node_group_name
    import capo_pcs.types.compute_node_group_status


class ComputeNodeGroupSummary(TypedDict, closed=True):
    name: "capo_pcs.types.compute_node_group_name.ComputeNodeGroupName"
    """<p>The name that identifies the compute node group.</p>"""
    id: "str"
    """<p>The generated unique ID of the compute node group.</p>"""
    arn: "str"
    """<p>The unique Amazon Resource Name (ARN) of the compute node group.</p>"""
    cluster_id: "str"
    """<p>The ID of the cluster of the compute node group.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the resource was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time the resource was modified.</p>"""
    status: "capo_pcs.types.compute_node_group_status.ComputeNodeGroupStatus"
    """<p>The provisioning status of the compute node group.</p> <note> <p>The provisioning status doesn't indicate the overall health of the compute node group.</p> </note> <important> <p>The resource enters the <code>SUSPENDING</code> and <code>SUSPENDED</code> states when the scheduler is beyond end of life and we have suspended the cluster. When in these states, you can't use the cluster. The cluster controller is down and all compute instances are terminated. The resources still count toward your service quotas. You can delete a resource if its status is <code>SUSPENDED</code>. For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions_faq.html">Frequently asked questions about Slurm versions in PCS</a> in the <i>PCS User Guide</i>.</p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComputeNodeGroupSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["clusterId"] = value["cluster_id"]
    import capo_pcs._protocol.serialize

    out["createdAt"] = capo_pcs._protocol.serialize.fmt_date_time(value["created_at"])
    import capo_pcs._protocol.serialize

    out["modifiedAt"] = capo_pcs._protocol.serialize.fmt_date_time(value["modified_at"])
    import capo_pcs.types.compute_node_group_status

    out["status"] = capo_pcs.types.compute_node_group_status.serialize_aws_json_1_0(
        value["status"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ComputeNodeGroupSummary:
    out: ComputeNodeGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ComputeNodeGroupSummary.name required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ComputeNodeGroupSummary.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ComputeNodeGroupSummary.arn required")
    if data.get("clusterId") is not None:
        out["cluster_id"] = data["clusterId"]
    else:
        raise DeserializationError("ComputeNodeGroupSummary.cluster_id required")
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("ComputeNodeGroupSummary.created_at required")
    if data.get("modifiedAt") is not None:
        import datetime

        out["modified_at"] = datetime.datetime.fromisoformat(
            data["modifiedAt"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("ComputeNodeGroupSummary.modified_at required")
    if data.get("status") is not None:
        import capo_pcs.types.compute_node_group_status

        out["status"] = (
            capo_pcs.types.compute_node_group_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ComputeNodeGroupSummary.status required")
    return out
