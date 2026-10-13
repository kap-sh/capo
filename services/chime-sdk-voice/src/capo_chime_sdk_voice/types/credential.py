"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#Credential``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sensitive_string


class Credential(TypedDict, closed=True):
    username: NotRequired["capo_chime_sdk_voice.types.sensitive_string.SensitiveString"]
    """<p>The RFC2617 compliant user name associated with the SIP credentials, in US-ASCII format.</p>"""
    password: NotRequired["capo_chime_sdk_voice.types.sensitive_string.SensitiveString"]
    """<p>The RFC2617 compliant password associated with the SIP credentials, in US-ASCII format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Credential) -> dict:
    out: dict = {}
    if "username" in value:
        out["Username"] = value["username"]
    if "password" in value:
        out["Password"] = value["password"]
    return out


def deserialize_json(data: dict) -> Credential:
    out: Credential = {}  # type: ignore[typeddict-item]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    return out


def redact_sensitive(value: Credential) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
