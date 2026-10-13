"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#RefreshTokenRequestBody``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.sensitive_string


class RefreshTokenRequestBody(TypedDict, closed=True):
    token: "capo_amplifyuibuilder.types.sensitive_string.SensitiveString"
    """<p>The token to use to refresh a previously issued access token that might have expired.</p>"""
    client_id: NotRequired[
        "capo_amplifyuibuilder.types.sensitive_string.SensitiveString"
    ]
    """<p>The ID of the client to request the token from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RefreshTokenRequestBody) -> dict:
    out: dict = {}
    out["token"] = value["token"]
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    return out


def deserialize_json(data: dict) -> RefreshTokenRequestBody:
    out: RefreshTokenRequestBody = {}  # type: ignore[typeddict-item]
    if data.get("token") is not None:
        out["token"] = data["token"]
    else:
        raise DeserializationError("RefreshTokenRequestBody.token required")
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    return out


def redact_sensitive(value: RefreshTokenRequestBody) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "token" in value:
        out["token"] = "*** Sensitive Data Redacted ***"
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    return out
