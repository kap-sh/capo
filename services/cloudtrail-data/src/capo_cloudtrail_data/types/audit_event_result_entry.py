"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#AuditEventResultEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail_data.types.uuid


class AuditEventResultEntry(TypedDict, closed=True):
    id: "capo_cloudtrail_data.types.uuid.Uuid"
    """<p>The original event ID from the source event.</p>"""
    event_id: "capo_cloudtrail_data.types.uuid.Uuid"
    """<p>The event ID assigned by CloudTrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditEventResultEntry) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["eventID"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> AuditEventResultEntry:
    out: AuditEventResultEntry = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("eventID") is not None:
        out["event_id"] = data["eventID"]
    else:
        out["event_id"] = ""
    return out
