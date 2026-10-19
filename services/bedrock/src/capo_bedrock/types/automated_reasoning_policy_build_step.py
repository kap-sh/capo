"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildStep``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_build_step_context
    import capo_bedrock.types.automated_reasoning_policy_build_step_message_list
    import capo_bedrock.types.automated_reasoning_policy_definition_element


class AutomatedReasoningPolicyBuildStep(TypedDict, closed=True):
    context: "capo_bedrock.types.automated_reasoning_policy_build_step_context.AutomatedReasoningPolicyBuildStepContext"
    """<p>Contextual information about what was being processed during this build step, such as the type of operation or the source material being analyzed.</p>"""
    prior_element: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_element.AutomatedReasoningPolicyDefinitionElement"
    ]
    """<p>Reference to the previous element or step in the build process, helping to trace the sequence of operations.</p>"""
    messages: "capo_bedrock.types.automated_reasoning_policy_build_step_message_list.AutomatedReasoningPolicyBuildStepMessageList"
    """<p>A list of messages generated during this build step, including informational messages, warnings, and error details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildStep) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_build_step_context

    out["context"] = (
        capo_bedrock.types.automated_reasoning_policy_build_step_context.serialize_json(
            value["context"]
        )
    )
    if "prior_element" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_element

        out["priorElement"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_element.serialize_json(
                value["prior_element"]
            )
        )
    import capo_bedrock.types.automated_reasoning_policy_build_step_message_list

    out["messages"] = (
        capo_bedrock.types.automated_reasoning_policy_build_step_message_list.serialize_json(
            value["messages"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildStep:
    out: AutomatedReasoningPolicyBuildStep = {}  # type: ignore[typeddict-item]
    if data.get("context") is not None:
        import capo_bedrock.types.automated_reasoning_policy_build_step_context

        out["context"] = (
            capo_bedrock.types.automated_reasoning_policy_build_step_context.deserialize_json(
                data["context"]
            )
        )
    else:
        import capo_bedrock.types._unknown

        out["context"] = capo_bedrock.types._unknown.UnknownUnionMember("")
    if data.get("priorElement") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_element

        out["prior_element"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_element.deserialize_json(
                data["priorElement"]
            )
        )
    if data.get("messages") is not None:
        import capo_bedrock.types.automated_reasoning_policy_build_step_message_list

        out["messages"] = (
            capo_bedrock.types.automated_reasoning_policy_build_step_message_list.deserialize_json(
                data["messages"]
            )
        )
    else:
        out["messages"] = []
    return out


def redact_sensitive(value: AutomatedReasoningPolicyBuildStep) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "context" in value:
        import capo_bedrock.types.automated_reasoning_policy_build_step_context

        out["context"] = (
            capo_bedrock.types.automated_reasoning_policy_build_step_context.redact_sensitive(
                value["context"]
            )
        )
    if "prior_element" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_element

        out["prior_element"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_element.redact_sensitive(
                value["prior_element"]
            )
        )
    return out
