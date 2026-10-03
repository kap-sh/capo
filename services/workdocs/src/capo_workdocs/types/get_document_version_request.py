"""Generated from Smithy shape ``com.amazonaws.workdocs#GetDocumentVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.boolean_type
    import capo_workdocs.types.document_version_id_type
    import capo_workdocs.types.field_names_type
    import capo_workdocs.types.resource_id_type


class GetDocumentVersionRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    document_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the document.</p>"""
    version_id: "capo_workdocs.types.document_version_id_type.DocumentVersionIdType"
    """<p>The version ID of the document.</p>"""
    fields: NotRequired["capo_workdocs.types.field_names_type.FieldNamesType"]
    """<p>A comma-separated list of values. Specify "SOURCE" to include a URL for the source document.</p>"""
    include_custom_metadata: "capo_workdocs.types.boolean_type.BooleanType"
    """<p>Set this to TRUE to include custom metadata in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDocumentVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDocumentVersionRequest:
    out: GetDocumentVersionRequest = {}  # type: ignore[typeddict-item]
    return out
