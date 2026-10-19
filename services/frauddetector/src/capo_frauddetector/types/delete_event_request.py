"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteEventRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.delete_audit_history
    import capo_frauddetector.types.identifier


class DeleteEventRequest(TypedDict, closed=True):
    event_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The ID of the event to delete.</p>"""
    event_type_name: "capo_frauddetector.types.identifier.identifier"
    """<p>The name of the event type.</p>"""
    delete_audit_history: NotRequired[
        "capo_frauddetector.types.delete_audit_history.DeleteAuditHistory"
    ]
    """<p>Specifies whether or not to delete any predictions associated with the event. If set to <code>True</code>, </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEventRequest) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    out["eventTypeName"] = value["event_type_name"]
    if "delete_audit_history" in value:
        out["deleteAuditHistory"] = value["delete_audit_history"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEventRequest:
    out: DeleteEventRequest = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    if data.get("eventTypeName") is not None:
        out["event_type_name"] = data["eventTypeName"]
    else:
        out["event_type_name"] = ""
    if data.get("deleteAuditHistory") is not None:
        out["delete_audit_history"] = data["deleteAuditHistory"]
    return out
