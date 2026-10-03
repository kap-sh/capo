"""Generated from Smithy shape ``com.amazonaws.eventbridge#TestEventPatternRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.event_pattern
    import capo_eventbridge.types.string


class TestEventPatternRequest(TypedDict, closed=True):
    event_pattern: "capo_eventbridge.types.event_pattern.EventPattern"
    """<p>The event pattern. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html">Events and Event Patterns</a> in the <i> <i>Amazon EventBridge User Guide</i> </i>.</p>"""
    event: "capo_eventbridge.types.string.String"
    """<p>The event, in JSON format, to test against the event pattern. The JSON must follow the format specified in <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/aws-events.html">Amazon Web Services Events</a>, and the following fields are mandatory:</p> <ul> <li> <p> <code>id</code> </p> </li> <li> <p> <code>account</code> </p> </li> <li> <p> <code>source</code> </p> </li> <li> <p> <code>time</code> </p> </li> <li> <p> <code>region</code> </p> </li> <li> <p> <code>resources</code> </p> </li> <li> <p> <code>detail-type</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestEventPatternRequest) -> dict:
    out: dict = {}
    out["EventPattern"] = value["event_pattern"]
    out["Event"] = value["event"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TestEventPatternRequest:
    out: TestEventPatternRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventPattern") is not None:
        out["event_pattern"] = data["EventPattern"]
    else:
        raise DeserializationError("TestEventPatternRequest.event_pattern required")
    if data.get("Event") is not None:
        out["event"] = data["Event"]
    else:
        raise DeserializationError("TestEventPatternRequest.event required")
    return out
