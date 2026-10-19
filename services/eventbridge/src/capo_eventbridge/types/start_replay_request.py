"""Generated from Smithy shape ``com.amazonaws.eventbridge#StartReplayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.archive_arn
    import capo_eventbridge.types.replay_description
    import capo_eventbridge.types.replay_destination
    import capo_eventbridge.types.replay_name
    import capo_eventbridge.types.timestamp


class StartReplayRequest(TypedDict, closed=True):
    replay_name: "capo_eventbridge.types.replay_name.ReplayName"
    """<p>The name of the replay to start.</p>"""
    description: NotRequired[
        "capo_eventbridge.types.replay_description.ReplayDescription"
    ]
    """<p>A description for the replay to start.</p>"""
    event_source_arn: "capo_eventbridge.types.archive_arn.ArchiveArn"
    """<p>The ARN of the archive to replay events from.</p>"""
    event_start_time: "capo_eventbridge.types.timestamp.Timestamp"
    """<p>A time stamp for the time to start replaying events. Only events that occurred between the <code>EventStartTime</code> and <code>EventEndTime</code> are replayed.</p>"""
    event_end_time: "capo_eventbridge.types.timestamp.Timestamp"
    """<p>A time stamp for the time to stop replaying events. Only events that occurred between the <code>EventStartTime</code> and <code>EventEndTime</code> are replayed.</p>"""
    destination: "capo_eventbridge.types.replay_destination.ReplayDestination"
    """<p>A <code>ReplayDestination</code> object that includes details about the destination for the replay.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartReplayRequest) -> dict:
    out: dict = {}
    out["ReplayName"] = value["replay_name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["EventSourceArn"] = value["event_source_arn"]
    import capo_eventbridge.types.timestamp

    out["EventStartTime"] = capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
        value["event_start_time"]
    )
    import capo_eventbridge.types.timestamp

    out["EventEndTime"] = capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
        value["event_end_time"]
    )
    import capo_eventbridge.types.replay_destination

    out["Destination"] = (
        capo_eventbridge.types.replay_destination.serialize_aws_json_1_1(
            value["destination"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartReplayRequest:
    out: StartReplayRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReplayName") is not None:
        out["replay_name"] = data["ReplayName"]
    else:
        out["replay_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EventSourceArn") is not None:
        out["event_source_arn"] = data["EventSourceArn"]
    else:
        out["event_source_arn"] = ""
    if data.get("EventStartTime") is not None:
        import capo_eventbridge.types.timestamp

        out["event_start_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["EventStartTime"]
            )
        )
    else:
        import datetime

        out["event_start_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("EventEndTime") is not None:
        import capo_eventbridge.types.timestamp

        out["event_end_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["EventEndTime"]
            )
        )
    else:
        import datetime

        out["event_end_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Destination") is not None:
        import capo_eventbridge.types.replay_destination

        out["destination"] = (
            capo_eventbridge.types.replay_destination.deserialize_aws_json_1_1(
                data["Destination"]
            )
        )
    else:
        raise DeserializationError("StartReplayRequest.destination required")
    return out
