"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildWorkflowSource``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition
    import capo_bedrock.types.automated_reasoning_policy_workflow_type_content


class AutomatedReasoningPolicyBuildWorkflowSource(TypedDict, closed=True):
    policy_definition: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition.AutomatedReasoningPolicyDefinition"
    ]
    """<p>An existing policy definition that serves as the starting point for the build workflow, typically used in policy repair or update scenarios.</p>"""
    workflow_content: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_workflow_type_content.AutomatedReasoningPolicyWorkflowTypeContent"
    ]
    """<p>The actual content to be processed in the build workflow, such as documents to analyze or repair instructions to apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildWorkflowSource) -> dict:
    out: dict = {}
    if "policy_definition" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition

        out["policyDefinition"] = (
            capo_bedrock.types.automated_reasoning_policy_definition.serialize_json(
                value["policy_definition"]
            )
        )
    if "workflow_content" in value:
        import capo_bedrock.types.automated_reasoning_policy_workflow_type_content

        out["workflowContent"] = (
            capo_bedrock.types.automated_reasoning_policy_workflow_type_content.serialize_json(
                value["workflow_content"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildWorkflowSource:
    out: AutomatedReasoningPolicyBuildWorkflowSource = {}  # type: ignore[typeddict-item]
    if data.get("policyDefinition") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition

        out["policy_definition"] = (
            capo_bedrock.types.automated_reasoning_policy_definition.deserialize_json(
                data["policyDefinition"]
            )
        )
    if data.get("workflowContent") is not None:
        import capo_bedrock.types.automated_reasoning_policy_workflow_type_content

        out["workflow_content"] = (
            capo_bedrock.types.automated_reasoning_policy_workflow_type_content.deserialize_json(
                data["workflowContent"]
            )
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyBuildWorkflowSource,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policy_definition" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition

        out["policy_definition"] = (
            capo_bedrock.types.automated_reasoning_policy_definition.redact_sensitive(
                value["policy_definition"]
            )
        )
    if "workflow_content" in value:
        import capo_bedrock.types.automated_reasoning_policy_workflow_type_content

        out["workflow_content"] = (
            capo_bedrock.types.automated_reasoning_policy_workflow_type_content.redact_sensitive(
                value["workflow_content"]
            )
        )
    return out
