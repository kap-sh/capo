"""Generated from Smithy shape ``com.amazonaws.eks#NodegroupUpdateConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.nodegroup_update_strategies
    import capo_eks.types.non_zero_integer
    import capo_eks.types.percent_capacity


class NodegroupUpdateConfig(TypedDict, closed=True):
    max_unavailable: NotRequired["capo_eks.types.non_zero_integer.NonZeroInteger"]
    """<p>The maximum number of nodes unavailable at once during a version update. Nodes are updated in parallel. This value or <code>maxUnavailablePercentage</code> is required to have a value.The maximum number is 100.</p>"""
    max_unavailable_percentage: NotRequired[
        "capo_eks.types.percent_capacity.PercentCapacity"
    ]
    """<p>The maximum percentage of nodes unavailable during a version update. This percentage of nodes are updated in parallel, up to 100 nodes at once. This value or <code>maxUnavailable</code> is required to have a value.</p>"""
    update_strategy: NotRequired[
        "capo_eks.types.nodegroup_update_strategies.NodegroupUpdateStrategies"
    ]
    """<p>The configuration for the behavior to follow during a node group version update of this managed node group. You choose between two possible strategies for replacing nodes during an <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateNodegroupVersion.html"> <code>UpdateNodegroupVersion</code> </a> action.</p> <p>An Amazon EKS managed node group updates by replacing nodes with new nodes of newer AMI versions in parallel. The <i>update strategy</i> changes the managed node update behavior of the managed node group for each quantity. The <i>default</i> strategy has guardrails to protect you from misconfiguration and launches the new instances first, before terminating the old instances. The <i>minimal</i> strategy removes the guardrails and terminates the old instances before launching the new instances. This minimal strategy is useful in scenarios where you are constrained to resources or costs (for example, with hardware accelerators such as GPUs).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodegroupUpdateConfig) -> dict:
    out: dict = {}
    if "max_unavailable" in value:
        out["maxUnavailable"] = value["max_unavailable"]
    if "max_unavailable_percentage" in value:
        out["maxUnavailablePercentage"] = value["max_unavailable_percentage"]
    if "update_strategy" in value:
        import capo_eks.types.nodegroup_update_strategies

        out["updateStrategy"] = (
            capo_eks.types.nodegroup_update_strategies.serialize_json(
                value["update_strategy"]
            )
        )
    return out


def deserialize_json(data: dict) -> NodegroupUpdateConfig:
    out: NodegroupUpdateConfig = {}  # type: ignore[typeddict-item]
    if data.get("maxUnavailable") is not None:
        out["max_unavailable"] = data["maxUnavailable"]
    if data.get("maxUnavailablePercentage") is not None:
        out["max_unavailable_percentage"] = data["maxUnavailablePercentage"]
    if data.get("updateStrategy") is not None:
        import capo_eks.types.nodegroup_update_strategies

        out["update_strategy"] = (
            capo_eks.types.nodegroup_update_strategies.deserialize_json(
                data["updateStrategy"]
            )
        )
    return out
