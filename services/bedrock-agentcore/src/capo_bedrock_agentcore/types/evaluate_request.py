"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluateRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.evaluation_input
    import capo_bedrock_agentcore.types.evaluation_reference_inputs
    import capo_bedrock_agentcore.types.evaluation_target
    import capo_bedrock_agentcore.types.evaluator_id


class EvaluateRequest(TypedDict, closed=True):
    evaluator_id: "capo_bedrock_agentcore.types.evaluator_id.EvaluatorId"
    """<p> The unique identifier of the evaluator to use for scoring. Can be a built-in evaluator (e.g., <code>Builtin.Helpfulness</code>, <code>Builtin.Correctness</code>) or a custom evaluator Id created through the control plane API. </p>"""
    evaluation_input: "capo_bedrock_agentcore.types.evaluation_input.EvaluationInput"
    """<p> The input data containing agent session spans to be evaluated. Includes a list of spans in OpenTelemetry format from supported frameworks like Strands (AgentCore Runtime) or LangGraph with OpenInference instrumentation. </p>"""
    evaluation_target: NotRequired[
        "capo_bedrock_agentcore.types.evaluation_target.EvaluationTarget"
    ]
    """<p> The specific trace or span IDs to evaluate within the provided input. Allows targeting evaluation at different levels: individual tool calls, single request-response interactions (traces), or entire conversation sessions. </p>"""
    evaluation_reference_inputs: NotRequired[
        "capo_bedrock_agentcore.types.evaluation_reference_inputs.EvaluationReferenceInputs"
    ]
    """<p> Ground truth data to compare against agent responses during evaluation. Allows to provide expected responses, assertions, and expected tool trajectories at different evaluation levels. Session-level reference inputs apply to the entire conversation, while trace-level reference inputs target specific request-response interactions identified by trace ID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluateRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.evaluation_input

    out["evaluationInput"] = (
        capo_bedrock_agentcore.types.evaluation_input.serialize_json(
            value["evaluation_input"]
        )
    )
    if "evaluation_target" in value:
        import capo_bedrock_agentcore.types.evaluation_target

        out["evaluationTarget"] = (
            capo_bedrock_agentcore.types.evaluation_target.serialize_json(
                value["evaluation_target"]
            )
        )
    if "evaluation_reference_inputs" in value:
        import capo_bedrock_agentcore.types.evaluation_reference_inputs

        out["evaluationReferenceInputs"] = (
            capo_bedrock_agentcore.types.evaluation_reference_inputs.serialize_json(
                value["evaluation_reference_inputs"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluateRequest:
    out: EvaluateRequest = {}  # type: ignore[typeddict-item]
    if data.get("evaluationInput") is not None:
        import capo_bedrock_agentcore.types.evaluation_input

        out["evaluation_input"] = (
            capo_bedrock_agentcore.types.evaluation_input.deserialize_json(
                data["evaluationInput"]
            )
        )
    else:
        out["evaluation_input"] = {"$unknown": {"name": ""}}
    if data.get("evaluationTarget") is not None:
        import capo_bedrock_agentcore.types.evaluation_target

        out["evaluation_target"] = (
            capo_bedrock_agentcore.types.evaluation_target.deserialize_json(
                data["evaluationTarget"]
            )
        )
    if data.get("evaluationReferenceInputs") is not None:
        import capo_bedrock_agentcore.types.evaluation_reference_inputs

        out["evaluation_reference_inputs"] = (
            capo_bedrock_agentcore.types.evaluation_reference_inputs.deserialize_json(
                data["evaluationReferenceInputs"]
            )
        )
    return out


def redact_sensitive(value: EvaluateRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "evaluation_input" in value:
        import capo_bedrock_agentcore.types.evaluation_input

        out["evaluation_input"] = (
            capo_bedrock_agentcore.types.evaluation_input.redact_sensitive(
                value["evaluation_input"]
            )
        )
    if "evaluation_reference_inputs" in value:
        out["evaluation_reference_inputs"] = "*** Sensitive Data Redacted ***"
    return out
