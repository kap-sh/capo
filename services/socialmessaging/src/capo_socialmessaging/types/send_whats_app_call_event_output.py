"""Generated from Smithy shape ``com.amazonaws.socialmessaging#SendWhatsAppCallEventOutput``."""

from typing_extensions import TypedDict


class SendWhatsAppCallEventOutput(TypedDict, closed=True):
    call_id: "str"
    """<p>The unique identifier that Meta assigns to the call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendWhatsAppCallEventOutput) -> dict:
    out: dict = {}
    out["callId"] = value["call_id"]
    return out


def deserialize_json(data: dict) -> SendWhatsAppCallEventOutput:
    out: SendWhatsAppCallEventOutput = {}  # type: ignore[typeddict-item]
    if data.get("callId") is not None:
        out["call_id"] = data["callId"]
    else:
        out["call_id"] = ""
    return out
