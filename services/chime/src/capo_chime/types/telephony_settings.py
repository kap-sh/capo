"""Generated from Smithy shape ``com.amazonaws.chime#TelephonySettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime.types.boolean


class TelephonySettings(TypedDict, closed=True):
    inbound_calling: "capo_chime.types.boolean.Boolean"
    """<p>Allows or denies inbound calling.</p>"""
    outbound_calling: "capo_chime.types.boolean.Boolean"
    """<p>Allows or denies outbound calling.</p>"""
    sms: "capo_chime.types.boolean.Boolean"
    """<p>Allows or denies SMS messaging.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelephonySettings) -> dict:
    out: dict = {}
    out["InboundCalling"] = value["inbound_calling"]
    out["OutboundCalling"] = value["outbound_calling"]
    out["SMS"] = value["sms"]
    return out


def deserialize_json(data: dict) -> TelephonySettings:
    out: TelephonySettings = {}  # type: ignore[typeddict-item]
    if data.get("InboundCalling") is not None:
        out["inbound_calling"] = data["InboundCalling"]
    else:
        out["inbound_calling"] = False
    if data.get("OutboundCalling") is not None:
        out["outbound_calling"] = data["OutboundCalling"]
    else:
        out["outbound_calling"] = False
    if data.get("SMS") is not None:
        out["sms"] = data["SMS"]
    else:
        out["sms"] = False
    return out
