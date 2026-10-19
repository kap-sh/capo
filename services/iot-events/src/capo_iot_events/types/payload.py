"""Generated from Smithy shape ``com.amazonaws.iotevents#Payload``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.content_expression
    import capo_iot_events.types.payload_type


class Payload(TypedDict, closed=True):
    content_expression: "capo_iot_events.types.content_expression.ContentExpression"
    """<p>The content of the payload. You can use a string expression that includes quoted strings (<code>'<string>'</code>), variables (<code>$variable.<variable-name></code>), input values (<code>$input.<input-name>.<path-to-datum></code>), string concatenations, and quoted strings that contain <code>${}</code> as the content. The recommended maximum size of a content expression is 1 KB.</p>"""
    type: "capo_iot_events.types.payload_type.PayloadType"
    """<p>The value of the payload type can be either <code>STRING</code> or <code>JSON</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Payload) -> dict:
    out: dict = {}
    out["contentExpression"] = value["content_expression"]
    import capo_iot_events.types.payload_type

    out["type"] = capo_iot_events.types.payload_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> Payload:
    out: Payload = {}  # type: ignore[typeddict-item]
    if data.get("contentExpression") is not None:
        out["content_expression"] = data["contentExpression"]
    else:
        out["content_expression"] = ""
    if data.get("type") is not None:
        import capo_iot_events.types.payload_type

        out["type"] = capo_iot_events.types.payload_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast("capo_iot_events.types.payload_type.PayloadType", "")
    return out
