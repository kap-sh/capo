"""Generated from Smithy shape ``com.amazonaws.workdocs#GetCurrentUserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type


class GetCurrentUserRequest(TypedDict, closed=True):
    authentication_token: (
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    )
    """<p>Amazon WorkDocs authentication token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCurrentUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCurrentUserRequest:
    out: GetCurrentUserRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: GetCurrentUserRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
