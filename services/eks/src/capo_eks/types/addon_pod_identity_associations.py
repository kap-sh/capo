"""Generated from Smithy shape ``com.amazonaws.eks#AddonPodIdentityAssociations``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class AddonPodIdentityAssociations(TypedDict, closed=True):
    service_account: "capo_eks.types.string.String"
    """<p>The name of a Kubernetes Service Account.</p>"""
    role_arn: "capo_eks.types.string.String"
    """<p>The ARN of an IAM Role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddonPodIdentityAssociations) -> dict:
    out: dict = {}
    out["serviceAccount"] = value["service_account"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> AddonPodIdentityAssociations:
    out: AddonPodIdentityAssociations = {}  # type: ignore[typeddict-item]
    if data.get("serviceAccount") is not None:
        out["service_account"] = data["serviceAccount"]
    else:
        out["service_account"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
