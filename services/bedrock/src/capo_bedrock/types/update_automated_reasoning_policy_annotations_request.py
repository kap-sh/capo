"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateAutomatedReasoningPolicyAnnotationsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_annotation_list
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_id
    import capo_bedrock.types.automated_reasoning_policy_hash


class UpdateAutomatedReasoningPolicyAnnotationsRequest(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose annotations you want to update.</p>"""
    build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId"
    """<p>The unique identifier of the build workflow whose annotations you want to update.</p>"""
    annotations: "capo_bedrock.types.automated_reasoning_policy_annotation_list.AutomatedReasoningPolicyAnnotationList"
    """<p>The updated annotations containing modified rules, variables, and types for the policy.</p>"""
    last_updated_annotation_set_hash: "capo_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash"
    """<p>The hash value of the annotation set that you're updating. This is used for optimistic concurrency control to prevent conflicting updates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAutomatedReasoningPolicyAnnotationsRequest) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_annotation_list

    out["annotations"] = (
        capo_bedrock.types.automated_reasoning_policy_annotation_list.serialize_json(
            value["annotations"]
        )
    )
    out["lastUpdatedAnnotationSetHash"] = value["last_updated_annotation_set_hash"]
    return out


def deserialize_json(data: dict) -> UpdateAutomatedReasoningPolicyAnnotationsRequest:
    out: UpdateAutomatedReasoningPolicyAnnotationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("annotations") is not None:
        import capo_bedrock.types.automated_reasoning_policy_annotation_list

        out["annotations"] = (
            capo_bedrock.types.automated_reasoning_policy_annotation_list.deserialize_json(
                data["annotations"]
            )
        )
    else:
        out["annotations"] = []
    if data.get("lastUpdatedAnnotationSetHash") is not None:
        out["last_updated_annotation_set_hash"] = data["lastUpdatedAnnotationSetHash"]
    else:
        out["last_updated_annotation_set_hash"] = ""
    return out


def redact_sensitive(
    value: UpdateAutomatedReasoningPolicyAnnotationsRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "annotations" in value:
        import capo_bedrock.types.automated_reasoning_policy_annotation_list

        out["annotations"] = (
            capo_bedrock.types.automated_reasoning_policy_annotation_list.redact_sensitive(
                value["annotations"]
            )
        )
    return out
