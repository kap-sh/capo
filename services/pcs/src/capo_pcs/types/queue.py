"""Generated from Smithy shape ``com.amazonaws.pcs#Queue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pcs.types.compute_node_group_configuration_list
    import capo_pcs.types.error_info_list
    import capo_pcs.types.queue_name
    import capo_pcs.types.queue_slurm_configuration
    import capo_pcs.types.queue_status


class Queue(TypedDict, closed=True):
    name: "capo_pcs.types.queue_name.QueueName"
    """<p>The name that identifies the queue.</p>"""
    id: "str"
    """<p>The generated unique ID of the queue.</p>"""
    arn: "str"
    """<p>The unique Amazon Resource Name (ARN) of the queue.</p>"""
    cluster_id: "str"
    """<p>The ID of the cluster of the queue.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the resource was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time the resource was modified.</p>"""
    status: "capo_pcs.types.queue_status.QueueStatus"
    """<p>The provisioning status of the queue.</p> <note> <p>The provisioning status doesn't indicate the overall health of the queue.</p> </note> <important> <p>The resource enters the <code>SUSPENDING</code> and <code>SUSPENDED</code> states when the scheduler is beyond end of life and we have suspended the cluster. When in these states, you can't use the cluster. The cluster controller is down and all compute instances are terminated. The resources still count toward your service quotas. You can delete a resource if its status is <code>SUSPENDED</code>. For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions_faq.html">Frequently asked questions about Slurm versions in PCS</a> in the <i>PCS User Guide</i>.</p> </important>"""
    compute_node_group_configurations: "capo_pcs.types.compute_node_group_configuration_list.ComputeNodeGroupConfigurationList"
    """<p>The list of compute node group configurations associated with the queue. Queues assign jobs to associated compute node groups.</p>"""
    slurm_configuration: NotRequired[
        "capo_pcs.types.queue_slurm_configuration.QueueSlurmConfiguration"
    ]
    """<p>Additional options related to the Slurm scheduler.</p>"""
    error_info: NotRequired["capo_pcs.types.error_info_list.ErrorInfoList"]
    """<p>The list of errors that occurred during queue provisioning.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Queue) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["clusterId"] = value["cluster_id"]
    import capo_pcs._protocol.serialize

    out["createdAt"] = capo_pcs._protocol.serialize.fmt_date_time(value["created_at"])
    import capo_pcs._protocol.serialize

    out["modifiedAt"] = capo_pcs._protocol.serialize.fmt_date_time(value["modified_at"])
    import capo_pcs.types.queue_status

    out["status"] = capo_pcs.types.queue_status.serialize_aws_json_1_0(value["status"])
    import capo_pcs.types.compute_node_group_configuration_list

    out["computeNodeGroupConfigurations"] = (
        capo_pcs.types.compute_node_group_configuration_list.serialize_aws_json_1_0(
            value["compute_node_group_configurations"]
        )
    )
    if "slurm_configuration" in value:
        import capo_pcs.types.queue_slurm_configuration

        out["slurmConfiguration"] = (
            capo_pcs.types.queue_slurm_configuration.serialize_aws_json_1_0(
                value["slurm_configuration"]
            )
        )
    if "error_info" in value:
        import capo_pcs.types.error_info_list

        out["errorInfo"] = capo_pcs.types.error_info_list.serialize_aws_json_1_0(
            value["error_info"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Queue:
    out: Queue = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Queue.name required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("Queue.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Queue.arn required")
    if data.get("clusterId") is not None:
        out["cluster_id"] = data["clusterId"]
    else:
        raise DeserializationError("Queue.cluster_id required")
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("Queue.created_at required")
    if data.get("modifiedAt") is not None:
        import datetime

        out["modified_at"] = datetime.datetime.fromisoformat(
            data["modifiedAt"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("Queue.modified_at required")
    if data.get("status") is not None:
        import capo_pcs.types.queue_status

        out["status"] = capo_pcs.types.queue_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        raise DeserializationError("Queue.status required")
    if data.get("computeNodeGroupConfigurations") is not None:
        import capo_pcs.types.compute_node_group_configuration_list

        out["compute_node_group_configurations"] = (
            capo_pcs.types.compute_node_group_configuration_list.deserialize_aws_json_1_0(
                data["computeNodeGroupConfigurations"]
            )
        )
    else:
        raise DeserializationError("Queue.compute_node_group_configurations required")
    if data.get("slurmConfiguration") is not None:
        import capo_pcs.types.queue_slurm_configuration

        out["slurm_configuration"] = (
            capo_pcs.types.queue_slurm_configuration.deserialize_aws_json_1_0(
                data["slurmConfiguration"]
            )
        )
    if data.get("errorInfo") is not None:
        import capo_pcs.types.error_info_list

        out["error_info"] = capo_pcs.types.error_info_list.deserialize_aws_json_1_0(
            data["errorInfo"]
        )
    return out
