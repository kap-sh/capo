"""Generated from Smithy shape ``com.amazonaws.pcs#CreateQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.cluster_identifier
    import capo_pcs.types.compute_node_group_configuration_list
    import capo_pcs.types.queue_name
    import capo_pcs.types.queue_slurm_configuration_request
    import capo_pcs.types.request_tag_map
    import capo_pcs.types.sb_client_token


class CreateQueueRequest(TypedDict, closed=True):
    cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier"
    """<p>The name or ID of the cluster for which to create a queue.</p>"""
    queue_name: "capo_pcs.types.queue_name.QueueName"
    """<p>A name to identify the queue.</p>"""
    compute_node_group_configurations: NotRequired[
        "capo_pcs.types.compute_node_group_configuration_list.ComputeNodeGroupConfigurationList"
    ]
    """<p>The list of compute node group configurations to associate with the queue. Queues assign jobs to associated compute node groups.</p>"""
    slurm_configuration: NotRequired[
        "capo_pcs.types.queue_slurm_configuration_request.QueueSlurmConfigurationRequest"
    ]
    """<p>Additional options related to the Slurm scheduler.</p>"""
    client_token: NotRequired["capo_pcs.types.sb_client_token.SBClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>"""
    tags: NotRequired["capo_pcs.types.request_tag_map.RequestTagMap"]
    """<p>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateQueueRequest) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    out["queueName"] = value["queue_name"]
    if "compute_node_group_configurations" in value:
        import capo_pcs.types.compute_node_group_configuration_list

        out["computeNodeGroupConfigurations"] = (
            capo_pcs.types.compute_node_group_configuration_list.serialize_aws_json_1_0(
                value["compute_node_group_configurations"]
            )
        )
    if "slurm_configuration" in value:
        import capo_pcs.types.queue_slurm_configuration_request

        out["slurmConfiguration"] = (
            capo_pcs.types.queue_slurm_configuration_request.serialize_aws_json_1_0(
                value["slurm_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_pcs.types.request_tag_map

        out["tags"] = capo_pcs.types.request_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateQueueRequest:
    out: CreateQueueRequest = {}  # type: ignore[typeddict-item]
    if data.get("clusterIdentifier") is not None:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        out["cluster_identifier"] = ""
    if data.get("queueName") is not None:
        out["queue_name"] = data["queueName"]
    else:
        out["queue_name"] = ""
    if data.get("computeNodeGroupConfigurations") is not None:
        import capo_pcs.types.compute_node_group_configuration_list

        out["compute_node_group_configurations"] = (
            capo_pcs.types.compute_node_group_configuration_list.deserialize_aws_json_1_0(
                data["computeNodeGroupConfigurations"]
            )
        )
    if data.get("slurmConfiguration") is not None:
        import capo_pcs.types.queue_slurm_configuration_request

        out["slurm_configuration"] = (
            capo_pcs.types.queue_slurm_configuration_request.deserialize_aws_json_1_0(
                data["slurmConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_pcs.types.request_tag_map

        out["tags"] = capo_pcs.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
