"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateCustomMetadataRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.custom_metadata_map
    import capo_workdocs.types.document_version_id_type
    import capo_workdocs.types.resource_id_type


class CreateCustomMetadataRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    resource_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the resource.</p>"""
    version_id: NotRequired[
        "capo_workdocs.types.document_version_id_type.DocumentVersionIdType"
    ]
    """<p>The ID of the version, if the custom metadata is being added to a document version.</p>"""
    custom_metadata: "capo_workdocs.types.custom_metadata_map.CustomMetadataMap"
    """<p>Custom metadata in the form of name-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomMetadataRequest) -> dict:
    out: dict = {}
    import capo_workdocs.types.custom_metadata_map

    out["CustomMetadata"] = capo_workdocs.types.custom_metadata_map.serialize_json(
        value["custom_metadata"]
    )
    return out


def deserialize_json(data: dict) -> CreateCustomMetadataRequest:
    out: CreateCustomMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("CustomMetadata") is not None:
        import capo_workdocs.types.custom_metadata_map

        out["custom_metadata"] = (
            capo_workdocs.types.custom_metadata_map.deserialize_json(
                data["CustomMetadata"]
            )
        )
    else:
        out["custom_metadata"] = {}
    return out


def redact_sensitive(value: CreateCustomMetadataRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
