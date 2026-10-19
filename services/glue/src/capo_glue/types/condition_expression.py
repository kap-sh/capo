"""Generated from Smithy shape ``com.amazonaws.glue#ConditionExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.databrew_condition
    import capo_glue.types.databrew_condition_value
    import capo_glue.types.target_column


class ConditionExpression(TypedDict, closed=True):
    condition: "capo_glue.types.databrew_condition.DatabrewCondition"
    """<p>The condition of the condition expression.</p>"""
    value: NotRequired[
        "capo_glue.types.databrew_condition_value.DatabrewConditionValue"
    ]
    """<p>The value of the condition expression.</p>"""
    target_column: "capo_glue.types.target_column.TargetColumn"
    """<p>The target column of the condition expressions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionExpression) -> dict:
    out: dict = {}
    out["Condition"] = value["condition"]
    if "value" in value:
        out["Value"] = value["value"]
    out["TargetColumn"] = value["target_column"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConditionExpression:
    out: ConditionExpression = {}  # type: ignore[typeddict-item]
    if data.get("Condition") is not None:
        out["condition"] = data["Condition"]
    else:
        out["condition"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("TargetColumn") is not None:
        out["target_column"] = data["TargetColumn"]
    else:
        out["target_column"] = ""
    return out
