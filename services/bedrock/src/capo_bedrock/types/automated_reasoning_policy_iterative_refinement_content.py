"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyIterativeRefinementContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_build_feedback
    import capo_bedrock.types.automated_reasoning_policy_iterative_refinement_document_list


class AutomatedReasoningPolicyIterativeRefinementContent(TypedDict, closed=True):
    documents: "capo_bedrock.types.automated_reasoning_policy_iterative_refinement_document_list.AutomatedReasoningPolicyIterativeRefinementDocumentList"
    """<p>Source documents used for iterative policy refinement. These documents provide context for refining the policy definition.</p>"""
    feedback: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_build_feedback.AutomatedReasoningPolicyBuildFeedback"
    ]
    """<p>Optional feedback to guide the iterative refinement workflow. Provide specific instructions or constraints for policy refinement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyIterativeRefinementContent) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_iterative_refinement_document_list

    out["documents"] = (
        capo_bedrock.types.automated_reasoning_policy_iterative_refinement_document_list.serialize_json(
            value["documents"]
        )
    )
    if "feedback" in value:
        out["feedback"] = value["feedback"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyIterativeRefinementContent:
    out: AutomatedReasoningPolicyIterativeRefinementContent = {}  # type: ignore[typeddict-item]
    if data.get("documents") is not None:
        import capo_bedrock.types.automated_reasoning_policy_iterative_refinement_document_list

        out["documents"] = (
            capo_bedrock.types.automated_reasoning_policy_iterative_refinement_document_list.deserialize_json(
                data["documents"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyIterativeRefinementContent.documents required"
        )
    if data.get("feedback") is not None:
        out["feedback"] = data["feedback"]
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyIterativeRefinementContent,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "documents" in value:
        import capo_bedrock.types.automated_reasoning_policy_iterative_refinement_document_list

        out["documents"] = (
            capo_bedrock.types.automated_reasoning_policy_iterative_refinement_document_list.redact_sensitive(
                value["documents"]
            )
        )
    if "feedback" in value:
        out["feedback"] = "*** Sensitive Data Redacted ***"
    return out
