"""Generated from Smithy shape ``com.amazonaws.workdocs#AbortDocumentVersionUploadRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.document_version_id_type
    import capo_workdocs.types.resource_id_type


class AbortDocumentVersionUploadRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    document_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the document.</p>"""
    version_id: "capo_workdocs.types.document_version_id_type.DocumentVersionIdType"
    """<p>The ID of the version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AbortDocumentVersionUploadRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AbortDocumentVersionUploadRequest:
    out: AbortDocumentVersionUploadRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: AbortDocumentVersionUploadRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
