"""Generated from Smithy shape ``com.amazonaws.databrew#UpdateRecipeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.recipe_name


class UpdateRecipeResponse(TypedDict, closed=True):
    name: "capo_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecipeResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateRecipeResponse:
    out: UpdateRecipeResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
