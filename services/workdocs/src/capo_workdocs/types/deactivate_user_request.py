"""Generated from Smithy shape ``com.amazonaws.workdocs#DeactivateUserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.id_type


class DeactivateUserRequest(TypedDict, closed=True):
    user_id: "capo_workdocs.types.id_type.IdType"
    """<p>The ID of the user.</p>"""
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeactivateUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeactivateUserRequest:
    out: DeactivateUserRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: DeactivateUserRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
