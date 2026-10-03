"""Generated from Smithy shape ``com.amazonaws.eks#UpdateNodegroupConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.node_repair_config
    import capo_eks.types.nodegroup_scaling_config
    import capo_eks.types.nodegroup_update_config
    import capo_eks.types.string
    import capo_eks.types.update_labels_payload
    import capo_eks.types.update_taints_payload
    import capo_eks.types.warm_pool_config


class UpdateNodegroupConfigRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    nodegroup_name: "capo_eks.types.string.String"
    """<p>The name of the managed node group to update.</p>"""
    labels: NotRequired["capo_eks.types.update_labels_payload.UpdateLabelsPayload"]
    """<p>The Kubernetes <code>labels</code> to apply to the nodes in the node group after the update.</p>"""
    taints: NotRequired["capo_eks.types.update_taints_payload.UpdateTaintsPayload"]
    """<p>The Kubernetes taints to be applied to the nodes in the node group after the update. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html">Node taints on managed node groups</a>.</p>"""
    scaling_config: NotRequired[
        "capo_eks.types.nodegroup_scaling_config.NodegroupScalingConfig"
    ]
    """<p>The scaling configuration details for the Auto Scaling group after the update.</p>"""
    update_config: NotRequired[
        "capo_eks.types.nodegroup_update_config.NodegroupUpdateConfig"
    ]
    """<p>The node group update configuration.</p>"""
    node_repair_config: NotRequired[
        "capo_eks.types.node_repair_config.NodeRepairConfig"
    ]
    """<p>The node auto repair configuration for the node group.</p>"""
    warm_pool_config: NotRequired["capo_eks.types.warm_pool_config.WarmPoolConfig"]
    """<p>The warm pool configuration to apply to the node group. You can use this to add a warm pool to an existing node group or modify the settings of an existing warm pool.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNodegroupConfigRequest) -> dict:
    out: dict = {}
    if "labels" in value:
        import capo_eks.types.update_labels_payload

        out["labels"] = capo_eks.types.update_labels_payload.serialize_json(
            value["labels"]
        )
    if "taints" in value:
        import capo_eks.types.update_taints_payload

        out["taints"] = capo_eks.types.update_taints_payload.serialize_json(
            value["taints"]
        )
    if "scaling_config" in value:
        import capo_eks.types.nodegroup_scaling_config

        out["scalingConfig"] = capo_eks.types.nodegroup_scaling_config.serialize_json(
            value["scaling_config"]
        )
    if "update_config" in value:
        import capo_eks.types.nodegroup_update_config

        out["updateConfig"] = capo_eks.types.nodegroup_update_config.serialize_json(
            value["update_config"]
        )
    if "node_repair_config" in value:
        import capo_eks.types.node_repair_config

        out["nodeRepairConfig"] = capo_eks.types.node_repair_config.serialize_json(
            value["node_repair_config"]
        )
    if "warm_pool_config" in value:
        import capo_eks.types.warm_pool_config

        out["warmPoolConfig"] = capo_eks.types.warm_pool_config.serialize_json(
            value["warm_pool_config"]
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> UpdateNodegroupConfigRequest:
    out: UpdateNodegroupConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("labels") is not None:
        import capo_eks.types.update_labels_payload

        out["labels"] = capo_eks.types.update_labels_payload.deserialize_json(
            data["labels"]
        )
    if data.get("taints") is not None:
        import capo_eks.types.update_taints_payload

        out["taints"] = capo_eks.types.update_taints_payload.deserialize_json(
            data["taints"]
        )
    if data.get("scalingConfig") is not None:
        import capo_eks.types.nodegroup_scaling_config

        out["scaling_config"] = (
            capo_eks.types.nodegroup_scaling_config.deserialize_json(
                data["scalingConfig"]
            )
        )
    if data.get("updateConfig") is not None:
        import capo_eks.types.nodegroup_update_config

        out["update_config"] = capo_eks.types.nodegroup_update_config.deserialize_json(
            data["updateConfig"]
        )
    if data.get("nodeRepairConfig") is not None:
        import capo_eks.types.node_repair_config

        out["node_repair_config"] = capo_eks.types.node_repair_config.deserialize_json(
            data["nodeRepairConfig"]
        )
    if data.get("warmPoolConfig") is not None:
        import capo_eks.types.warm_pool_config

        out["warm_pool_config"] = capo_eks.types.warm_pool_config.deserialize_json(
            data["warmPoolConfig"]
        )
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    return out
