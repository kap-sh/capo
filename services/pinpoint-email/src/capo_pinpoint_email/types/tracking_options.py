"""Generated from Smithy shape ``com.amazonaws.pinpointemail#TrackingOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.custom_redirect_domain


class TrackingOptions(TypedDict, closed=True):
    custom_redirect_domain: (
        "capo_pinpoint_email.types.custom_redirect_domain.CustomRedirectDomain"
    )
    """<p>The domain that you want to use for tracking open and click events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrackingOptions) -> dict:
    out: dict = {}
    out["CustomRedirectDomain"] = value["custom_redirect_domain"]
    return out


def deserialize_json(data: dict) -> TrackingOptions:
    out: TrackingOptions = {}  # type: ignore[typeddict-item]
    if data.get("CustomRedirectDomain") is not None:
        out["custom_redirect_domain"] = data["CustomRedirectDomain"]
    else:
        out["custom_redirect_domain"] = ""
    return out
