"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PutImageRecipePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_recipe_arn
    import capo_imagebuilder.types.resource_policy_document


class PutImageRecipePolicyRequest(TypedDict, closed=True):
    image_recipe_arn: "capo_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
    """<p>The Amazon Resource Name (ARN) of the image recipe that this policy should be applied to.</p>"""
    policy: "capo_imagebuilder.types.resource_policy_document.ResourcePolicyDocument"
    """<p>The policy to apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutImageRecipePolicyRequest) -> dict:
    out: dict = {}
    out["imageRecipeArn"] = value["image_recipe_arn"]
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutImageRecipePolicyRequest:
    out: PutImageRecipePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("imageRecipeArn") is not None:
        out["image_recipe_arn"] = data["imageRecipeArn"]
    else:
        out["image_recipe_arn"] = ""
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
