"""Generated from Smithy shape ``com.amazonaws.dataexchange#EventActionEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.action
    import capo_dataexchange.types.arn
    import capo_dataexchange.types.event
    import capo_dataexchange.types.id
    import capo_dataexchange.types.timestamp


class EventActionEntry(TypedDict, closed=True):
    action: "capo_dataexchange.types.action.Action"
    """<p>What occurs after a certain event.</p>"""
    arn: "capo_dataexchange.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the event action.</p>"""
    created_at: "capo_dataexchange.types.timestamp.Timestamp"
    """<p>The date and time that the event action was created, in ISO 8601 format.</p>"""
    event: "capo_dataexchange.types.event.Event"
    """<p>What occurs to start an action.</p>"""
    id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the event action.</p>"""
    updated_at: "capo_dataexchange.types.timestamp.Timestamp"
    """<p>The date and time that the event action was last updated, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventActionEntry) -> dict:
    out: dict = {}
    import capo_dataexchange.types.action

    out["Action"] = capo_dataexchange.types.action.serialize_json(value["action"])
    out["Arn"] = value["arn"]
    import capo_dataexchange.types.timestamp

    out["CreatedAt"] = capo_dataexchange.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_dataexchange.types.event

    out["Event"] = capo_dataexchange.types.event.serialize_json(value["event"])
    out["Id"] = value["id"]
    import capo_dataexchange.types.timestamp

    out["UpdatedAt"] = capo_dataexchange.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> EventActionEntry:
    out: EventActionEntry = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_dataexchange.types.action

        out["action"] = capo_dataexchange.types.action.deserialize_json(data["Action"])
    else:
        raise DeserializationError("EventActionEntry.action required")
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("CreatedAt") is not None:
        import capo_dataexchange.types.timestamp

        out["created_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Event") is not None:
        import capo_dataexchange.types.event

        out["event"] = capo_dataexchange.types.event.deserialize_json(data["Event"])
    else:
        raise DeserializationError("EventActionEntry.event required")
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("UpdatedAt") is not None:
        import capo_dataexchange.types.timestamp

        out["updated_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
