"""Generated from Smithy shape ``com.amazonaws.eks#OutpostConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks.types.control_plane_placement_request
    import capo_eks.types.etcd_placement_request
    import capo_eks.types.string
    import capo_eks.types.string_list


class OutpostConfigRequest(TypedDict, closed=True):
    outpost_arns: "capo_eks.types.string_list.StringList"
    """<p>The ARN of the Outpost that you want to use for your local Amazon EKS cluster on Outposts. Only a single Outpost ARN is supported.</p>"""
    control_plane_instance_type: "capo_eks.types.string.String"
    """<p>The Amazon EC2 instance type for the Kubernetes control plane instances of your local Amazon EKS cluster on Amazon Web Services Outposts. This instance type applies to all control plane instances and cannot be changed after cluster creation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html">Capacity considerations</a> in the <i>Amazon EKS User Guide</i>.</p> <p> </p>"""
    control_plane_placement: NotRequired[
        "capo_eks.types.control_plane_placement_request.ControlPlanePlacementRequest"
    ]
    """<p>An object representing the placement configuration for all the control plane instances of your local Amazon EKS cluster on an Amazon Web Services Outpost. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html">Capacity considerations</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    etcd_instance_type: NotRequired["capo_eks.types.string.String"]
    """<p>The Amazon EC2 instance type for etcd instances of your local Amazon EKS cluster on Amazon Web Services Outposts. This instance type applies to all etcd instances and cannot be changed after cluster creation.</p>"""
    etcd_placement: NotRequired[
        "capo_eks.types.etcd_placement_request.EtcdPlacementRequest"
    ]
    """<p>An object representing the placement configuration for the etcd instances of your local Amazon EKS cluster on an Amazon Web Services Outpost. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html">Capacity considerations</a> in the <i>Amazon EKS User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutpostConfigRequest) -> dict:
    out: dict = {}
    import capo_eks.types.string_list

    out["outpostArns"] = capo_eks.types.string_list.serialize_json(
        value["outpost_arns"]
    )
    out["controlPlaneInstanceType"] = value["control_plane_instance_type"]
    if "control_plane_placement" in value:
        import capo_eks.types.control_plane_placement_request

        out["controlPlanePlacement"] = (
            capo_eks.types.control_plane_placement_request.serialize_json(
                value["control_plane_placement"]
            )
        )
    if "etcd_instance_type" in value:
        out["etcdInstanceType"] = value["etcd_instance_type"]
    if "etcd_placement" in value:
        import capo_eks.types.etcd_placement_request

        out["etcdPlacement"] = capo_eks.types.etcd_placement_request.serialize_json(
            value["etcd_placement"]
        )
    return out


def deserialize_json(data: dict) -> OutpostConfigRequest:
    out: OutpostConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("outpostArns") is not None:
        import capo_eks.types.string_list

        out["outpost_arns"] = capo_eks.types.string_list.deserialize_json(
            data["outpostArns"]
        )
    else:
        raise DeserializationError("OutpostConfigRequest.outpost_arns required")
    if data.get("controlPlaneInstanceType") is not None:
        out["control_plane_instance_type"] = data["controlPlaneInstanceType"]
    else:
        raise DeserializationError(
            "OutpostConfigRequest.control_plane_instance_type required"
        )
    if data.get("controlPlanePlacement") is not None:
        import capo_eks.types.control_plane_placement_request

        out["control_plane_placement"] = (
            capo_eks.types.control_plane_placement_request.deserialize_json(
                data["controlPlanePlacement"]
            )
        )
    if data.get("etcdInstanceType") is not None:
        out["etcd_instance_type"] = data["etcdInstanceType"]
    if data.get("etcdPlacement") is not None:
        import capo_eks.types.etcd_placement_request

        out["etcd_placement"] = capo_eks.types.etcd_placement_request.deserialize_json(
            data["etcdPlacement"]
        )
    return out
