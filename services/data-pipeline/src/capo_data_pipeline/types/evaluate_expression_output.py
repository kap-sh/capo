"""Generated from Smithy shape ``com.amazonaws.datapipeline#EvaluateExpressionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.long_string


class EvaluateExpressionOutput(TypedDict, closed=True):
    evaluated_expression: "capo_data_pipeline.types.long_string.longString"
    """<p>The evaluated expression.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluateExpressionOutput) -> dict:
    out: dict = {}
    out["evaluatedExpression"] = value["evaluated_expression"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluateExpressionOutput:
    out: EvaluateExpressionOutput = {}  # type: ignore[typeddict-item]
    if data.get("evaluatedExpression") is not None:
        out["evaluated_expression"] = data["evaluatedExpression"]
    else:
        out["evaluated_expression"] = ""
    return out
