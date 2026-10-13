"""Generated from Smithy shape ``com.amazonaws.workdocs#RemoveResourcePermissionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.id_type
    import capo_workdocs.types.principal_type
    import capo_workdocs.types.resource_id_type


class RemoveResourcePermissionRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    resource_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the resource.</p>"""
    principal_id: "capo_workdocs.types.id_type.IdType"
    """<p>The principal ID of the resource.</p>"""
    principal_type: NotRequired["capo_workdocs.types.principal_type.PrincipalType"]
    """<p>The principal type of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveResourcePermissionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveResourcePermissionRequest:
    out: RemoveResourcePermissionRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: RemoveResourcePermissionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
