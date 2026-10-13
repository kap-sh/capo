"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_evaluation_config
    import capo_bedrock.types.human_evaluation_config


class _EvaluationConfig_automated(TypedDict, closed=True):
    automated: (
        "capo_bedrock.types.automated_evaluation_config.AutomatedEvaluationConfig"
    )


class _EvaluationConfig_human(TypedDict, closed=True):
    human: "capo_bedrock.types.human_evaluation_config.HumanEvaluationConfig"


EvaluationConfig: TypeAlias = _EvaluationConfig_automated | _EvaluationConfig_human


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationConfig) -> dict:
    if "automated" in value:
        import capo_bedrock.types.automated_evaluation_config

        return {
            "automated": capo_bedrock.types.automated_evaluation_config.serialize_json(
                value["automated"]
            )
        }
    elif "human" in value:
        import capo_bedrock.types.human_evaluation_config

        return {
            "human": capo_bedrock.types.human_evaluation_config.serialize_json(
                value["human"]
            )
        }
    else:
        raise SerializationError("EvaluationConfig: no variant present")


def deserialize_json(data: dict) -> EvaluationConfig:
    if data.get("automated") is not None:
        import capo_bedrock.types.automated_evaluation_config

        return {
            "automated": capo_bedrock.types.automated_evaluation_config.deserialize_json(
                data["automated"]
            )
        }
    elif data.get("human") is not None:
        import capo_bedrock.types.human_evaluation_config

        return {
            "human": capo_bedrock.types.human_evaluation_config.deserialize_json(
                data["human"]
            )
        }
    else:
        raise DeserializationError("EvaluationConfig: no recognized variant key")


def redact_sensitive(value: EvaluationConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "automated" in value:
        import capo_bedrock.types.automated_evaluation_config

        out["automated"] = (
            capo_bedrock.types.automated_evaluation_config.redact_sensitive(
                value["automated"]
            )
        )
    if "human" in value:
        import capo_bedrock.types.human_evaluation_config

        out["human"] = capo_bedrock.types.human_evaluation_config.redact_sensitive(
            value["human"]
        )
    return out
