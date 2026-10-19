"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyResourceSelectionRecipe``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.wildcard_version_number


class LifecyclePolicyResourceSelectionRecipe(TypedDict, closed=True):
    name: "capo_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of an Image Builder recipe that the lifecycle policy uses for resource selection.</p>"""
    semantic_version: (
        "capo_imagebuilder.types.wildcard_version_number.WildcardVersionNumber"
    )
    """<p>The version of the Image Builder recipe specified by the <code>name</code> field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyResourceSelectionRecipe) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["semanticVersion"] = value["semantic_version"]
    return out


def deserialize_json(data: dict) -> LifecyclePolicyResourceSelectionRecipe:
    out: LifecyclePolicyResourceSelectionRecipe = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("semanticVersion") is not None:
        out["semantic_version"] = data["semanticVersion"]
    else:
        out["semantic_version"] = ""
    return out
