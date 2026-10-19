"""Generated from Smithy shape ``com.amazonaws.databrew#RecipeReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.recipe_name
    import capo_databrew.types.recipe_version


class RecipeReference(TypedDict, closed=True):
    name: "capo_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe.</p>"""
    recipe_version: NotRequired["capo_databrew.types.recipe_version.RecipeVersion"]
    """<p>The identifier for the version for the recipe. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecipeReference) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "recipe_version" in value:
        out["RecipeVersion"] = value["recipe_version"]
    return out


def deserialize_json(data: dict) -> RecipeReference:
    out: RecipeReference = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("RecipeVersion") is not None:
        out["recipe_version"] = data["RecipeVersion"]
    return out
