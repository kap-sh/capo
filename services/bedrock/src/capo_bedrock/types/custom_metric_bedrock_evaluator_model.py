"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomMetricBedrockEvaluatorModel``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.evaluator_model_identifier


class CustomMetricBedrockEvaluatorModel(TypedDict, closed=True):
    model_identifier: (
        "capo_bedrock.types.evaluator_model_identifier.EvaluatorModelIdentifier"
    )
    """<p>The Amazon Resource Name (ARN) of the evaluator model for custom metrics. For a list of supported evaluator models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html">Evaluate model performance using another LLM as a judge</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html">Evaluate the performance of RAG sources using Amazon Bedrock evaluations</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomMetricBedrockEvaluatorModel) -> dict:
    out: dict = {}
    out["modelIdentifier"] = value["model_identifier"]
    return out


def deserialize_json(data: dict) -> CustomMetricBedrockEvaluatorModel:
    out: CustomMetricBedrockEvaluatorModel = {}  # type: ignore[typeddict-item]
    if data.get("modelIdentifier") is not None:
        out["model_identifier"] = data["modelIdentifier"]
    else:
        raise DeserializationError(
            "CustomMetricBedrockEvaluatorModel.model_identifier required"
        )
    return out
