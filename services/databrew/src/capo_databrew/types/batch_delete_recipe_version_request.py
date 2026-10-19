"""Generated from Smithy shape ``com.amazonaws.databrew#BatchDeleteRecipeVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.recipe_name
    import capo_databrew.types.recipe_version_list


class BatchDeleteRecipeVersionRequest(TypedDict, closed=True):
    name: "capo_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe whose versions are to be deleted.</p>"""
    recipe_versions: "capo_databrew.types.recipe_version_list.RecipeVersionList"
    """<p>An array of version identifiers, for the recipe versions to be deleted. You can specify numeric versions (<code>X.Y</code>) or <code>LATEST_WORKING</code>. <code>LATEST_PUBLISHED</code> is not supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteRecipeVersionRequest) -> dict:
    out: dict = {}
    import capo_databrew.types.recipe_version_list

    out["RecipeVersions"] = capo_databrew.types.recipe_version_list.serialize_json(
        value["recipe_versions"]
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteRecipeVersionRequest:
    out: BatchDeleteRecipeVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("RecipeVersions") is not None:
        import capo_databrew.types.recipe_version_list

        out["recipe_versions"] = (
            capo_databrew.types.recipe_version_list.deserialize_json(
                data["RecipeVersions"]
            )
        )
    else:
        out["recipe_versions"] = []
    return out
