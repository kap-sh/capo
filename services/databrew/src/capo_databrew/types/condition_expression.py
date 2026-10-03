"""Generated from Smithy shape ``com.amazonaws.databrew#ConditionExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.condition
    import capo_databrew.types.condition_value
    import capo_databrew.types.target_column


class ConditionExpression(TypedDict, closed=True):
    condition: "capo_databrew.types.condition.Condition"
    """<p>A specific condition to apply to a recipe action. For more information, see <a href="https://docs.aws.amazon.com/databrew/latest/dg/recipes.html#recipes.structure">Recipe structure</a> in the <i>Glue DataBrew Developer Guide</i>.</p>"""
    value: NotRequired["capo_databrew.types.condition_value.ConditionValue"]
    """<p>A value that the condition must evaluate to for the condition to succeed.</p>"""
    target_column: "capo_databrew.types.target_column.TargetColumn"
    """<p>A column to apply this condition to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionExpression) -> dict:
    out: dict = {}
    out["Condition"] = value["condition"]
    if "value" in value:
        out["Value"] = value["value"]
    out["TargetColumn"] = value["target_column"]
    return out


def deserialize_json(data: dict) -> ConditionExpression:
    out: ConditionExpression = {}  # type: ignore[typeddict-item]
    if data.get("Condition") is not None:
        out["condition"] = data["Condition"]
    else:
        raise DeserializationError("ConditionExpression.condition required")
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("TargetColumn") is not None:
        out["target_column"] = data["TargetColumn"]
    else:
        raise DeserializationError("ConditionExpression.target_column required")
    return out
