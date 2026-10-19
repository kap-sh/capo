"""Generated from Smithy shape ``com.amazonaws.databrew#CreateRecipeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.recipe_description
    import capo_databrew.types.recipe_name
    import capo_databrew.types.recipe_step_list
    import capo_databrew.types.tag_map


class CreateRecipeRequest(TypedDict, closed=True):
    description: NotRequired["capo_databrew.types.recipe_description.RecipeDescription"]
    """<p>A description for the recipe.</p>"""
    name: "capo_databrew.types.recipe_name.RecipeName"
    """<p>A unique name for the recipe. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>"""
    steps: "capo_databrew.types.recipe_step_list.RecipeStepList"
    """<p>An array containing the steps to be performed by the recipe. Each recipe step consists of one recipe action and (optionally) an array of condition expressions.</p>"""
    tags: NotRequired["capo_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags to apply to this recipe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecipeRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    out["Name"] = value["name"]
    import capo_databrew.types.recipe_step_list

    out["Steps"] = capo_databrew.types.recipe_step_list.serialize_json(value["steps"])
    if "tags" in value:
        import capo_databrew.types.tag_map

        out["Tags"] = capo_databrew.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRecipeRequest:
    out: CreateRecipeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Steps") is not None:
        import capo_databrew.types.recipe_step_list

        out["steps"] = capo_databrew.types.recipe_step_list.deserialize_json(
            data["Steps"]
        )
    else:
        out["steps"] = []
    if data.get("Tags") is not None:
        import capo_databrew.types.tag_map

        out["tags"] = capo_databrew.types.tag_map.deserialize_json(data["Tags"])
    return out
