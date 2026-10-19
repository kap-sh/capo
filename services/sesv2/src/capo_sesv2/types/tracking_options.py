"""Generated from Smithy shape ``com.amazonaws.sesv2#TrackingOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.custom_redirect_domain
    import capo_sesv2.types.https_policy


class TrackingOptions(TypedDict, closed=True):
    custom_redirect_domain: (
        "capo_sesv2.types.custom_redirect_domain.CustomRedirectDomain"
    )
    """<p>The domain to use for tracking open and click events.</p>"""
    https_policy: NotRequired["capo_sesv2.types.https_policy.HttpsPolicy"]
    """<p>The https policy to use for tracking open and click events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrackingOptions) -> dict:
    out: dict = {}
    out["CustomRedirectDomain"] = value["custom_redirect_domain"]
    if "https_policy" in value:
        import capo_sesv2.types.https_policy

        out["HttpsPolicy"] = capo_sesv2.types.https_policy.serialize_json(
            value["https_policy"]
        )
    return out


def deserialize_json(data: dict) -> TrackingOptions:
    out: TrackingOptions = {}  # type: ignore[typeddict-item]
    if data.get("CustomRedirectDomain") is not None:
        out["custom_redirect_domain"] = data["CustomRedirectDomain"]
    else:
        out["custom_redirect_domain"] = ""
    if data.get("HttpsPolicy") is not None:
        import capo_sesv2.types.https_policy

        out["https_policy"] = capo_sesv2.types.https_policy.deserialize_json(
            data["HttpsPolicy"]
        )
    return out
