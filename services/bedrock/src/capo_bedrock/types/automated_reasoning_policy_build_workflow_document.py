"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildWorkflowDocument``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_build_document_blob
    import capo_bedrock.types.automated_reasoning_policy_build_document_content_type
    import capo_bedrock.types.automated_reasoning_policy_build_document_description
    import capo_bedrock.types.automated_reasoning_policy_build_document_name


class AutomatedReasoningPolicyBuildWorkflowDocument(TypedDict, closed=True):
    document: "capo_bedrock.types.automated_reasoning_policy_build_document_blob.AutomatedReasoningPolicyBuildDocumentBlob"
    """<p>The actual content of the source document that will be analyzed to extract policy rules and concepts.</p>"""
    document_content_type: "capo_bedrock.types.automated_reasoning_policy_build_document_content_type.AutomatedReasoningPolicyBuildDocumentContentType"
    """<p>The MIME type of the document content (e.g., text/plain, application/pdf, text/markdown).</p>"""
    document_name: "capo_bedrock.types.automated_reasoning_policy_build_document_name.AutomatedReasoningPolicyBuildDocumentName"
    """<p>A descriptive name for the document that helps identify its purpose and content.</p>"""
    document_description: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_build_document_description.AutomatedReasoningPolicyBuildDocumentDescription"
    ]
    """<p>A detailed description of the document's content and how it should be used in the policy generation process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildWorkflowDocument) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_build_document_blob

    out["document"] = (
        capo_bedrock.types.automated_reasoning_policy_build_document_blob.serialize_json(
            value["document"]
        )
    )
    import capo_bedrock.types.automated_reasoning_policy_build_document_content_type

    out["documentContentType"] = (
        capo_bedrock.types.automated_reasoning_policy_build_document_content_type.serialize_json(
            value["document_content_type"]
        )
    )
    out["documentName"] = value["document_name"]
    if "document_description" in value:
        out["documentDescription"] = value["document_description"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildWorkflowDocument:
    out: AutomatedReasoningPolicyBuildWorkflowDocument = {}  # type: ignore[typeddict-item]
    if data.get("document") is not None:
        import capo_bedrock.types.automated_reasoning_policy_build_document_blob

        out["document"] = (
            capo_bedrock.types.automated_reasoning_policy_build_document_blob.deserialize_json(
                data["document"]
            )
        )
    else:
        out["document"] = b""
    if data.get("documentContentType") is not None:
        import capo_bedrock.types.automated_reasoning_policy_build_document_content_type

        out["document_content_type"] = (
            capo_bedrock.types.automated_reasoning_policy_build_document_content_type.deserialize_json(
                data["documentContentType"]
            )
        )
    else:
        import typing

        out["document_content_type"] = typing.cast(
            "capo_bedrock.types.automated_reasoning_policy_build_document_content_type.AutomatedReasoningPolicyBuildDocumentContentType",
            "",
        )
    if data.get("documentName") is not None:
        out["document_name"] = data["documentName"]
    else:
        out["document_name"] = ""
    if data.get("documentDescription") is not None:
        out["document_description"] = data["documentDescription"]
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyBuildWorkflowDocument,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "document" in value:
        out["document"] = "*** Sensitive Data Redacted ***"
    if "document_name" in value:
        out["document_name"] = "*** Sensitive Data Redacted ***"
    if "document_description" in value:
        out["document_description"] = "*** Sensitive Data Redacted ***"
    return out
