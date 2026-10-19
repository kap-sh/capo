"""Generated from Smithy shape ``com.amazonaws.codeconnections#ResourceSyncEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.event
    import capo_codeconnections.types.external_id
    import capo_codeconnections.types.timestamp
    import capo_codeconnections.types.type


class ResourceSyncEvent(TypedDict, closed=True):
    event: "capo_codeconnections.types.event.Event"
    """<p>The event for a resource sync event.</p>"""
    external_id: NotRequired["capo_codeconnections.types.external_id.ExternalId"]
    """<p>The ID for a resource sync event.</p>"""
    time: "capo_codeconnections.types.timestamp.Timestamp"
    """<p>The time that a resource sync event occurred.</p>"""
    type: "capo_codeconnections.types.type.Type"
    """<p>The type of resource sync event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSyncEvent) -> dict:
    out: dict = {}
    out["Event"] = value["event"]
    if "external_id" in value:
        out["ExternalId"] = value["external_id"]
    import capo_codeconnections.types.timestamp

    out["Time"] = capo_codeconnections.types.timestamp.serialize_aws_json_1_0(
        value["time"]
    )
    out["Type"] = value["type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceSyncEvent:
    out: ResourceSyncEvent = {}  # type: ignore[typeddict-item]
    if data.get("Event") is not None:
        out["event"] = data["Event"]
    else:
        out["event"] = ""
    if data.get("ExternalId") is not None:
        out["external_id"] = data["ExternalId"]
    if data.get("Time") is not None:
        import capo_codeconnections.types.timestamp

        out["time"] = capo_codeconnections.types.timestamp.deserialize_aws_json_1_0(
            data["Time"]
        )
    else:
        import datetime

        out["time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    return out
