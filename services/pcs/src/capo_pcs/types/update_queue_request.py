"""Generated from Smithy shape ``com.amazonaws.pcs#UpdateQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.cluster_identifier
    import capo_pcs.types.compute_node_group_configuration_list
    import capo_pcs.types.queue_identifier
    import capo_pcs.types.sb_client_token
    import capo_pcs.types.update_queue_slurm_configuration_request


class UpdateQueueRequest(TypedDict, closed=True):
    cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier"
    """<p>The name or ID of the cluster of the queue.</p>"""
    queue_identifier: "capo_pcs.types.queue_identifier.QueueIdentifier"
    """<p>The name or ID of the queue.</p>"""
    compute_node_group_configurations: NotRequired[
        "capo_pcs.types.compute_node_group_configuration_list.ComputeNodeGroupConfigurationList"
    ]
    """<p>The list of compute node group configurations to associate with the queue. Queues assign jobs to associated compute node groups.</p>"""
    slurm_configuration: NotRequired[
        "capo_pcs.types.update_queue_slurm_configuration_request.UpdateQueueSlurmConfigurationRequest"
    ]
    """<p>Additional options related to the Slurm scheduler.</p>"""
    client_token: NotRequired["capo_pcs.types.sb_client_token.SBClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateQueueRequest) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    out["queueIdentifier"] = value["queue_identifier"]
    if "compute_node_group_configurations" in value:
        import capo_pcs.types.compute_node_group_configuration_list

        out["computeNodeGroupConfigurations"] = (
            capo_pcs.types.compute_node_group_configuration_list.serialize_aws_json_1_0(
                value["compute_node_group_configurations"]
            )
        )
    if "slurm_configuration" in value:
        import capo_pcs.types.update_queue_slurm_configuration_request

        out["slurmConfiguration"] = (
            capo_pcs.types.update_queue_slurm_configuration_request.serialize_aws_json_1_0(
                value["slurm_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateQueueRequest:
    out: UpdateQueueRequest = {}  # type: ignore[typeddict-item]
    if data.get("clusterIdentifier") is not None:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        out["cluster_identifier"] = ""
    if data.get("queueIdentifier") is not None:
        out["queue_identifier"] = data["queueIdentifier"]
    else:
        out["queue_identifier"] = ""
    if data.get("computeNodeGroupConfigurations") is not None:
        import capo_pcs.types.compute_node_group_configuration_list

        out["compute_node_group_configurations"] = (
            capo_pcs.types.compute_node_group_configuration_list.deserialize_aws_json_1_0(
                data["computeNodeGroupConfigurations"]
            )
        )
    if data.get("slurmConfiguration") is not None:
        import capo_pcs.types.update_queue_slurm_configuration_request

        out["slurm_configuration"] = (
            capo_pcs.types.update_queue_slurm_configuration_request.deserialize_aws_json_1_0(
                data["slurmConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
