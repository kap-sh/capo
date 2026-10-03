"""Generated from Smithy shape ``com.amazonaws.eks#NodegroupScalingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.capacity
    import capo_eks.types.zero_capacity


class NodegroupScalingConfig(TypedDict, closed=True):
    min_size: NotRequired["capo_eks.types.zero_capacity.ZeroCapacity"]
    """<p>The minimum number of nodes that the managed node group can scale in to.</p>"""
    max_size: NotRequired["capo_eks.types.capacity.Capacity"]
    """<p>The maximum number of nodes that the managed node group can scale out to. For information about the maximum number that you can specify, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/service-quotas.html">Amazon EKS service quotas</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    desired_size: NotRequired["capo_eks.types.zero_capacity.ZeroCapacity"]
    """<p>The current number of nodes that the managed node group should maintain.</p> <important> <p>If you use the Kubernetes <a href="https://github.com/kubernetes/autoscaler#kubernetes-autoscaler">Cluster Autoscaler</a>, you shouldn't change the <code>desiredSize</code> value directly, as this can cause the Cluster Autoscaler to suddenly scale up or scale down.</p> </important> <p>Whenever this parameter changes, the number of worker nodes in the node group is updated to the specified size. If this parameter is given a value that is smaller than the current number of running worker nodes, the necessary number of worker nodes are terminated to match the given value. When using CloudFormation, no action occurs if you remove this parameter from your CFN template.</p> <p>This parameter can be different from <code>minSize</code> in some cases, such as when starting with extra hosts for testing. This parameter can also be different when you want to start with an estimated number of needed hosts, but let the Cluster Autoscaler reduce the number if there are too many. When the Cluster Autoscaler is used, the <code>desiredSize</code> parameter is altered by the Cluster Autoscaler (but can be out-of-date for short periods of time). the Cluster Autoscaler doesn't scale a managed node group lower than <code>minSize</code> or higher than <code>maxSize</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodegroupScalingConfig) -> dict:
    out: dict = {}
    if "min_size" in value:
        out["minSize"] = value["min_size"]
    if "max_size" in value:
        out["maxSize"] = value["max_size"]
    if "desired_size" in value:
        out["desiredSize"] = value["desired_size"]
    return out


def deserialize_json(data: dict) -> NodegroupScalingConfig:
    out: NodegroupScalingConfig = {}  # type: ignore[typeddict-item]
    if data.get("minSize") is not None:
        out["min_size"] = data["minSize"]
    if data.get("maxSize") is not None:
        out["max_size"] = data["maxSize"]
    if data.get("desiredSize") is not None:
        out["desired_size"] = data["desiredSize"]
    return out
