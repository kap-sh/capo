"""Generated from Smithy shape ``com.amazonaws.sesv2#PutEmailIdentityDkimAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.enabled
    import capo_sesv2.types.identity


class PutEmailIdentityDkimAttributesRequest(TypedDict, closed=True):
    email_identity: "capo_sesv2.types.identity.Identity"
    """<p>The email identity.</p>"""
    signing_enabled: NotRequired["capo_sesv2.types.enabled.Enabled"]
    """<p>Sets the DKIM signing configuration for the identity.</p> <p>When you set this value <code>true</code>, then the messages that are sent from the identity are signed using DKIM. If you set this value to <code>false</code>, your messages are sent without DKIM signing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutEmailIdentityDkimAttributesRequest) -> dict:
    out: dict = {}
    if "signing_enabled" in value:
        out["SigningEnabled"] = value["signing_enabled"]
    return out


def deserialize_json(data: dict) -> PutEmailIdentityDkimAttributesRequest:
    out: PutEmailIdentityDkimAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("SigningEnabled") is not None:
        out["signing_enabled"] = data["SigningEnabled"]
    return out
