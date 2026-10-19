"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ExchangeCodeForTokenRequestBody``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.sensitive_string


class ExchangeCodeForTokenRequestBody(TypedDict, closed=True):
    code: "capo_amplifyuibuilder.types.sensitive_string.SensitiveString"
    """<p>The access code to send in the request.</p>"""
    redirect_uri: "str"
    """<p>The location of the application that will receive the access code.</p>"""
    client_id: NotRequired[
        "capo_amplifyuibuilder.types.sensitive_string.SensitiveString"
    ]
    """<p>The ID of the client to request the token from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExchangeCodeForTokenRequestBody) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["redirectUri"] = value["redirect_uri"]
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    return out


def deserialize_json(data: dict) -> ExchangeCodeForTokenRequestBody:
    out: ExchangeCodeForTokenRequestBody = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("redirectUri") is not None:
        out["redirect_uri"] = data["redirectUri"]
    else:
        out["redirect_uri"] = ""
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    return out


def redact_sensitive(value: ExchangeCodeForTokenRequestBody) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "code" in value:
        out["code"] = "*** Sensitive Data Redacted ***"
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    return out
