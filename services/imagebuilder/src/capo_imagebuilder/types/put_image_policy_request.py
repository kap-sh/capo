"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PutImagePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_build_version_arn
    import capo_imagebuilder.types.resource_policy_document


class PutImagePolicyRequest(TypedDict, closed=True):
    image_arn: "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    """<p>The Amazon Resource Name (ARN) of the image that this policy should be applied to.</p>"""
    policy: "capo_imagebuilder.types.resource_policy_document.ResourcePolicyDocument"
    """<p>The resource policy to apply to the image, as a JSON policy document. Image Builder validates the policy with Amazon Web Services RAM before applying it, and rejects invalid policies with <code>InvalidParameterValueException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutImagePolicyRequest) -> dict:
    out: dict = {}
    out["imageArn"] = value["image_arn"]
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutImagePolicyRequest:
    out: PutImagePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("imageArn") is not None:
        out["image_arn"] = data["imageArn"]
    else:
        out["image_arn"] = ""
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
