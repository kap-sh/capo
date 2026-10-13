"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildWorkflowRepairContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_annotation_list


class AutomatedReasoningPolicyBuildWorkflowRepairContent(TypedDict, closed=True):
    annotations: "capo_bedrock.types.automated_reasoning_policy_annotation_list.AutomatedReasoningPolicyAnnotationList"
    """<p>Specific annotations or modifications to apply during the policy repair process, such as rule corrections or variable updates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildWorkflowRepairContent) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_annotation_list

    out["annotations"] = (
        capo_bedrock.types.automated_reasoning_policy_annotation_list.serialize_json(
            value["annotations"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildWorkflowRepairContent:
    out: AutomatedReasoningPolicyBuildWorkflowRepairContent = {}  # type: ignore[typeddict-item]
    if data.get("annotations") is not None:
        import capo_bedrock.types.automated_reasoning_policy_annotation_list

        out["annotations"] = (
            capo_bedrock.types.automated_reasoning_policy_annotation_list.deserialize_json(
                data["annotations"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildWorkflowRepairContent.annotations required"
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyBuildWorkflowRepairContent,
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
