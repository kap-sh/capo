"""Generated from Smithy shape ``com.amazonaws.connect#UpdateOutboundEmailContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.update_outbound_email_message_source_type
    import capo_connect.types.update_outbound_raw_message


class UpdateOutboundEmailContent(TypedDict, closed=True):
    message_source_type: "capo_connect.types.update_outbound_email_message_source_type.UpdateOutboundEmailMessageSourceType"
    """<p>The message source type. The only supported value is <code>RAW</code>.</p>"""
    raw_message: (
        "capo_connect.types.update_outbound_raw_message.UpdateOutboundRawMessage"
    )
    """<p>The raw email body content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOutboundEmailContent) -> dict:
    out: dict = {}
    import capo_connect.types.update_outbound_email_message_source_type

    out["MessageSourceType"] = (
        capo_connect.types.update_outbound_email_message_source_type.serialize_json(
            value["message_source_type"]
        )
    )
    import capo_connect.types.update_outbound_raw_message

    out["RawMessage"] = capo_connect.types.update_outbound_raw_message.serialize_json(
        value["raw_message"]
    )
    return out


def deserialize_json(data: dict) -> UpdateOutboundEmailContent:
    out: UpdateOutboundEmailContent = {}  # type: ignore[typeddict-item]
    if data.get("MessageSourceType") is not None:
        import capo_connect.types.update_outbound_email_message_source_type

        out["message_source_type"] = (
            capo_connect.types.update_outbound_email_message_source_type.deserialize_json(
                data["MessageSourceType"]
            )
        )
    else:
        import typing

        out["message_source_type"] = typing.cast(
            "capo_connect.types.update_outbound_email_message_source_type.UpdateOutboundEmailMessageSourceType",
            "",
        )
    if data.get("RawMessage") is not None:
        import capo_connect.types.update_outbound_raw_message

        out["raw_message"] = (
            capo_connect.types.update_outbound_raw_message.deserialize_json(
                data["RawMessage"]
            )
        )
    else:
        raise DeserializationError("UpdateOutboundEmailContent.raw_message required")
    return out


def redact_sensitive(value: UpdateOutboundEmailContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "raw_message" in value:
        import capo_connect.types.update_outbound_raw_message

        out["raw_message"] = (
            capo_connect.types.update_outbound_raw_message.redact_sensitive(
                value["raw_message"]
            )
        )
    return out
