"""Generated from Smithy shape ``com.amazonaws.databrew#DeleteRecipeVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.recipe_name
    import capo_databrew.types.recipe_version


class DeleteRecipeVersionResponse(TypedDict, closed=True):
    name: "capo_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe that was deleted.</p>"""
    recipe_version: "capo_databrew.types.recipe_version.RecipeVersion"
    """<p>The version of the recipe that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecipeVersionResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RecipeVersion"] = value["recipe_version"]
    return out


def deserialize_json(data: dict) -> DeleteRecipeVersionResponse:
    out: DeleteRecipeVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("RecipeVersion") is not None:
        out["recipe_version"] = data["RecipeVersion"]
    else:
        out["recipe_version"] = ""
    return out
