"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaEventSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.lambda_event_source_type
    import capo_greengrassv2.types.topic_string


class LambdaEventSource(TypedDict, closed=True):
    topic: "capo_greengrassv2.types.topic_string.TopicString"
    """<p>The topic to which to subscribe to receive event messages.</p>"""
    type: "capo_greengrassv2.types.lambda_event_source_type.LambdaEventSourceType"
    """<p>The type of event source. Choose from the following options:</p> <ul> <li> <p> <code>PUB_SUB</code> – Subscribe to local publish/subscribe messages. This event source type doesn't support MQTT wildcards (<code>+</code> and <code>#</code>) in the event source topic.</p> </li> <li> <p> <code>IOT_CORE</code> – Subscribe to Amazon Web Services IoT Core MQTT messages. This event source type supports MQTT wildcards (<code>+</code> and <code>#</code>) in the event source topic.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaEventSource) -> dict:
    out: dict = {}
    out["topic"] = value["topic"]
    import capo_greengrassv2.types.lambda_event_source_type

    out["type"] = capo_greengrassv2.types.lambda_event_source_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> LambdaEventSource:
    out: LambdaEventSource = {}  # type: ignore[typeddict-item]
    if data.get("topic") is not None:
        out["topic"] = data["topic"]
    else:
        out["topic"] = ""
    if data.get("type") is not None:
        import capo_greengrassv2.types.lambda_event_source_type

        out["type"] = capo_greengrassv2.types.lambda_event_source_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_greengrassv2.types.lambda_event_source_type.LambdaEventSourceType", ""
        )
    return out
