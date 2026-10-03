"""Generated from Smithy shape ``com.amazonaws.eks#DeleteAddonRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.boolean
    import capo_eks.types.cluster_name
    import capo_eks.types.string


class DeleteAddonRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.cluster_name.ClusterName"
    """<p>The name of your cluster.</p>"""
    addon_name: "capo_eks.types.string.String"
    """<p>The name of the add-on. The name must match one of the names returned by <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html"> <code>ListAddons</code> </a>.</p>"""
    preserve: "capo_eks.types.boolean.Boolean"
    """<p>Specifying this option preserves the add-on software on your cluster but Amazon EKS stops managing any settings for the add-on. If an IAM account is associated with the add-on, it isn't removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAddonRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAddonRequest:
    out: DeleteAddonRequest = {}  # type: ignore[typeddict-item]
    return out
