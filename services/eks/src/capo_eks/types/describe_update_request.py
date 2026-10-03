"""Generated from Smithy shape ``com.amazonaws.eks#DescribeUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class DescribeUpdateRequest(TypedDict, closed=True):
    name: "capo_eks.types.string.String"
    """<p>The name of the Amazon EKS cluster associated with the update.</p>"""
    update_id: "capo_eks.types.string.String"
    """<p>The ID of the update to describe.</p>"""
    nodegroup_name: NotRequired["capo_eks.types.string.String"]
    """<p>The name of the Amazon EKS node group associated with the update. This parameter is required if the update is a node group update.</p>"""
    addon_name: NotRequired["capo_eks.types.string.String"]
    """<p>The name of the add-on. The name must match one of the names returned by <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html"> <code>ListAddons</code> </a>. This parameter is required if the update is an add-on update.</p>"""
    capability_name: NotRequired["capo_eks.types.string.String"]
    """<p>The name of the capability for which you want to describe updates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUpdateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeUpdateRequest:
    out: DescribeUpdateRequest = {}  # type: ignore[typeddict-item]
    return out
