"""Generated from Smithy shape ``com.amazonaws.bedrock#BedrockEvaluatorModel``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.evaluator_model_identifier


class BedrockEvaluatorModel(TypedDict, closed=True):
    model_identifier: (
        "capo_bedrock.types.evaluator_model_identifier.EvaluatorModelIdentifier"
    )
    """<p>The Amazon Resource Name (ARN) of the evaluator model used used in knowledge base evaluation job or in model evaluation job that use a model as judge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockEvaluatorModel) -> dict:
    out: dict = {}
    out["modelIdentifier"] = value["model_identifier"]
    return out


def deserialize_json(data: dict) -> BedrockEvaluatorModel:
    out: BedrockEvaluatorModel = {}  # type: ignore[typeddict-item]
    if data.get("modelIdentifier") is not None:
        out["model_identifier"] = data["modelIdentifier"]
    else:
        out["model_identifier"] = ""
    return out
