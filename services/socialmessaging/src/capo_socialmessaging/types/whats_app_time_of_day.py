"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppTimeOfDay``."""

from typing_extensions import TypedDict


class WhatsAppTimeOfDay(TypedDict, closed=True):
    hours: "int"
    """<p>The hour of the day, from 0 to 23.</p>"""
    minutes: "int"
    """<p>The minute of the hour, from 0 to 59.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppTimeOfDay) -> dict:
    out: dict = {}
    out["hours"] = value["hours"]
    out["minutes"] = value["minutes"]
    return out


def deserialize_json(data: dict) -> WhatsAppTimeOfDay:
    out: WhatsAppTimeOfDay = {}  # type: ignore[typeddict-item]
    if data.get("hours") is not None:
        out["hours"] = data["hours"]
    else:
        out["hours"] = 0
    if data.get("minutes") is not None:
        out["minutes"] = data["minutes"]
    else:
        out["minutes"] = 0
    return out
