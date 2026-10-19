"""Generated from Smithy shape ``com.amazonaws.databrew#ListRecipeVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.next_token
    import capo_databrew.types.recipe_list


class ListRecipeVersionsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_databrew.types.next_token.NextToken"]
    """<p>A token that you can use in a subsequent call to retrieve the next set of results.</p>"""
    recipes: "capo_databrew.types.recipe_list.RecipeList"
    """<p>A list of versions for the specified recipe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecipeVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_databrew.types.recipe_list

    out["Recipes"] = capo_databrew.types.recipe_list.serialize_json(value["recipes"])
    return out


def deserialize_json(data: dict) -> ListRecipeVersionsResponse:
    out: ListRecipeVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Recipes") is not None:
        import capo_databrew.types.recipe_list

        out["recipes"] = capo_databrew.types.recipe_list.deserialize_json(
            data["Recipes"]
        )
    else:
        out["recipes"] = []
    return out
