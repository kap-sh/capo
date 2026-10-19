"""Generated from Smithy shape ``com.amazonaws.databrew#RecipeAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.operation
    import capo_databrew.types.parameter_map


class RecipeAction(TypedDict, closed=True):
    operation: "capo_databrew.types.operation.Operation"
    """<p>The name of a valid DataBrew transformation to be performed on the data.</p>"""
    parameters: NotRequired["capo_databrew.types.parameter_map.ParameterMap"]
    """<p>Contextual parameters for the transformation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecipeAction) -> dict:
    out: dict = {}
    out["Operation"] = value["operation"]
    if "parameters" in value:
        import capo_databrew.types.parameter_map

        out["Parameters"] = capo_databrew.types.parameter_map.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> RecipeAction:
    out: RecipeAction = {}  # type: ignore[typeddict-item]
    if data.get("Operation") is not None:
        out["operation"] = data["Operation"]
    else:
        out["operation"] = ""
    if data.get("Parameters") is not None:
        import capo_databrew.types.parameter_map

        out["parameters"] = capo_databrew.types.parameter_map.deserialize_json(
            data["Parameters"]
        )
    return out
