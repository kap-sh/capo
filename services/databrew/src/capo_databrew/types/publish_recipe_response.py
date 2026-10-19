"""Generated from Smithy shape ``com.amazonaws.databrew#PublishRecipeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.recipe_name


class PublishRecipeResponse(TypedDict, closed=True):
    name: "capo_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe that you published.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishRecipeResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> PublishRecipeResponse:
    out: PublishRecipeResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
