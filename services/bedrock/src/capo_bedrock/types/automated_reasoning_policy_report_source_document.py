"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyReportSourceDocument``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_annotated_chunk_list
    import capo_bedrock.types.automated_reasoning_policy_atomic_statement_list
    import capo_bedrock.types.automated_reasoning_policy_build_document_name
    import capo_bedrock.types.automated_reasoning_policy_document_id
    import capo_bedrock.types.automated_reasoning_policy_document_sha256


class AutomatedReasoningPolicyReportSourceDocument(TypedDict, closed=True):
    document_name: "capo_bedrock.types.automated_reasoning_policy_build_document_name.AutomatedReasoningPolicyBuildDocumentName"
    """<p>The name of the source document that was analyzed.</p>"""
    document_hash: "capo_bedrock.types.automated_reasoning_policy_document_sha256.AutomatedReasoningPolicyDocumentSha256"
    """<p>A SHA-256 hash of the document content, used for verification and ensuring the document hasn't changed since analysis.</p>"""
    document_id: "capo_bedrock.types.automated_reasoning_policy_document_id.AutomatedReasoningPolicyDocumentId"
    """<p>A unique identifier for this document within the fidelity report.</p>"""
    atomic_statements: "capo_bedrock.types.automated_reasoning_policy_atomic_statement_list.AutomatedReasoningPolicyAtomicStatementList"
    """<p>The list of atomic statements extracted from this document, representing the fundamental units of meaning used for grounding.</p>"""
    document_content: "capo_bedrock.types.automated_reasoning_policy_annotated_chunk_list.AutomatedReasoningPolicyAnnotatedChunkList"
    """<p>The document's content organized into annotated chunks with line number information for precise referencing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyReportSourceDocument) -> dict:
    out: dict = {}
    out["documentName"] = value["document_name"]
    out["documentHash"] = value["document_hash"]
    out["documentId"] = value["document_id"]
    import capo_bedrock.types.automated_reasoning_policy_atomic_statement_list

    out["atomicStatements"] = (
        capo_bedrock.types.automated_reasoning_policy_atomic_statement_list.serialize_json(
            value["atomic_statements"]
        )
    )
    import capo_bedrock.types.automated_reasoning_policy_annotated_chunk_list

    out["documentContent"] = (
        capo_bedrock.types.automated_reasoning_policy_annotated_chunk_list.serialize_json(
            value["document_content"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyReportSourceDocument:
    out: AutomatedReasoningPolicyReportSourceDocument = {}  # type: ignore[typeddict-item]
    if data.get("documentName") is not None:
        out["document_name"] = data["documentName"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyReportSourceDocument.document_name required"
        )
    if data.get("documentHash") is not None:
        out["document_hash"] = data["documentHash"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyReportSourceDocument.document_hash required"
        )
    if data.get("documentId") is not None:
        out["document_id"] = data["documentId"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyReportSourceDocument.document_id required"
        )
    if data.get("atomicStatements") is not None:
        import capo_bedrock.types.automated_reasoning_policy_atomic_statement_list

        out["atomic_statements"] = (
            capo_bedrock.types.automated_reasoning_policy_atomic_statement_list.deserialize_json(
                data["atomicStatements"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyReportSourceDocument.atomic_statements required"
        )
    if data.get("documentContent") is not None:
        import capo_bedrock.types.automated_reasoning_policy_annotated_chunk_list

        out["document_content"] = (
            capo_bedrock.types.automated_reasoning_policy_annotated_chunk_list.deserialize_json(
                data["documentContent"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyReportSourceDocument.document_content required"
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyReportSourceDocument,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "document_name" in value:
        out["document_name"] = "*** Sensitive Data Redacted ***"
    if "atomic_statements" in value:
        import capo_bedrock.types.automated_reasoning_policy_atomic_statement_list

        out["atomic_statements"] = (
            capo_bedrock.types.automated_reasoning_policy_atomic_statement_list.redact_sensitive(
                value["atomic_statements"]
            )
        )
    if "document_content" in value:
        import capo_bedrock.types.automated_reasoning_policy_annotated_chunk_list

        out["document_content"] = (
            capo_bedrock.types.automated_reasoning_policy_annotated_chunk_list.redact_sensitive(
                value["document_content"]
            )
        )
    return out
