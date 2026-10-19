"""Generated from Smithy shape ``com.amazonaws.socialmessaging#SendWhatsAppConversionEventOutput``."""

from typing_extensions import TypedDict


class SendWhatsAppConversionEventOutput(TypedDict, closed=True):
    request_id: "str"
    """<p>The unique identifier for the conversion event request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendWhatsAppConversionEventOutput) -> dict:
    out: dict = {}
    out["requestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SendWhatsAppConversionEventOutput:
    out: SendWhatsAppConversionEventOutput = {}  # type: ignore[typeddict-item]
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    else:
        out["request_id"] = ""
    return out
