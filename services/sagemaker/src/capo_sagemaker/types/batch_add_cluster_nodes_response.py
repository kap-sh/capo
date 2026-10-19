"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchAddClusterNodesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.batch_add_cluster_nodes_error_list
    import capo_sagemaker.types.node_addition_result_list


class BatchAddClusterNodesResponse(TypedDict, closed=True):
    successful: "capo_sagemaker.types.node_addition_result_list.NodeAdditionResultList"
    """<p>A list of <code>NodeLogicalIDs</code> that were successfully added to the cluster. The <code>NodeLogicalID</code> is unique per cluster and does not change between instance replacements. Each entry includes a <code>NodeLogicalId</code> that can be used to track the node's provisioning status (with <code>DescribeClusterNode</code>), the instance group name, and the current status of the node.</p>"""
    failed: "capo_sagemaker.types.batch_add_cluster_nodes_error_list.BatchAddClusterNodesErrorList"
    """<p>A list of errors that occurred during the node addition operation. Each entry includes the instance group name, error code, number of failed additions, and an error message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchAddClusterNodesResponse) -> dict:
    out: dict = {}
    import capo_sagemaker.types.node_addition_result_list

    out["Successful"] = (
        capo_sagemaker.types.node_addition_result_list.serialize_aws_json_1_1(
            value["successful"]
        )
    )
    import capo_sagemaker.types.batch_add_cluster_nodes_error_list

    out["Failed"] = (
        capo_sagemaker.types.batch_add_cluster_nodes_error_list.serialize_aws_json_1_1(
            value["failed"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchAddClusterNodesResponse:
    out: BatchAddClusterNodesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Successful") is not None:
        import capo_sagemaker.types.node_addition_result_list

        out["successful"] = (
            capo_sagemaker.types.node_addition_result_list.deserialize_aws_json_1_1(
                data["Successful"]
            )
        )
    else:
        out["successful"] = []
    if data.get("Failed") is not None:
        import capo_sagemaker.types.batch_add_cluster_nodes_error_list

        out["failed"] = (
            capo_sagemaker.types.batch_add_cluster_nodes_error_list.deserialize_aws_json_1_1(
                data["Failed"]
            )
        )
    else:
        out["failed"] = []
    return out
