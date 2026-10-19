"""Generated from Smithy shape ``com.amazonaws.frauddetector#LogOddsMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.float
    import capo_frauddetector.types.string


class LogOddsMetric(TypedDict, closed=True):
    variable_name: "capo_frauddetector.types.string.string"
    """<p>The name of the variable.</p>"""
    variable_type: "capo_frauddetector.types.string.string"
    """<p>The type of variable.</p>"""
    variable_importance: "capo_frauddetector.types.float.float"
    """<p>The relative importance of the variable. For more information, see <a href="https://docs.aws.amazon.com/frauddetector/latest/ug/model-variable-importance.html">Model variable importance</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogOddsMetric) -> dict:
    out: dict = {}
    out["variableName"] = value["variable_name"]
    out["variableType"] = value["variable_type"]
    out["variableImportance"] = (
        "NaN"
        if value["variable_importance"] != value["variable_importance"]
        else "Infinity"
        if value["variable_importance"] == float("inf")
        else "-Infinity"
        if value["variable_importance"] == float("-inf")
        else value["variable_importance"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogOddsMetric:
    out: LogOddsMetric = {}  # type: ignore[typeddict-item]
    if data.get("variableName") is not None:
        out["variable_name"] = data["variableName"]
    else:
        out["variable_name"] = ""
    if data.get("variableType") is not None:
        out["variable_type"] = data["variableType"]
    else:
        out["variable_type"] = ""
    if data.get("variableImportance") is not None:
        out["variable_importance"] = float(data["variableImportance"])
    else:
        out["variable_importance"] = 0.0
    return out
