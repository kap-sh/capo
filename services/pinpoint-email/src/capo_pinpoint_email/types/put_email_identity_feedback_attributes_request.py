"""Generated from Smithy shape ``com.amazonaws.pinpointemail#PutEmailIdentityFeedbackAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.enabled
    import capo_pinpoint_email.types.identity


class PutEmailIdentityFeedbackAttributesRequest(TypedDict, closed=True):
    email_identity: "capo_pinpoint_email.types.identity.Identity"
    """<p>The email identity that you want to configure bounce and complaint feedback forwarding for.</p>"""
    email_forwarding_enabled: NotRequired["capo_pinpoint_email.types.enabled.Enabled"]
    """<p>Sets the feedback forwarding configuration for the identity.</p> <p>If the value is <code>true</code>, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.</p> <p>When you set this value to <code>false</code>, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic or another event destination. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).</p>"""


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
