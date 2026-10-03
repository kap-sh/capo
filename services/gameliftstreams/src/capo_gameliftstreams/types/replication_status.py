"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ReplicationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.location_name
    import capo_gameliftstreams.types.replication_status_type


class ReplicationStatus(TypedDict, closed=True):
    location: NotRequired["capo_gameliftstreams.types.location_name.LocationName"]
    """<p> A location's name. For example, <code>us-east-1</code>. For a complete list of locations that Amazon GameLift Streams supports, refer to <a href="https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html">Regions, quotas, and limitations</a> in the <i>Amazon GameLift Streams Developer Guide</i>. </p>"""
    status: NotRequired[
        "capo_gameliftstreams.types.replication_status_type.ReplicationStatusType"
    ]
    """<p>The current status of the replication process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationStatus) -> dict:
    out: dict = {}
    if "location" in value:
        out["Location"] = value["location"]
    if "status" in value:
        import capo_gameliftstreams.types.replication_status_type

        out["Status"] = (
            capo_gameliftstreams.types.replication_status_type.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReplicationStatus:
    out: ReplicationStatus = {}  # type: ignore[typeddict-item]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    if data.get("Status") is not None:
        import capo_gameliftstreams.types.replication_status_type

        out["status"] = (
            capo_gameliftstreams.types.replication_status_type.deserialize_json(
                data["Status"]
            )
        )
    return out
