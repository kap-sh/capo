"""Generated from Smithy shape ``com.amazonaws.databrew#ListRecipesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.next_token
    import capo_databrew.types.recipe_list


class ListRecipesResponse(TypedDict, closed=True):
    recipes: "capo_databrew.types.recipe_list.RecipeList"
    """<p>A list of recipes that are defined.</p>"""
    next_token: NotRequired["capo_databrew.types.next_token.NextToken"]
    """<p>A token that you can use in a subsequent call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecipesResponse) -> dict:
    out: dict = {}
    import capo_databrew.types.recipe_list

    out["Recipes"] = capo_databrew.types.recipe_list.serialize_json(value["recipes"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecipesResponse:
    out: ListRecipesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Recipes") is not None:
        import capo_databrew.types.recipe_list

        out["recipes"] = capo_databrew.types.recipe_list.deserialize_json(
            data["Recipes"]
        )
    else:
        out["recipes"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
