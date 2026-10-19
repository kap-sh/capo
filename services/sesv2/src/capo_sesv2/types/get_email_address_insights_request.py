"""Generated from Smithy shape ``com.amazonaws.sesv2#GetEmailAddressInsightsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_address


class GetEmailAddressInsightsRequest(TypedDict, closed=True):
    email_address: "capo_sesv2.types.email_address.EmailAddress"
    """<p>The email address to analyze for validation insights.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEmailAddressInsightsRequest) -> dict:
    out: dict = {}
    out["EmailAddress"] = value["email_address"]
    return out


def deserialize_json(data: dict) -> GetEmailAddressInsightsRequest:
    out: GetEmailAddressInsightsRequest = {}  # type: ignore[typeddict-item]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    else:
        out["email_address"] = ""
    return out
