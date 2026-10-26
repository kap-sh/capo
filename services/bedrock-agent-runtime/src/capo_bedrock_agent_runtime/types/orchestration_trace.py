"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OrchestrationTrace``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.invocation_input
    import capo_bedrock_agent_runtime.types.model_invocation_input
    import capo_bedrock_agent_runtime.types.observation
    import capo_bedrock_agent_runtime.types.orchestration_model_invocation_output
    import capo_bedrock_agent_runtime.types.rationale


class _OrchestrationTrace_rationale(TypedDict, closed=True):
    rationale: "capo_bedrock_agent_runtime.types.rationale.Rationale"


class _OrchestrationTrace_invocationInput(TypedDict, closed=True):
    invocationInput: "capo_bedrock_agent_runtime.types.invocation_input.InvocationInput"


class _OrchestrationTrace_observation(TypedDict, closed=True):
    observation: "capo_bedrock_agent_runtime.types.observation.Observation"


class _OrchestrationTrace_modelInvocationInput(TypedDict, closed=True):
    modelInvocationInput: (
        "capo_bedrock_agent_runtime.types.model_invocation_input.ModelInvocationInput"
    )


class _OrchestrationTrace_modelInvocationOutput(TypedDict, closed=True):
    modelInvocationOutput: "capo_bedrock_agent_runtime.types.orchestration_model_invocation_output.OrchestrationModelInvocationOutput"


OrchestrationTrace: TypeAlias = (
    _OrchestrationTrace_rationale
    | _OrchestrationTrace_invocationInput
    | _OrchestrationTrace_observation
    | _OrchestrationTrace_modelInvocationInput
    | _OrchestrationTrace_modelInvocationOutput
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: OrchestrationTrace) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OrchestrationTrace: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "rationale" in value:
        import capo_bedrock_agent_runtime.types.rationale

        return {
            "rationale": capo_bedrock_agent_runtime.types.rationale.serialize_json(
                value["rationale"]
            )
        }
    elif "invocationInput" in value:
        import capo_bedrock_agent_runtime.types.invocation_input

        return {
            "invocationInput": capo_bedrock_agent_runtime.types.invocation_input.serialize_json(
                value["invocationInput"]
            )
        }
    elif "observation" in value:
        import capo_bedrock_agent_runtime.types.observation

        return {
            "observation": capo_bedrock_agent_runtime.types.observation.serialize_json(
                value["observation"]
            )
        }
    elif "modelInvocationInput" in value:
        import capo_bedrock_agent_runtime.types.model_invocation_input

        return {
            "modelInvocationInput": capo_bedrock_agent_runtime.types.model_invocation_input.serialize_json(
                value["modelInvocationInput"]
            )
        }
    elif "modelInvocationOutput" in value:
        import capo_bedrock_agent_runtime.types.orchestration_model_invocation_output

        return {
            "modelInvocationOutput": capo_bedrock_agent_runtime.types.orchestration_model_invocation_output.serialize_json(
                value["modelInvocationOutput"]
            )
        }
    else:
        raise SerializationError("OrchestrationTrace: no variant present")


def deserialize_json(data: dict) -> OrchestrationTrace:
    if data.get("rationale") is not None:
        import capo_bedrock_agent_runtime.types.rationale

        return {
            "rationale": capo_bedrock_agent_runtime.types.rationale.deserialize_json(
                data["rationale"]
            )
        }
    elif data.get("invocationInput") is not None:
        import capo_bedrock_agent_runtime.types.invocation_input

        return {
            "invocationInput": capo_bedrock_agent_runtime.types.invocation_input.deserialize_json(
                data["invocationInput"]
            )
        }
    elif data.get("observation") is not None:
        import capo_bedrock_agent_runtime.types.observation

        return {
            "observation": capo_bedrock_agent_runtime.types.observation.deserialize_json(
                data["observation"]
            )
        }
    elif data.get("modelInvocationInput") is not None:
        import capo_bedrock_agent_runtime.types.model_invocation_input

        return {
            "modelInvocationInput": capo_bedrock_agent_runtime.types.model_invocation_input.deserialize_json(
                data["modelInvocationInput"]
            )
        }
    elif data.get("modelInvocationOutput") is not None:
        import capo_bedrock_agent_runtime.types.orchestration_model_invocation_output

        return {
            "modelInvocationOutput": capo_bedrock_agent_runtime.types.orchestration_model_invocation_output.deserialize_json(
                data["modelInvocationOutput"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("OrchestrationTrace: no recognized variant key")
