"""Generated from Smithy shape ``com.amazonaws.sesv2#PutEmailIdentityFeedbackAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.enabled
    import capo_sesv2.types.identity


class PutEmailIdentityFeedbackAttributesRequest(TypedDict, closed=True):
    email_identity: "capo_sesv2.types.identity.Identity"
    """<p>The email identity.</p>"""
    email_forwarding_enabled: NotRequired["capo_sesv2.types.enabled.Enabled"]
    """<p>Sets the feedback forwarding configuration for the identity.</p> <p>If the value is <code>true</code>, you receive email notifications when bounce or complaint events occur. These notifications are sent to the address that you specified in the <code>Return-Path</code> header of the original email.</p> <p>You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications (for example, by setting up an event destination), you receive an email notification when these events occur (even if this setting is disabled).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutEmailIdentityFeedbackAttributesRequest) -> dict:
    out: dict = {}
    if "email_forwarding_enabled" in value:
        out["EmailForwardingEnabled"] = value["email_forwarding_enabled"]
    return out


def deserialize_json(data: dict) -> PutEmailIdentityFeedbackAttributesRequest:
    out: PutEmailIdentityFeedbackAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("EmailForwardingEnabled") is not None:
        out["email_forwarding_enabled"] = data["EmailForwardingEnabled"]
    return out
