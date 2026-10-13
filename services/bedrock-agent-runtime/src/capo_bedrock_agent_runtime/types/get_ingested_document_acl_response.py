"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GetIngestedDocumentAclResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.document_acl


class GetIngestedDocumentAclResponse(TypedDict, closed=True):
    document_acl: "capo_bedrock_agent_runtime.types.document_acl.DocumentAcl"
    """<p>The ingested document access control list (ACL) containing allow and deny membership information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIngestedDocumentAclResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.document_acl

    out["documentAcl"] = capo_bedrock_agent_runtime.types.document_acl.serialize_json(
        value["document_acl"]
    )
    return out


def deserialize_json(data: dict) -> GetIngestedDocumentAclResponse:
    out: GetIngestedDocumentAclResponse = {}  # type: ignore[typeddict-item]
    if data.get("documentAcl") is not None:
        import capo_bedrock_agent_runtime.types.document_acl

        out["document_acl"] = (
            capo_bedrock_agent_runtime.types.document_acl.deserialize_json(
                data["documentAcl"]
            )
        )
    else:
        raise DeserializationError(
            "GetIngestedDocumentAclResponse.document_acl required"
        )
    return out


def redact_sensitive(value: GetIngestedDocumentAclResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "document_acl" in value:
        out["document_acl"] = "*** Sensitive Data Redacted ***"
    return out
