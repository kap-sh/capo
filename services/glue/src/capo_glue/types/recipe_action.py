"""Generated from Smithy shape ``com.amazonaws.glue#RecipeAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.operation
    import capo_glue.types.parameter_map


class RecipeAction(TypedDict, closed=True):
    operation: "capo_glue.types.operation.Operation"
    """<p>The operation of the recipe action.</p>"""
    parameters: NotRequired["capo_glue.types.parameter_map.ParameterMap"]
    """<p>The parameters of the recipe action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecipeAction) -> dict:
    out: dict = {}
    out["Operation"] = value["operation"]
    if "parameters" in value:
        import capo_glue.types.parameter_map

        out["Parameters"] = capo_glue.types.parameter_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecipeAction:
    out: RecipeAction = {}  # type: ignore[typeddict-item]
    if data.get("Operation") is not None:
        out["operation"] = data["Operation"]
    else:
        out["operation"] = ""
    if data.get("Parameters") is not None:
        import capo_glue.types.parameter_map

        out["parameters"] = capo_glue.types.parameter_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    return out
