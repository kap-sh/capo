"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PutComponentPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.component_build_version_arn
    import capo_imagebuilder.types.resource_policy_document


class PutComponentPolicyRequest(TypedDict, closed=True):
    component_arn: (
        "capo_imagebuilder.types.component_build_version_arn.ComponentBuildVersionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the component that this policy should be applied to.</p>"""
    policy: "capo_imagebuilder.types.resource_policy_document.ResourcePolicyDocument"
    """<p>The policy to apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutComponentPolicyRequest) -> dict:
    out: dict = {}
    out["componentArn"] = value["component_arn"]
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutComponentPolicyRequest:
    out: PutComponentPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("componentArn") is not None:
        out["component_arn"] = data["componentArn"]
    else:
        out["component_arn"] = ""
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
