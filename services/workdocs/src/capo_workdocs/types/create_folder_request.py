"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateFolderRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workdocs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.resource_id_type
    import capo_workdocs.types.resource_name_type


class CreateFolderRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    name: NotRequired["capo_workdocs.types.resource_name_type.ResourceNameType"]
    """<p>The name of the new folder.</p>"""
    parent_folder_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the parent folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFolderRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    out["ParentFolderId"] = value["parent_folder_id"]
    return out


def deserialize_json(data: dict) -> CreateFolderRequest:
    out: CreateFolderRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ParentFolderId") is not None:
        out["parent_folder_id"] = data["ParentFolderId"]
    else:
        raise DeserializationError("CreateFolderRequest.parent_folder_id required")
    return out


def redact_sensitive(value: CreateFolderRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
