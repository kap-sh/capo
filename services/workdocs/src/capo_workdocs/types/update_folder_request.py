"""Generated from Smithy shape ``com.amazonaws.workdocs#UpdateFolderRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.resource_id_type
    import capo_workdocs.types.resource_name_type
    import capo_workdocs.types.resource_state_type


class UpdateFolderRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    folder_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the folder.</p>"""
    name: NotRequired["capo_workdocs.types.resource_name_type.ResourceNameType"]
    """<p>The name of the folder.</p>"""
    parent_folder_id: NotRequired["capo_workdocs.types.resource_id_type.ResourceIdType"]
    """<p>The ID of the parent folder.</p>"""
    resource_state: NotRequired[
        "capo_workdocs.types.resource_state_type.ResourceStateType"
    ]
    """<p>The resource state of the folder. Only ACTIVE and RECYCLED are accepted values from the API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFolderRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "parent_folder_id" in value:
        out["ParentFolderId"] = value["parent_folder_id"]
    if "resource_state" in value:
        import capo_workdocs.types.resource_state_type

        out["ResourceState"] = capo_workdocs.types.resource_state_type.serialize_json(
            value["resource_state"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFolderRequest:
    out: UpdateFolderRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ParentFolderId") is not None:
        out["parent_folder_id"] = data["ParentFolderId"]
    if data.get("ResourceState") is not None:
        import capo_workdocs.types.resource_state_type

        out["resource_state"] = (
            capo_workdocs.types.resource_state_type.deserialize_json(
                data["ResourceState"]
            )
        )
    return out


def redact_sensitive(value: UpdateFolderRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
