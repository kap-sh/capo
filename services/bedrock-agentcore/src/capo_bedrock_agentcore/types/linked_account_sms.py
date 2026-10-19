"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LinkedAccountSms``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.phone_number


class LinkedAccountSms(TypedDict, closed=True):
    phone_number: "capo_bedrock_agentcore.types.phone_number.PhoneNumber"
    """<p>The phone number in E.164 format (e.g., +1234567890).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkedAccountSms) -> dict:
    out: dict = {}
    out["phoneNumber"] = value["phone_number"]
    return out


def deserialize_json(data: dict) -> LinkedAccountSms:
    out: LinkedAccountSms = {}  # type: ignore[typeddict-item]
    if data.get("phoneNumber") is not None:
        out["phone_number"] = data["phoneNumber"]
    else:
        out["phone_number"] = ""
    return out
