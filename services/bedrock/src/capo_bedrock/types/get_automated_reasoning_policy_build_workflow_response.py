"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyBuildWorkflowResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_build_document_content_type
    import capo_bedrock.types.automated_reasoning_policy_build_document_description
    import capo_bedrock.types.automated_reasoning_policy_build_document_name
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_id
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_status
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_type
    import capo_bedrock.types.timestamp


class GetAutomatedReasoningPolicyBuildWorkflowResponse(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy.</p>"""
    build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId"
    """<p>The unique identifier of the build workflow.</p>"""
    status: "capo_bedrock.types.automated_reasoning_policy_build_workflow_status.AutomatedReasoningPolicyBuildWorkflowStatus"
    """<p>The current status of the build workflow (e.g., RUNNING, COMPLETED, FAILED, CANCELLED).</p>"""
    build_workflow_type: "capo_bedrock.types.automated_reasoning_policy_build_workflow_type.AutomatedReasoningPolicyBuildWorkflowType"
    """<p>The type of build workflow being executed (e.g., DOCUMENT_INGESTION, POLICY_REPAIR).</p>"""
    document_name: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_build_document_name.AutomatedReasoningPolicyBuildDocumentName"
    ]
    """<p>The name of the source document used in the build workflow.</p>"""
    document_content_type: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_build_document_content_type.AutomatedReasoningPolicyBuildDocumentContentType"
    ]
    """<p>The content type of the source document (e.g., text/plain, application/pdf).</p>"""
    document_description: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_build_document_description.AutomatedReasoningPolicyBuildDocumentDescription"
    ]
    """<p>A detailed description of the document's content and how it should be used in the policy generation process.</p>"""
    created_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the build workflow was created.</p>"""
    updated_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the build workflow was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedReasoningPolicyBuildWorkflowResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["buildWorkflowId"] = value["build_workflow_id"]
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_status

    out["status"] = (
        capo_bedrock.types.automated_reasoning_policy_build_workflow_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_type

    out["buildWorkflowType"] = (
        capo_bedrock.types.automated_reasoning_policy_build_workflow_type.serialize_json(
            value["build_workflow_type"]
        )
    )
    if "document_name" in value:
        out["documentName"] = value["document_name"]
    if "document_content_type" in value:
        import capo_bedrock.types.automated_reasoning_policy_build_document_content_type

        out["documentContentType"] = (
            capo_bedrock.types.automated_reasoning_policy_build_document_content_type.serialize_json(
                value["document_content_type"]
            )
        )
    if "document_description" in value:
        out["documentDescription"] = value["document_description"]
    import capo_bedrock.types.timestamp

    out["createdAt"] = capo_bedrock.types.timestamp.serialize_json(value["created_at"])
    import capo_bedrock.types.timestamp

    out["updatedAt"] = capo_bedrock.types.timestamp.serialize_json(value["updated_at"])
    return out


def deserialize_json(data: dict) -> GetAutomatedReasoningPolicyBuildWorkflowResponse:
    out: GetAutomatedReasoningPolicyBuildWorkflowResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        out["policy_arn"] = ""
    if data.get("buildWorkflowId") is not None:
        out["build_workflow_id"] = data["buildWorkflowId"]
    else:
        out["build_workflow_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock.types.automated_reasoning_policy_build_workflow_status

        out["status"] = (
            capo_bedrock.types.automated_reasoning_policy_build_workflow_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock.types.automated_reasoning_policy_build_workflow_status.AutomatedReasoningPolicyBuildWorkflowStatus",
            "",
        )
    if data.get("buildWorkflowType") is not None:
        import capo_bedrock.types.automated_reasoning_policy_build_workflow_type

        out["build_workflow_type"] = (
            capo_bedrock.types.automated_reasoning_policy_build_workflow_type.deserialize_json(
                data["buildWorkflowType"]
            )
        )
    else:
        import typing

        out["build_workflow_type"] = typing.cast(
            "capo_bedrock.types.automated_reasoning_policy_build_workflow_type.AutomatedReasoningPolicyBuildWorkflowType",
            "",
        )
    if data.get("documentName") is not None:
        out["document_name"] = data["documentName"]
    if data.get("documentContentType") is not None:
        import capo_bedrock.types.automated_reasoning_policy_build_document_content_type

        out["document_content_type"] = (
            capo_bedrock.types.automated_reasoning_policy_build_document_content_type.deserialize_json(
                data["documentContentType"]
            )
        )
    if data.get("documentDescription") is not None:
        out["document_description"] = data["documentDescription"]
    if data.get("createdAt") is not None:
        import capo_bedrock.types.timestamp

        out["created_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock.types.timestamp

        out["updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out


def redact_sensitive(
    value: GetAutomatedReasoningPolicyBuildWorkflowResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "document_name" in value:
        out["document_name"] = "*** Sensitive Data Redacted ***"
    if "document_description" in value:
        out["document_description"] = "*** Sensitive Data Redacted ***"
    return out
