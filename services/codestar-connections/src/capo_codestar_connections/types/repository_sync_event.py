"""Generated from Smithy shape ``com.amazonaws.codestarconnections#RepositorySyncEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_connections.types.event
    import capo_codestar_connections.types.external_id
    import capo_codestar_connections.types.timestamp
    import capo_codestar_connections.types.type


class RepositorySyncEvent(TypedDict, closed=True):
    event: "capo_codestar_connections.types.event.Event"
    """<p>A description of a repository sync event.</p>"""
    external_id: NotRequired["capo_codestar_connections.types.external_id.ExternalId"]
    """<p>The ID for a repository sync event.</p>"""
    time: "capo_codestar_connections.types.timestamp.Timestamp"
    """<p>The time that a repository sync event occurred.</p>"""
    type: "capo_codestar_connections.types.type.Type"
    """<p>The event type for a repository sync event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySyncEvent) -> dict:
    out: dict = {}
    out["Event"] = value["event"]
    if "external_id" in value:
        out["ExternalId"] = value["external_id"]
    import capo_codestar_connections.types.timestamp

    out["Time"] = capo_codestar_connections.types.timestamp.serialize_aws_json_1_0(
        value["time"]
    )
    out["Type"] = value["type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RepositorySyncEvent:
    out: RepositorySyncEvent = {}  # type: ignore[typeddict-item]
    if data.get("Event") is not None:
        out["event"] = data["Event"]
    else:
        out["event"] = ""
    if data.get("ExternalId") is not None:
        out["external_id"] = data["ExternalId"]
    if data.get("Time") is not None:
        import capo_codestar_connections.types.timestamp

        out["time"] = (
            capo_codestar_connections.types.timestamp.deserialize_aws_json_1_0(
                data["Time"]
            )
        )
    else:
        import datetime

        out["time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    return out
