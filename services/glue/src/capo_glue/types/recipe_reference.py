"""Generated from Smithy shape ``com.amazonaws.glue#RecipeReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.recipe_version


class RecipeReference(TypedDict, closed=True):
    recipe_arn: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The ARN of the DataBrew recipe.</p>"""
    recipe_version: "capo_glue.types.recipe_version.RecipeVersion"
    """<p>The RecipeVersion of the DataBrew recipe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecipeReference) -> dict:
    out: dict = {}
    out["RecipeArn"] = value["recipe_arn"]
    out["RecipeVersion"] = value["recipe_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecipeReference:
    out: RecipeReference = {}  # type: ignore[typeddict-item]
    if data.get("RecipeArn") is not None:
        out["recipe_arn"] = data["RecipeArn"]
    else:
        out["recipe_arn"] = ""
    if data.get("RecipeVersion") is not None:
        out["recipe_version"] = data["RecipeVersion"]
    else:
        out["recipe_version"] = ""
    return out
