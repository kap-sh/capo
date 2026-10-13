"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildWorkflowDocumentList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_document

AutomatedReasoningPolicyBuildWorkflowDocumentList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_build_workflow_document.AutomatedReasoningPolicyBuildWorkflowDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildWorkflowDocumentList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_document

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_build_workflow_document.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyBuildWorkflowDocumentList:
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_document

    out: AutomatedReasoningPolicyBuildWorkflowDocumentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_build_workflow_document.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyBuildWorkflowDocumentList,
) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_document

    return [
        capo_bedrock.types.automated_reasoning_policy_build_workflow_document.redact_sensitive(
            item
        )
        for item in value
    ]
