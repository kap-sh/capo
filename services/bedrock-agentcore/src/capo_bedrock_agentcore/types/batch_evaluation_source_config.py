"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BatchEvaluationSourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.batch_evaluation_arn


class BatchEvaluationSourceConfig(TypedDict, closed=True):
    batch_evaluation_arn: (
        "capo_bedrock_agentcore.types.batch_evaluation_arn.BatchEvaluationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the batch evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchEvaluationSourceConfig) -> dict:
    out: dict = {}
    out["batchEvaluationArn"] = value["batch_evaluation_arn"]
    return out


def deserialize_json(data: dict) -> BatchEvaluationSourceConfig:
    out: BatchEvaluationSourceConfig = {}  # type: ignore[typeddict-item]
    if data.get("batchEvaluationArn") is not None:
        out["batch_evaluation_arn"] = data["batchEvaluationArn"]
    else:
        out["batch_evaluation_arn"] = ""
    return out
