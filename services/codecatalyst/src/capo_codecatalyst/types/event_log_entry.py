"""Generated from Smithy shape ``com.amazonaws.codecatalyst#EventLogEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.event_payload
    import capo_codecatalyst.types.operation_type
    import capo_codecatalyst.types.project_information
    import capo_codecatalyst.types.timestamp
    import capo_codecatalyst.types.user_identity


class EventLogEntry(TypedDict, closed=True):
    id: "str"
    """<p>The system-generated unique ID of the event.</p>"""
    event_name: "str"
    """<p>The name of the event.</p>"""
    event_type: "str"
    """<p>The type of the event.</p>"""
    event_category: "str"
    """<p>The category for the event.</p>"""
    event_source: "str"
    """<p>The source of the event.</p>"""
    event_time: "capo_codecatalyst.types.timestamp.Timestamp"
    """<p>The time the event took place, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a>.</p>"""
    operation_type: "capo_codecatalyst.types.operation_type.OperationType"
    """<p>The type of the event.</p>"""
    user_identity: "capo_codecatalyst.types.user_identity.UserIdentity"
    """<p>The system-generated unique ID of the user whose actions are recorded in the event.</p>"""
    project_information: NotRequired[
        "capo_codecatalyst.types.project_information.ProjectInformation"
    ]
    """<p>Information about the project where the event occurred.</p>"""
    request_id: NotRequired["str"]
    """<p>The system-generated unique ID of the request.</p>"""
    request_payload: NotRequired["capo_codecatalyst.types.event_payload.EventPayload"]
    """<p>Information about the payload of the request.</p>"""
    response_payload: NotRequired["capo_codecatalyst.types.event_payload.EventPayload"]
    """<p>Information about the payload of the response, if any.</p>"""
    error_code: NotRequired["str"]
    """<p>The code of the error, if any.</p>"""
    source_ip_address: NotRequired["str"]
    """<p>The IP address of the user whose actions are recorded in the event.</p>"""
    user_agent: NotRequired["str"]
    """<p>The user agent whose actions are recorded in the event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventLogEntry) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["eventName"] = value["event_name"]
    out["eventType"] = value["event_type"]
    out["eventCategory"] = value["event_category"]
    out["eventSource"] = value["event_source"]
    import capo_codecatalyst._protocol.serialize

    out["eventTime"] = capo_codecatalyst._protocol.serialize.fmt_date_time(
        value["event_time"]
    )
    out["operationType"] = value["operation_type"]
    import capo_codecatalyst.types.user_identity

    out["userIdentity"] = capo_codecatalyst.types.user_identity.serialize_json(
        value["user_identity"]
    )
    if "project_information" in value:
        import capo_codecatalyst.types.project_information

        out["projectInformation"] = (
            capo_codecatalyst.types.project_information.serialize_json(
                value["project_information"]
            )
        )
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "request_payload" in value:
        import capo_codecatalyst.types.event_payload

        out["requestPayload"] = capo_codecatalyst.types.event_payload.serialize_json(
            value["request_payload"]
        )
    if "response_payload" in value:
        import capo_codecatalyst.types.event_payload

        out["responsePayload"] = capo_codecatalyst.types.event_payload.serialize_json(
            value["response_payload"]
        )
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "source_ip_address" in value:
        out["sourceIpAddress"] = value["source_ip_address"]
    if "user_agent" in value:
        out["userAgent"] = value["user_agent"]
    return out


def deserialize_json(data: dict) -> EventLogEntry:
    out: EventLogEntry = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("EventLogEntry.id required")
    if data.get("eventName") is not None:
        out["event_name"] = data["eventName"]
    else:
        raise DeserializationError("EventLogEntry.event_name required")
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    else:
        raise DeserializationError("EventLogEntry.event_type required")
    if data.get("eventCategory") is not None:
        out["event_category"] = data["eventCategory"]
    else:
        raise DeserializationError("EventLogEntry.event_category required")
    if data.get("eventSource") is not None:
        out["event_source"] = data["eventSource"]
    else:
        raise DeserializationError("EventLogEntry.event_source required")
    if data.get("eventTime") is not None:
        import datetime

        out["event_time"] = datetime.datetime.fromisoformat(
            data["eventTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("EventLogEntry.event_time required")
    if data.get("operationType") is not None:
        out["operation_type"] = data["operationType"]
    else:
        raise DeserializationError("EventLogEntry.operation_type required")
    if data.get("userIdentity") is not None:
        import capo_codecatalyst.types.user_identity

        out["user_identity"] = capo_codecatalyst.types.user_identity.deserialize_json(
            data["userIdentity"]
        )
    else:
        raise DeserializationError("EventLogEntry.user_identity required")
    if data.get("projectInformation") is not None:
        import capo_codecatalyst.types.project_information

        out["project_information"] = (
            capo_codecatalyst.types.project_information.deserialize_json(
                data["projectInformation"]
            )
        )
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    if data.get("requestPayload") is not None:
        import capo_codecatalyst.types.event_payload

        out["request_payload"] = capo_codecatalyst.types.event_payload.deserialize_json(
            data["requestPayload"]
        )
    if data.get("responsePayload") is not None:
        import capo_codecatalyst.types.event_payload

        out["response_payload"] = (
            capo_codecatalyst.types.event_payload.deserialize_json(
                data["responsePayload"]
            )
        )
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("sourceIpAddress") is not None:
        out["source_ip_address"] = data["sourceIpAddress"]
    if data.get("userAgent") is not None:
        out["user_agent"] = data["userAgent"]
    return out
