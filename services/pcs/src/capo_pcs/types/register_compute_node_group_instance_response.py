"""Generated from Smithy shape ``com.amazonaws.pcs#RegisterComputeNodeGroupInstanceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pcs.types.endpoints
    import capo_pcs.types.node_lifecycle_actions
    import capo_pcs.types.shared_secret


class RegisterComputeNodeGroupInstanceResponse(TypedDict, closed=True):
    node_id: "str"
    """<p>The scheduler node ID for this instance.</p>"""
    shared_secret: "capo_pcs.types.shared_secret.SharedSecret"
    """<p>For the Slurm scheduler, this is the shared Munge key the scheduler uses to authenticate compute node group instances.</p>"""
    endpoints: "capo_pcs.types.endpoints.Endpoints"
    """<p>The list of endpoints available for interaction with the scheduler.</p>"""
    cluster_name: NotRequired["str"]
    """<p>The name of the cluster that the compute node registered into.</p>"""
    compute_node_group_id: NotRequired["str"]
    """<p>The ID of the compute node group that the compute node registered into.</p>"""
    compute_node_group_name: NotRequired["str"]
    """<p>The name of the compute node group that the compute node registered into.</p>"""
    node_lifecycle_actions: NotRequired[
        "capo_pcs.types.node_lifecycle_actions.NodeLifecycleActions"
    ]
    """<p>The node lifecycle actions configured for the node group, including scripts to run when a compute node finishes bootstrapping or becomes ready to accept jobs.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegisterComputeNodeGroupInstanceResponse) -> dict:
    out: dict = {}
    out["nodeID"] = value["node_id"]
    out["sharedSecret"] = value["shared_secret"]
    import capo_pcs.types.endpoints

    out["endpoints"] = capo_pcs.types.endpoints.serialize_aws_json_1_0(
        value["endpoints"]
    )
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "compute_node_group_id" in value:
        out["computeNodeGroupId"] = value["compute_node_group_id"]
    if "compute_node_group_name" in value:
        out["computeNodeGroupName"] = value["compute_node_group_name"]
    if "node_lifecycle_actions" in value:
        import capo_pcs.types.node_lifecycle_actions

        out["nodeLifecycleActions"] = (
            capo_pcs.types.node_lifecycle_actions.serialize_aws_json_1_0(
                value["node_lifecycle_actions"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegisterComputeNodeGroupInstanceResponse:
    out: RegisterComputeNodeGroupInstanceResponse = {}  # type: ignore[typeddict-item]
    if data.get("nodeID") is not None:
        out["node_id"] = data["nodeID"]
    else:
        raise DeserializationError(
            "RegisterComputeNodeGroupInstanceResponse.node_id required"
        )
    if data.get("sharedSecret") is not None:
        out["shared_secret"] = data["sharedSecret"]
    else:
        raise DeserializationError(
            "RegisterComputeNodeGroupInstanceResponse.shared_secret required"
        )
    if data.get("endpoints") is not None:
        import capo_pcs.types.endpoints

        out["endpoints"] = capo_pcs.types.endpoints.deserialize_aws_json_1_0(
            data["endpoints"]
        )
    else:
        raise DeserializationError(
            "RegisterComputeNodeGroupInstanceResponse.endpoints required"
        )
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    if data.get("computeNodeGroupId") is not None:
        out["compute_node_group_id"] = data["computeNodeGroupId"]
    if data.get("computeNodeGroupName") is not None:
        out["compute_node_group_name"] = data["computeNodeGroupName"]
    if data.get("nodeLifecycleActions") is not None:
        import capo_pcs.types.node_lifecycle_actions

        out["node_lifecycle_actions"] = (
            capo_pcs.types.node_lifecycle_actions.deserialize_aws_json_1_0(
                data["nodeLifecycleActions"]
            )
        )
    return out


def redact_sensitive(value: RegisterComputeNodeGroupInstanceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "shared_secret" in value:
        out["shared_secret"] = "*** Sensitive Data Redacted ***"
    return out
