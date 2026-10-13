"""Generated from Smithy shape ``com.amazonaws.glue#AuthorizationCodeProperties``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.authorization_code
    import capo_glue.types.redirect_uri


class AuthorizationCodeProperties(TypedDict, closed=True):
    authorization_code: NotRequired[
        "capo_glue.types.authorization_code.AuthorizationCode"
    ]
    """<p>An authorization code to be used in the third leg of the <code>AUTHORIZATION_CODE</code> grant workflow. This is a single-use code which becomes invalid once exchanged for an access token, thus it is acceptable to have this value as a request parameter.</p>"""
    redirect_uri: NotRequired["capo_glue.types.redirect_uri.RedirectUri"]
    """<p>The redirect URI where the user gets redirected to by authorization server when issuing an authorization code. The URI is subsequently used when the authorization code is exchanged for an access token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthorizationCodeProperties) -> dict:
    out: dict = {}
    if "authorization_code" in value:
        out["AuthorizationCode"] = value["authorization_code"]
    if "redirect_uri" in value:
        out["RedirectUri"] = value["redirect_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthorizationCodeProperties:
    out: AuthorizationCodeProperties = {}  # type: ignore[typeddict-item]
    if data.get("AuthorizationCode") is not None:
        out["authorization_code"] = data["AuthorizationCode"]
    if data.get("RedirectUri") is not None:
        out["redirect_uri"] = data["RedirectUri"]
    return out


def redact_sensitive(value: AuthorizationCodeProperties) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authorization_code" in value:
        out["authorization_code"] = "*** Sensitive Data Redacted ***"
    return out
