"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxRegistrationStatusReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.status_reason_code
    import capo_taxsettings.types.status_reason_message


class TaxRegistrationStatusReason(TypedDict, closed=True):
    code: NotRequired["capo_taxsettings.types.status_reason_code.StatusReasonCode"]
    """<p>A code that identifies the rejection reason (for example, <code>NIT_MISMATCH</code> or <code>ENCRYPTED_PDF</code>). If the reason isn't recognized, the value is <code>OTHER</code>. New codes might be added in the future.</p>"""
    message: NotRequired[
        "capo_taxsettings.types.status_reason_message.StatusReasonMessage"
    ]
    """<p>A description of the rejection reason in English.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaxRegistrationStatusReason) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TaxRegistrationStatusReason:
    out: TaxRegistrationStatusReason = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
