"""Generated from Smithy shape ``com.amazonaws.workdocs#DeleteFolderRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.resource_id_type


class DeleteFolderRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    folder_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFolderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFolderRequest:
    out: DeleteFolderRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: DeleteFolderRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
