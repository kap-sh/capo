"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#AuditEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail_data.types.uuid


class AuditEvent(TypedDict, closed=True):
    id: "capo_cloudtrail_data.types.uuid.Uuid"
    """<p>The original event ID from the source event.</p>"""
    event_data: "str"
    """<p>The content of an audit event that comes from the event, such as <code>userIdentity</code>, <code>userAgent</code>, and <code>eventSource</code>.</p>"""
    event_data_checksum: NotRequired["str"]
    """<p>A checksum is a base64-SHA256 algorithm that helps you verify that CloudTrail receives the event that matches with the checksum. Calculate the checksum by running a command like the following:</p> <p> <code>printf %s <i>$eventdata</i> | openssl dgst -binary -sha256 | base64</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditEvent) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["eventData"] = value["event_data"]
    if "event_data_checksum" in value:
        out["eventDataChecksum"] = value["event_data_checksum"]
    return out


def deserialize_json(data: dict) -> AuditEvent:
    out: AuditEvent = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("eventData") is not None:
        out["event_data"] = data["eventData"]
    else:
        out["event_data"] = ""
    if data.get("eventDataChecksum") is not None:
        out["event_data_checksum"] = data["eventDataChecksum"]
    return out
