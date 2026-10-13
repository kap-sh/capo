"""Generated from Smithy shape ``com.amazonaws.sso#LogoutRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso.types.access_token_type


class LogoutRequest(TypedDict, closed=True):
    access_token: "capo_sso.types.access_token_type.AccessTokenType"
    """<p>The token issued by the <code>CreateToken</code> API call. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html">CreateToken</a> in the <i>IAM Identity Center OIDC API Reference Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogoutRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> LogoutRequest:
    out: LogoutRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: LogoutRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out
