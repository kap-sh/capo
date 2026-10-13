"""Generated from Smithy shape ``com.amazonaws.workdocs#UpdateDocumentVersionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.document_version_id_type
    import capo_workdocs.types.document_version_status
    import capo_workdocs.types.resource_id_type


class UpdateDocumentVersionRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    document_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the document.</p>"""
    version_id: "capo_workdocs.types.document_version_id_type.DocumentVersionIdType"
    """<p>The version ID of the document.</p>"""
    version_status: NotRequired[
        "capo_workdocs.types.document_version_status.DocumentVersionStatus"
    ]
    """<p>The status of the version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDocumentVersionRequest) -> dict:
    out: dict = {}
    if "version_status" in value:
        import capo_workdocs.types.document_version_status

        out["VersionStatus"] = (
            capo_workdocs.types.document_version_status.serialize_json(
                value["version_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDocumentVersionRequest:
    out: UpdateDocumentVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("VersionStatus") is not None:
        import capo_workdocs.types.document_version_status

        out["version_status"] = (
            capo_workdocs.types.document_version_status.deserialize_json(
                data["VersionStatus"]
            )
        )
    return out


def redact_sensitive(value: UpdateDocumentVersionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
