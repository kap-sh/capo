"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluatorConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.code_based_evaluator_config
    import capo_bedrock_agentcore_control.types.derived_evaluator_config
    import capo_bedrock_agentcore_control.types.llm_as_a_judge_evaluator_config


class _EvaluatorConfig_llmAsAJudge(TypedDict, closed=True):
    llmAsAJudge: "capo_bedrock_agentcore_control.types.llm_as_a_judge_evaluator_config.LlmAsAJudgeEvaluatorConfig"


class _EvaluatorConfig_codeBased(TypedDict, closed=True):
    codeBased: "capo_bedrock_agentcore_control.types.code_based_evaluator_config.CodeBasedEvaluatorConfig"


class _EvaluatorConfig_derived(TypedDict, closed=True):
    derived: "capo_bedrock_agentcore_control.types.derived_evaluator_config.DerivedEvaluatorConfig"


EvaluatorConfig: TypeAlias = (
    _EvaluatorConfig_llmAsAJudge
    | _EvaluatorConfig_codeBased
    | _EvaluatorConfig_derived
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EvaluatorConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "llmAsAJudge" in value:
        import capo_bedrock_agentcore_control.types.llm_as_a_judge_evaluator_config

        return {
            "llmAsAJudge": capo_bedrock_agentcore_control.types.llm_as_a_judge_evaluator_config.serialize_json(
                value["llmAsAJudge"]
            )
        }
    elif "codeBased" in value:
        import capo_bedrock_agentcore_control.types.code_based_evaluator_config

        return {
            "codeBased": capo_bedrock_agentcore_control.types.code_based_evaluator_config.serialize_json(
                value["codeBased"]
            )
        }
    elif "derived" in value:
        import capo_bedrock_agentcore_control.types.derived_evaluator_config

        return {
            "derived": capo_bedrock_agentcore_control.types.derived_evaluator_config.serialize_json(
                value["derived"]
            )
        }
    else:
        raise SerializationError("EvaluatorConfig: no variant present")


def deserialize_json(data: dict) -> EvaluatorConfig:
    if data.get("llmAsAJudge") is not None:
        import capo_bedrock_agentcore_control.types.llm_as_a_judge_evaluator_config

        return {
            "llmAsAJudge": capo_bedrock_agentcore_control.types.llm_as_a_judge_evaluator_config.deserialize_json(
                data["llmAsAJudge"]
            )
        }
    elif data.get("codeBased") is not None:
        import capo_bedrock_agentcore_control.types.code_based_evaluator_config

        return {
            "codeBased": capo_bedrock_agentcore_control.types.code_based_evaluator_config.deserialize_json(
                data["codeBased"]
            )
        }
    elif data.get("derived") is not None:
        import capo_bedrock_agentcore_control.types.derived_evaluator_config

        return {
            "derived": capo_bedrock_agentcore_control.types.derived_evaluator_config.deserialize_json(
                data["derived"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EvaluatorConfig: no recognized variant key")


def redact_sensitive(value: EvaluatorConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "llmAsAJudge" in value:
        import capo_bedrock_agentcore_control.types.llm_as_a_judge_evaluator_config

        out["llmAsAJudge"] = (
            capo_bedrock_agentcore_control.types.llm_as_a_judge_evaluator_config.redact_sensitive(
                value["llmAsAJudge"]
            )
        )
    return out
