"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationModelConfigs``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_model_config

EvaluationModelConfigs: TypeAlias = list[
    "capo_bedrock.types.evaluation_model_config.EvaluationModelConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationModelConfigs) -> list:
    import capo_bedrock.types.evaluation_model_config

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.evaluation_model_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluationModelConfigs:
    import capo_bedrock.types.evaluation_model_config

    out: EvaluationModelConfigs = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.evaluation_model_config.deserialize_json(item))
    return out


def redact_sensitive(value: EvaluationModelConfigs) -> list[Any]:
    import capo_bedrock.types.evaluation_model_config

    return [
        capo_bedrock.types.evaluation_model_config.redact_sensitive(item)
        for item in value
    ]
