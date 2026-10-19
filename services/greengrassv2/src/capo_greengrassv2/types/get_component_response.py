"""Generated from Smithy shape ``com.amazonaws.greengrassv2#GetComponentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.recipe_blob
    import capo_greengrassv2.types.recipe_output_format
    import capo_greengrassv2.types.tag_map


class GetComponentResponse(TypedDict, closed=True):
    recipe_output_format: (
        "capo_greengrassv2.types.recipe_output_format.RecipeOutputFormat"
    )
    """<p>The format of the recipe.</p>"""
    recipe: "capo_greengrassv2.types.recipe_blob.RecipeBlob"
    """<p>The recipe of the component version.</p>"""
    tags: NotRequired["capo_greengrassv2.types.tag_map.TagMap"]
    """<p>A list of key-value pairs that contain metadata for the resource. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html">Tag your resources</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentResponse) -> dict:
    out: dict = {}
    import capo_greengrassv2.types.recipe_output_format

    out["recipeOutputFormat"] = (
        capo_greengrassv2.types.recipe_output_format.serialize_json(
            value["recipe_output_format"]
        )
    )
    import capo_greengrassv2.types.recipe_blob

    out["recipe"] = capo_greengrassv2.types.recipe_blob.serialize_json(value["recipe"])
    if "tags" in value:
        import capo_greengrassv2.types.tag_map

        out["tags"] = capo_greengrassv2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetComponentResponse:
    out: GetComponentResponse = {}  # type: ignore[typeddict-item]
    if data.get("recipeOutputFormat") is not None:
        import capo_greengrassv2.types.recipe_output_format

        out["recipe_output_format"] = (
            capo_greengrassv2.types.recipe_output_format.deserialize_json(
                data["recipeOutputFormat"]
            )
        )
    else:
        import typing

        out["recipe_output_format"] = typing.cast(
            "capo_greengrassv2.types.recipe_output_format.RecipeOutputFormat", ""
        )
    if data.get("recipe") is not None:
        import capo_greengrassv2.types.recipe_blob

        out["recipe"] = capo_greengrassv2.types.recipe_blob.deserialize_json(
            data["recipe"]
        )
    else:
        out["recipe"] = b""
    if data.get("tags") is not None:
        import capo_greengrassv2.types.tag_map

        out["tags"] = capo_greengrassv2.types.tag_map.deserialize_json(data["tags"])
    return out
