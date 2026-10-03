"""Generated from Smithy shape ``com.amazonaws.eks#UpgradePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.support_type


class UpgradePolicyRequest(TypedDict, closed=True):
    support_type: NotRequired["capo_eks.types.support_type.SupportType"]
    """<p>If the cluster is set to <code>EXTENDED</code>, it will enter extended support at the end of standard support. If the cluster is set to <code>STANDARD</code>, it will be automatically upgraded at the end of standard support.</p> <p> <a href="https://docs.aws.amazon.com/eks/latest/userguide/extended-support-control.html">Learn more about EKS Extended Support in the <i>Amazon EKS User Guide</i>.</a> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpgradePolicyRequest) -> dict:
    out: dict = {}
    if "support_type" in value:
        import capo_eks.types.support_type

        out["supportType"] = capo_eks.types.support_type.serialize_json(
            value["support_type"]
        )
    return out


def deserialize_json(data: dict) -> UpgradePolicyRequest:
    out: UpgradePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("supportType") is not None:
        import capo_eks.types.support_type

        out["support_type"] = capo_eks.types.support_type.deserialize_json(
            data["supportType"]
        )
    return out
