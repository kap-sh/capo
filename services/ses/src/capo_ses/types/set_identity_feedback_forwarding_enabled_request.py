"""Generated from Smithy shape ``com.amazonaws.ses#SetIdentityFeedbackForwardingEnabledRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.enabled
    import capo_ses.types.identity


class SetIdentityFeedbackForwardingEnabledRequest(TypedDict, closed=True):
    identity: "capo_ses.types.identity.Identity"
    """<p>The identity for which to set bounce and complaint notification forwarding. Examples: <code>user@example.com</code>, <code>example.com</code>.</p>"""
    forwarding_enabled: "capo_ses.types.enabled.Enabled"
    """<p>Sets whether Amazon SES forwards bounce and complaint notifications as email. <code>true</code> specifies that Amazon SES forwards bounce and complaint notifications as email, in addition to any Amazon SNS topic publishing otherwise specified. <code>false</code> specifies that Amazon SES publishes bounce and complaint notifications only through Amazon SNS. This value can only be set to <code>false</code> when Amazon SNS topics are set for both <code>Bounce</code> and <code>Complaint</code> notification types.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetIdentityFeedbackForwardingEnabledRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Identity", str(value["identity"])))
    pairs.append(
        (
            f"{key_prefix}ForwardingEnabled",
            "true" if value["forwarding_enabled"] else "false",
        )
    )


def deserialize_query(el: Element) -> SetIdentityFeedbackForwardingEnabledRequest:
    out: SetIdentityFeedbackForwardingEnabledRequest = {}  # type: ignore[typeddict-item]
    child_identity = el.find("Identity")
    if child_identity is not None:
        out["identity"] = str(child_identity.text or "")
    else:
        out["identity"] = ""
    child_forwarding_enabled = el.find("ForwardingEnabled")
    if child_forwarding_enabled is not None:
        out["forwarding_enabled"] = (
            child_forwarding_enabled.text or ""
        ).lower() == "true"
    else:
        out["forwarding_enabled"] = False
    return out
