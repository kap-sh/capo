"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeRecipeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DescribeRecipeRequest(TypedDict, closed=True):
    recipe_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the recipe to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRecipeRequest) -> dict:
    out: dict = {}
    out["recipeArn"] = value["recipe_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRecipeRequest:
    out: DescribeRecipeRequest = {}  # type: ignore[typeddict-item]
    if data.get("recipeArn") is not None:
        out["recipe_arn"] = data["recipeArn"]
    else:
        out["recipe_arn"] = ""
    return out
