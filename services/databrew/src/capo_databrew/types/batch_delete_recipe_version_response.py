"""Generated from Smithy shape ``com.amazonaws.databrew#BatchDeleteRecipeVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.recipe_error_list
    import capo_databrew.types.recipe_name


class BatchDeleteRecipeVersionResponse(TypedDict, closed=True):
    name: "capo_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe that was modified.</p>"""
    errors: NotRequired["capo_databrew.types.recipe_error_list.RecipeErrorList"]
    """<p>Errors, if any, that occurred while attempting to delete the recipe versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteRecipeVersionResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "errors" in value:
        import capo_databrew.types.recipe_error_list

        out["Errors"] = capo_databrew.types.recipe_error_list.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteRecipeVersionResponse:
    out: BatchDeleteRecipeVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Errors") is not None:
        import capo_databrew.types.recipe_error_list

        out["errors"] = capo_databrew.types.recipe_error_list.deserialize_json(
            data["Errors"]
        )
    return out
