"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Trace``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.custom_orchestration_trace
    import capo_bedrock_agent_runtime.types.failure_trace
    import capo_bedrock_agent_runtime.types.guardrail_trace
    import capo_bedrock_agent_runtime.types.orchestration_trace
    import capo_bedrock_agent_runtime.types.post_processing_trace
    import capo_bedrock_agent_runtime.types.pre_processing_trace
    import capo_bedrock_agent_runtime.types.routing_classifier_trace


class _Trace_guardrailTrace(TypedDict, closed=True):
    guardrailTrace: "capo_bedrock_agent_runtime.types.guardrail_trace.GuardrailTrace"


class _Trace_preProcessingTrace(TypedDict, closed=True):
    preProcessingTrace: (
        "capo_bedrock_agent_runtime.types.pre_processing_trace.PreProcessingTrace"
    )


class _Trace_orchestrationTrace(TypedDict, closed=True):
    orchestrationTrace: (
        "capo_bedrock_agent_runtime.types.orchestration_trace.OrchestrationTrace"
    )


class _Trace_postProcessingTrace(TypedDict, closed=True):
    postProcessingTrace: (
        "capo_bedrock_agent_runtime.types.post_processing_trace.PostProcessingTrace"
    )


class _Trace_routingClassifierTrace(TypedDict, closed=True):
    routingClassifierTrace: "capo_bedrock_agent_runtime.types.routing_classifier_trace.RoutingClassifierTrace"


class _Trace_failureTrace(TypedDict, closed=True):
    failureTrace: "capo_bedrock_agent_runtime.types.failure_trace.FailureTrace"


class _Trace_customOrchestrationTrace(TypedDict, closed=True):
    customOrchestrationTrace: "capo_bedrock_agent_runtime.types.custom_orchestration_trace.CustomOrchestrationTrace"


Trace: TypeAlias = (
    _Trace_guardrailTrace
    | _Trace_preProcessingTrace
    | _Trace_orchestrationTrace
    | _Trace_postProcessingTrace
    | _Trace_routingClassifierTrace
    | _Trace_failureTrace
    | _Trace_customOrchestrationTrace
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Trace) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Trace: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "guardrailTrace" in value:
        import capo_bedrock_agent_runtime.types.guardrail_trace

        return {
            "guardrailTrace": capo_bedrock_agent_runtime.types.guardrail_trace.serialize_json(
                value["guardrailTrace"]
            )
        }
    elif "preProcessingTrace" in value:
        import capo_bedrock_agent_runtime.types.pre_processing_trace

        return {
            "preProcessingTrace": capo_bedrock_agent_runtime.types.pre_processing_trace.serialize_json(
                value["preProcessingTrace"]
            )
        }
    elif "orchestrationTrace" in value:
        import capo_bedrock_agent_runtime.types.orchestration_trace

        return {
            "orchestrationTrace": capo_bedrock_agent_runtime.types.orchestration_trace.serialize_json(
                value["orchestrationTrace"]
            )
        }
    elif "postProcessingTrace" in value:
        import capo_bedrock_agent_runtime.types.post_processing_trace

        return {
            "postProcessingTrace": capo_bedrock_agent_runtime.types.post_processing_trace.serialize_json(
                value["postProcessingTrace"]
            )
        }
    elif "routingClassifierTrace" in value:
        import capo_bedrock_agent_runtime.types.routing_classifier_trace

        return {
            "routingClassifierTrace": capo_bedrock_agent_runtime.types.routing_classifier_trace.serialize_json(
                value["routingClassifierTrace"]
            )
        }
    elif "failureTrace" in value:
        import capo_bedrock_agent_runtime.types.failure_trace

        return {
            "failureTrace": capo_bedrock_agent_runtime.types.failure_trace.serialize_json(
                value["failureTrace"]
            )
        }
    elif "customOrchestrationTrace" in value:
        import capo_bedrock_agent_runtime.types.custom_orchestration_trace

        return {
            "customOrchestrationTrace": capo_bedrock_agent_runtime.types.custom_orchestration_trace.serialize_json(
                value["customOrchestrationTrace"]
            )
        }
    else:
        raise SerializationError("Trace: no variant present")


def deserialize_json(data: dict) -> Trace:
    if data.get("guardrailTrace") is not None:
        import capo_bedrock_agent_runtime.types.guardrail_trace

        return {
            "guardrailTrace": capo_bedrock_agent_runtime.types.guardrail_trace.deserialize_json(
                data["guardrailTrace"]
            )
        }
    elif data.get("preProcessingTrace") is not None:
        import capo_bedrock_agent_runtime.types.pre_processing_trace

        return {
            "preProcessingTrace": capo_bedrock_agent_runtime.types.pre_processing_trace.deserialize_json(
                data["preProcessingTrace"]
            )
        }
    elif data.get("orchestrationTrace") is not None:
        import capo_bedrock_agent_runtime.types.orchestration_trace

        return {
            "orchestrationTrace": capo_bedrock_agent_runtime.types.orchestration_trace.deserialize_json(
                data["orchestrationTrace"]
            )
        }
    elif data.get("postProcessingTrace") is not None:
        import capo_bedrock_agent_runtime.types.post_processing_trace

        return {
            "postProcessingTrace": capo_bedrock_agent_runtime.types.post_processing_trace.deserialize_json(
                data["postProcessingTrace"]
            )
        }
    elif data.get("routingClassifierTrace") is not None:
        import capo_bedrock_agent_runtime.types.routing_classifier_trace

        return {
            "routingClassifierTrace": capo_bedrock_agent_runtime.types.routing_classifier_trace.deserialize_json(
                data["routingClassifierTrace"]
            )
        }
    elif data.get("failureTrace") is not None:
        import capo_bedrock_agent_runtime.types.failure_trace

        return {
            "failureTrace": capo_bedrock_agent_runtime.types.failure_trace.deserialize_json(
                data["failureTrace"]
            )
        }
    elif data.get("customOrchestrationTrace") is not None:
        import capo_bedrock_agent_runtime.types.custom_orchestration_trace

        return {
            "customOrchestrationTrace": capo_bedrock_agent_runtime.types.custom_orchestration_trace.deserialize_json(
                data["customOrchestrationTrace"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Trace: no recognized variant key")
