"""Generated from Smithy shape ``com.amazonaws.workdocs#GetDocumentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.boolean_type
    import capo_workdocs.types.resource_id_type


class GetDocumentRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    document_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the document.</p>"""
    include_custom_metadata: "capo_workdocs.types.boolean_type.BooleanType"
    """<p>Set this to <code>TRUE</code> to include custom metadata in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDocumentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDocumentRequest:
    out: GetDocumentRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: GetDocumentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
