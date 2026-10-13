"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseStreamTrace``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_trace_assessment
    import capo_bedrock_runtime.types.prompt_router_trace


class ConverseStreamTrace(TypedDict, closed=True):
    guardrail: NotRequired[
        "capo_bedrock_runtime.types.guardrail_trace_assessment.GuardrailTraceAssessment"
    ]
    """<p>The guardrail trace object. </p>"""
    prompt_router: NotRequired[
        "capo_bedrock_runtime.types.prompt_router_trace.PromptRouterTrace"
    ]
    """<p>The request's prompt router.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConverseStreamTrace) -> dict:
    out: dict = {}
    if "guardrail" in value:
        import capo_bedrock_runtime.types.guardrail_trace_assessment

        out["guardrail"] = (
            capo_bedrock_runtime.types.guardrail_trace_assessment.serialize_json(
                value["guardrail"]
            )
        )
    if "prompt_router" in value:
        import capo_bedrock_runtime.types.prompt_router_trace

        out["promptRouter"] = (
            capo_bedrock_runtime.types.prompt_router_trace.serialize_json(
                value["prompt_router"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConverseStreamTrace:
    out: ConverseStreamTrace = {}  # type: ignore[typeddict-item]
    if data.get("guardrail") is not None:
        import capo_bedrock_runtime.types.guardrail_trace_assessment

        out["guardrail"] = (
            capo_bedrock_runtime.types.guardrail_trace_assessment.deserialize_json(
                data["guardrail"]
            )
        )
    if data.get("promptRouter") is not None:
        import capo_bedrock_runtime.types.prompt_router_trace

        out["prompt_router"] = (
            capo_bedrock_runtime.types.prompt_router_trace.deserialize_json(
                data["promptRouter"]
            )
        )
    return out


def redact_sensitive(value: ConverseStreamTrace) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "guardrail" in value:
        import capo_bedrock_runtime.types.guardrail_trace_assessment

        out["guardrail"] = (
            capo_bedrock_runtime.types.guardrail_trace_assessment.redact_sensitive(
                value["guardrail"]
            )
        )
    return out
