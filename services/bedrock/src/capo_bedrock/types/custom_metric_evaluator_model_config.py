"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomMetricEvaluatorModelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.custom_metric_bedrock_evaluator_models


class CustomMetricEvaluatorModelConfig(TypedDict, closed=True):
    bedrock_evaluator_models: "capo_bedrock.types.custom_metric_bedrock_evaluator_models.CustomMetricBedrockEvaluatorModels"
    """<p>Defines the model you want to evaluate custom metrics in an Amazon Bedrock evaluation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomMetricEvaluatorModelConfig) -> dict:
    out: dict = {}
    import capo_bedrock.types.custom_metric_bedrock_evaluator_models

    out["bedrockEvaluatorModels"] = (
        capo_bedrock.types.custom_metric_bedrock_evaluator_models.serialize_json(
            value["bedrock_evaluator_models"]
        )
    )
    return out


def deserialize_json(data: dict) -> CustomMetricEvaluatorModelConfig:
    out: CustomMetricEvaluatorModelConfig = {}  # type: ignore[typeddict-item]
    if data.get("bedrockEvaluatorModels") is not None:
        import capo_bedrock.types.custom_metric_bedrock_evaluator_models

        out["bedrock_evaluator_models"] = (
            capo_bedrock.types.custom_metric_bedrock_evaluator_models.deserialize_json(
                data["bedrockEvaluatorModels"]
            )
        )
    else:
        out["bedrock_evaluator_models"] = []
    return out
