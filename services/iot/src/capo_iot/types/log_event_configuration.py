"""Generated from Smithy shape ``com.amazonaws.iot#LogEventConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.log_destination
    import capo_iot.types.log_event_type
    import capo_iot.types.log_level


class LogEventConfiguration(TypedDict, closed=True):
    event_type: "capo_iot.types.log_event_type.LogEventType"
    """<p> The type of event to log. These include event types like Connect, Publish, and Disconnect. </p>"""
    log_level: NotRequired["capo_iot.types.log_level.LogLevel"]
    """<p> The logging level for the specified event type. Determines the verbosity of log messages generated for this event type. </p>"""
    log_destination: NotRequired["capo_iot.types.log_destination.LogDestination"]
    """<p> CloudWatch Log Group for event-based logging. Specifies where log events should be sent. The log destination for event-based logging overrides default Log Group for the specified event type and applies to all resources associated with that event. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogEventConfiguration) -> dict:
    out: dict = {}
    out["eventType"] = value["event_type"]
    if "log_level" in value:
        import capo_iot.types.log_level

        out["logLevel"] = capo_iot.types.log_level.serialize_json(value["log_level"])
    if "log_destination" in value:
        out["logDestination"] = value["log_destination"]
    return out


def deserialize_json(data: dict) -> LogEventConfiguration:
    out: LogEventConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    else:
        out["event_type"] = ""
    if data.get("logLevel") is not None:
        import capo_iot.types.log_level

        out["log_level"] = capo_iot.types.log_level.deserialize_json(data["logLevel"])
    if data.get("logDestination") is not None:
        out["log_destination"] = data["logDestination"]
    return out
