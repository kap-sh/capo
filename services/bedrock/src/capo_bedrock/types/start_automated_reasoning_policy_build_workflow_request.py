"""Generated from Smithy shape ``com.amazonaws.bedrock#StartAutomatedReasoningPolicyBuildWorkflowRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_source
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_type
    import capo_bedrock.types.idempotency_token


class StartAutomatedReasoningPolicyBuildWorkflowRequest(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to start the build workflow.</p>"""
    build_workflow_type: "capo_bedrock.types.automated_reasoning_policy_build_workflow_type.AutomatedReasoningPolicyBuildWorkflowType"
    """<p>The type of build workflow to start (e.g., DOCUMENT_INGESTION for processing new documents, POLICY_REPAIR for fixing existing policies).</p>"""
    client_request_token: NotRequired[
        "capo_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.</p>"""
    source_content: "capo_bedrock.types.automated_reasoning_policy_build_workflow_source.AutomatedReasoningPolicyBuildWorkflowSource"
    """<p>The source content for the build workflow, such as documents to analyze or repair instructions for existing policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAutomatedReasoningPolicyBuildWorkflowRequest) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_source

    out["sourceContent"] = (
        capo_bedrock.types.automated_reasoning_policy_build_workflow_source.serialize_json(
            value["source_content"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartAutomatedReasoningPolicyBuildWorkflowRequest:
    out: StartAutomatedReasoningPolicyBuildWorkflowRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceContent") is not None:
        import capo_bedrock.types.automated_reasoning_policy_build_workflow_source

        out["source_content"] = (
            capo_bedrock.types.automated_reasoning_policy_build_workflow_source.deserialize_json(
                data["sourceContent"]
            )
        )
    else:
        raise DeserializationError(
            "StartAutomatedReasoningPolicyBuildWorkflowRequest.source_content required"
        )
    return out


def redact_sensitive(
    value: StartAutomatedReasoningPolicyBuildWorkflowRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_content" in value:
        import capo_bedrock.types.automated_reasoning_policy_build_workflow_source

        out["source_content"] = (
            capo_bedrock.types.automated_reasoning_policy_build_workflow_source.redact_sensitive(
                value["source_content"]
            )
        )
    return out
