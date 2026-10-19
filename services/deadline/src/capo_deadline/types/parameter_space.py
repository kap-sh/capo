"""Generated from Smithy shape ``com.amazonaws.deadline#ParameterSpace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.combination_expression
    import capo_deadline.types.step_parameter_list


class ParameterSpace(TypedDict, closed=True):
    parameters: "capo_deadline.types.step_parameter_list.StepParameterList"
    """<p>The parameters to search for.</p>"""
    combination: NotRequired[
        "capo_deadline.types.combination_expression.CombinationExpression"
    ]
    """<p>The combination expression to use in the search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterSpace) -> dict:
    out: dict = {}
    import capo_deadline.types.step_parameter_list

    out["parameters"] = capo_deadline.types.step_parameter_list.serialize_json(
        value["parameters"]
    )
    if "combination" in value:
        out["combination"] = value["combination"]
    return out


def deserialize_json(data: dict) -> ParameterSpace:
    out: ParameterSpace = {}  # type: ignore[typeddict-item]
    if data.get("parameters") is not None:
        import capo_deadline.types.step_parameter_list

        out["parameters"] = capo_deadline.types.step_parameter_list.deserialize_json(
            data["parameters"]
        )
    else:
        out["parameters"] = []
    if data.get("combination") is not None:
        out["combination"] = data["combination"]
    return out
