"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DerivedEvaluatorConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.evaluator_id
    import capo_bedrock_agentcore_control.types.evaluator_model_config


class DerivedEvaluatorConfig(TypedDict, closed=True):
    base_evaluator_id: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId"
    """<p> The identifier of the base evaluator whose logic to run (a <code>Builtin.*</code> or <code>ThirdParty.*</code> evaluator). </p>"""
    model_config: "capo_bedrock_agentcore_control.types.evaluator_model_config.EvaluatorModelConfig"
    """<p> The configuration of the evaluator model that you supply. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DerivedEvaluatorConfig) -> dict:
    out: dict = {}
    out["baseEvaluatorId"] = value["base_evaluator_id"]
    import capo_bedrock_agentcore_control.types.evaluator_model_config

    out["modelConfig"] = (
        capo_bedrock_agentcore_control.types.evaluator_model_config.serialize_json(
            value["model_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> DerivedEvaluatorConfig:
    out: DerivedEvaluatorConfig = {}  # type: ignore[typeddict-item]
    if data.get("baseEvaluatorId") is not None:
        out["base_evaluator_id"] = data["baseEvaluatorId"]
    else:
        out["base_evaluator_id"] = ""
    if data.get("modelConfig") is not None:
        import capo_bedrock_agentcore_control.types.evaluator_model_config

        out["model_config"] = (
            capo_bedrock_agentcore_control.types.evaluator_model_config.deserialize_json(
                data["modelConfig"]
            )
        )
    else:
        import capo_bedrock_agentcore_control.types._unknown

        out["model_config"] = (
            capo_bedrock_agentcore_control.types._unknown.UnknownUnionMember("")
        )
    return out
