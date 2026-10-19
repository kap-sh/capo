"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.test_run_event_attributes


class TestRunEvent(TypedDict, closed=True):
    event_id: "str"
    """<p>The unique identifier of the event.</p>"""
    event_type: "str"
    """<p>The type of the event, such as action_started, action_completed, or rto_recovery_detected.</p>"""
    message: "str"
    """<p>A human-readable description of what happened.</p>"""
    timestamp: "datetime.datetime"
    """<p>The timestamp when the event occurred.</p>"""
    attributes: NotRequired[
        "capo_resiliencehubv2.types.test_run_event_attributes.TestRunEventAttributes"
    ]
    """<p>Machine-parseable key-value attributes for the event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRunEvent) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    out["eventType"] = value["event_type"]
    out["message"] = value["message"]
    import capo_resiliencehubv2.types._prelude.timestamp

    out["timestamp"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    if "attributes" in value:
        import capo_resiliencehubv2.types.test_run_event_attributes

        out["attributes"] = (
            capo_resiliencehubv2.types.test_run_event_attributes.serialize_json(
                value["attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestRunEvent:
    out: TestRunEvent = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    else:
        out["event_type"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("timestamp") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["timestamp"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("attributes") is not None:
        import capo_resiliencehubv2.types.test_run_event_attributes

        out["attributes"] = (
            capo_resiliencehubv2.types.test_run_event_attributes.deserialize_json(
                data["attributes"]
            )
        )
    return out
