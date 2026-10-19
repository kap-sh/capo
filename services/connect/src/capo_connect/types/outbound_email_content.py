"""Generated from Smithy shape ``com.amazonaws.connect#OutboundEmailContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.outbound_message_source_type
    import capo_connect.types.outbound_raw_message
    import capo_connect.types.templated_message_config


class OutboundEmailContent(TypedDict, closed=True):
    message_source_type: (
        "capo_connect.types.outbound_message_source_type.OutboundMessageSourceType"
    )
    """<p>The message source type, that is, <code>RAW</code> or <code>TEMPLATE</code>.</p>"""
    templated_message_config: NotRequired[
        "capo_connect.types.templated_message_config.TemplatedMessageConfig"
    ]
    """<p>Information about template message configuration.</p>"""
    raw_message: NotRequired[
        "capo_connect.types.outbound_raw_message.OutboundRawMessage"
    ]
    """<p>The raw email body content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutboundEmailContent) -> dict:
    out: dict = {}
    import capo_connect.types.outbound_message_source_type

    out["MessageSourceType"] = (
        capo_connect.types.outbound_message_source_type.serialize_json(
            value["message_source_type"]
        )
    )
    if "templated_message_config" in value:
        import capo_connect.types.templated_message_config

        out["TemplatedMessageConfig"] = (
            capo_connect.types.templated_message_config.serialize_json(
                value["templated_message_config"]
            )
        )
    if "raw_message" in value:
        import capo_connect.types.outbound_raw_message

        out["RawMessage"] = capo_connect.types.outbound_raw_message.serialize_json(
            value["raw_message"]
        )
    return out


def deserialize_json(data: dict) -> OutboundEmailContent:
    out: OutboundEmailContent = {}  # type: ignore[typeddict-item]
    if data.get("MessageSourceType") is not None:
        import capo_connect.types.outbound_message_source_type

        out["message_source_type"] = (
            capo_connect.types.outbound_message_source_type.deserialize_json(
                data["MessageSourceType"]
            )
        )
    else:
        import typing

        out["message_source_type"] = typing.cast(
            "capo_connect.types.outbound_message_source_type.OutboundMessageSourceType",
            "",
        )
    if data.get("TemplatedMessageConfig") is not None:
        import capo_connect.types.templated_message_config

        out["templated_message_config"] = (
            capo_connect.types.templated_message_config.deserialize_json(
                data["TemplatedMessageConfig"]
            )
        )
    if data.get("RawMessage") is not None:
        import capo_connect.types.outbound_raw_message

        out["raw_message"] = capo_connect.types.outbound_raw_message.deserialize_json(
            data["RawMessage"]
        )
    return out


def redact_sensitive(value: OutboundEmailContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "raw_message" in value:
        import capo_connect.types.outbound_raw_message

        out["raw_message"] = capo_connect.types.outbound_raw_message.redact_sensitive(
            value["raw_message"]
        )
    return out
