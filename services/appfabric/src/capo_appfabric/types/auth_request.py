"""Generated from Smithy shape ``com.amazonaws.appfabric#AuthRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.redirect_uri
    import capo_appfabric.types.sensitive_string2048


class AuthRequest(TypedDict, closed=True):
    redirect_uri: "capo_appfabric.types.redirect_uri.RedirectUri"
    """<p>The redirect URL that is specified in the AuthURL and the application client.</p>"""
    code: "capo_appfabric.types.sensitive_string2048.SensitiveString2048"
    """<p>The authorization code returned by the application after permission is granted in the application OAuth page (after clicking on the AuthURL).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthRequest) -> dict:
    out: dict = {}
    out["redirectUri"] = value["redirect_uri"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> AuthRequest:
    out: AuthRequest = {}  # type: ignore[typeddict-item]
    if data.get("redirectUri") is not None:
        out["redirect_uri"] = data["redirectUri"]
    else:
        out["redirect_uri"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    return out


def redact_sensitive(value: AuthRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "code" in value:
        out["code"] = "*** Sensitive Data Redacted ***"
    return out
