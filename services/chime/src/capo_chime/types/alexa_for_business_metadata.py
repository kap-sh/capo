"""Generated from Smithy shape ``com.amazonaws.chime#AlexaForBusinessMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.boolean
    import capo_chime.types.sensitive_string


class AlexaForBusinessMetadata(TypedDict, closed=True):
    is_alexa_for_business_enabled: NotRequired["capo_chime.types.boolean.Boolean"]
    """<p>Starts or stops Alexa for Business.</p>"""
    alexa_for_business_room_arn: NotRequired[
        "capo_chime.types.sensitive_string.SensitiveString"
    ]
    """<p>The ARN of the room resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlexaForBusinessMetadata) -> dict:
    out: dict = {}
    if "is_alexa_for_business_enabled" in value:
        out["IsAlexaForBusinessEnabled"] = value["is_alexa_for_business_enabled"]
    if "alexa_for_business_room_arn" in value:
        out["AlexaForBusinessRoomArn"] = value["alexa_for_business_room_arn"]
    return out


def deserialize_json(data: dict) -> AlexaForBusinessMetadata:
    out: AlexaForBusinessMetadata = {}  # type: ignore[typeddict-item]
    if data.get("IsAlexaForBusinessEnabled") is not None:
        out["is_alexa_for_business_enabled"] = data["IsAlexaForBusinessEnabled"]
    if data.get("AlexaForBusinessRoomArn") is not None:
        out["alexa_for_business_room_arn"] = data["AlexaForBusinessRoomArn"]
    return out


def redact_sensitive(value: AlexaForBusinessMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "alexa_for_business_room_arn" in value:
        out["alexa_for_business_room_arn"] = "*** Sensitive Data Redacted ***"
    return out
