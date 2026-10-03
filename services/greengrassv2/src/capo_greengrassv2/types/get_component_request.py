"""Generated from Smithy shape ``com.amazonaws.greengrassv2#GetComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_version_arn
    import capo_greengrassv2.types.recipe_output_format


class GetComponentRequest(TypedDict, closed=True):
    recipe_output_format: NotRequired[
        "capo_greengrassv2.types.recipe_output_format.RecipeOutputFormat"
    ]
    """<p>The format of the recipe.</p>"""
    arn: "capo_greengrassv2.types.component_version_arn.ComponentVersionARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the component version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetComponentRequest:
    out: GetComponentRequest = {}  # type: ignore[typeddict-item]
    return out
