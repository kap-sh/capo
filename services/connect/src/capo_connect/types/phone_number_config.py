"""Generated from Smithy shape ``com.amazonaws.connect#PhoneNumberConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.channel
    import capo_connect.types.phone_type
    import capo_connect.types.sensitive_phone_number


class PhoneNumberConfig(TypedDict, closed=True):
    channel: "capo_connect.types.channel.Channel"
    """<p>The channel for this phone number configuration. <b>Only <code>VOICE</code> is supported for this data type.</b> </p>"""
    phone_type: "capo_connect.types.phone_type.PhoneType"
    """<p>The phone type. Valid values: SOFT_PHONE, DESK_PHONE.</p>"""
    phone_number: NotRequired[
        "capo_connect.types.sensitive_phone_number.SensitivePhoneNumber"
    ]
    """<p>The phone number for the user's desk phone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberConfig) -> dict:
    out: dict = {}
    import capo_connect.types.channel

    out["Channel"] = capo_connect.types.channel.serialize_json(value["channel"])
    import capo_connect.types.phone_type

    out["PhoneType"] = capo_connect.types.phone_type.serialize_json(value["phone_type"])
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    return out


def deserialize_json(data: dict) -> PhoneNumberConfig:
    out: PhoneNumberConfig = {}  # type: ignore[typeddict-item]
    if data.get("Channel") is not None:
        import capo_connect.types.channel

        out["channel"] = capo_connect.types.channel.deserialize_json(data["Channel"])
    else:
        raise DeserializationError("PhoneNumberConfig.channel required")
    if data.get("PhoneType") is not None:
        import capo_connect.types.phone_type

        out["phone_type"] = capo_connect.types.phone_type.deserialize_json(
            data["PhoneType"]
        )
    else:
        raise DeserializationError("PhoneNumberConfig.phone_type required")
    if data.get("PhoneNumber") is not None:
        out["phone_number"] = data["PhoneNumber"]
    return out


def redact_sensitive(value: PhoneNumberConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number" in value:
        out["phone_number"] = "*** Sensitive Data Redacted ***"
    return out
