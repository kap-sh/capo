"""Generated from Smithy shape ``com.amazonaws.workdocs#DeleteCustomMetadataRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.boolean_type
    import capo_workdocs.types.custom_metadata_key_list
    import capo_workdocs.types.document_version_id_type
    import capo_workdocs.types.resource_id_type


class DeleteCustomMetadataRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    resource_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the resource, either a document or folder.</p>"""
    version_id: NotRequired[
        "capo_workdocs.types.document_version_id_type.DocumentVersionIdType"
    ]
    """<p>The ID of the version, if the custom metadata is being deleted from a document version.</p>"""
    keys: NotRequired[
        "capo_workdocs.types.custom_metadata_key_list.CustomMetadataKeyList"
    ]
    """<p>List of properties to remove.</p>"""
    delete_all: "capo_workdocs.types.boolean_type.BooleanType"
    """<p>Flag to indicate removal of all custom metadata properties from the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomMetadataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCustomMetadataRequest:
    out: DeleteCustomMetadataRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: DeleteCustomMetadataRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
