"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#MessageAttributeValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.message_attribute_string_values


class MessageAttributeValue(TypedDict, closed=True):
    string_values: NotRequired[
        "capo_chime_sdk_messaging.types.message_attribute_string_values.MessageAttributeStringValues"
    ]
    """<p>The strings in a message attribute value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageAttributeValue) -> dict:
    out: dict = {}
    if "string_values" in value:
        import capo_chime_sdk_messaging.types.message_attribute_string_values

        out["StringValues"] = (
            capo_chime_sdk_messaging.types.message_attribute_string_values.serialize_json(
                value["string_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> MessageAttributeValue:
    out: MessageAttributeValue = {}  # type: ignore[typeddict-item]
    if data.get("StringValues") is not None:
        import capo_chime_sdk_messaging.types.message_attribute_string_values

        out["string_values"] = (
            capo_chime_sdk_messaging.types.message_attribute_string_values.deserialize_json(
                data["StringValues"]
            )
        )
    return out


def redact_sensitive(value: MessageAttributeValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "string_values" in value:
        import capo_chime_sdk_messaging.types.message_attribute_string_values

        out["string_values"] = (
            capo_chime_sdk_messaging.types.message_attribute_string_values.redact_sensitive(
                value["string_values"]
            )
        )
    return out
