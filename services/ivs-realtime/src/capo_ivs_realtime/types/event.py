"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#Event``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.event_error_code
    import capo_ivs_realtime.types.event_name
    import capo_ivs_realtime.types.exchanged_participant_token
    import capo_ivs_realtime.types.participant_id
    import capo_ivs_realtime.types.replica
    import capo_ivs_realtime.types.stage_arn
    import capo_ivs_realtime.types.stage_session_id
    import capo_ivs_realtime.types.time


class Event(TypedDict, closed=True):
    name: NotRequired["capo_ivs_realtime.types.event_name.EventName"]
    """<p>The name of the event.</p>"""
    participant_id: NotRequired["capo_ivs_realtime.types.participant_id.ParticipantId"]
    """<p>Unique identifier for the participant who triggered the event. This is assigned by IVS.</p>"""
    event_time: NotRequired["capo_ivs_realtime.types.time.Time"]
    """<p>ISO 8601 timestamp (returned as a string) for when the event occurred.</p>"""
    remote_participant_id: NotRequired[
        "capo_ivs_realtime.types.participant_id.ParticipantId"
    ]
    """<p>Unique identifier for the remote participant. For a subscribe event, this is the publisher. For a publish or join event, this is null. This is assigned by IVS.</p>"""
    error_code: NotRequired["capo_ivs_realtime.types.event_error_code.EventErrorCode"]
    """<p>If the event is an error event, the error code is provided to give insight into the specific error that occurred. If the event is not an error event, this field is null.</p> <ul> <li> <p> <code>B_FRAME_PRESENT</code> — The participant's stream includes B-frames. For details, see <a href="https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html"> IVS RTMP Publishing</a>.</p> </li> <li> <p> <code>BITRATE_EXCEEDED</code> — The participant exceeded the maximum supported bitrate. For details, see <a href="https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html"> Service Quotas</a>.</p> </li> <li> <p> <code>INSUFFICIENT_CAPABILITIES</code> — The participant tried to take an action that the participant’s token is not allowed to do. For details on participant capabilities, see the <code>capabilities</code> field in <a>CreateParticipantToken</a>.</p> </li> <li> <p> <code>INTERNAL_SERVER_EXCEPTION</code> — The participant failed to publish to the stage due to an internal server error.</p> </li> <li> <p> <code>INVALID_AUDIO_CODEC</code> — The participant is using an invalid audio codec. For details, see <a href="https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html"> Stream Ingest</a>.</p> </li> <li> <p> <code>INVALID_INPUT</code> — The participant is using an invalid input stream.</p> </li> <li> <p> <code>INVALID_PROTOCOL</code> — The participant's IngestConfiguration resource is configured for RTMPS but they tried streaming with RTMP. For details, see <a href="https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html"> IVS RTMP Publishing</a>.</p> </li> <li> <p> <code>INVALID_STREAM_KEY</code> — The participant is using an invalid stream key. For details, see <a href="https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html"> IVS RTMP Publishing</a>.</p> </li> <li> <p> <code>INVALID_VIDEO_CODEC</code> — The participant is using an invalid video codec. For details, see <a href="https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html"> Stream Ingest</a>.</p> </li> <li> <p> <code>PUBLISHER_NOT_FOUND</code> — The participant tried to subscribe to a publisher that doesn’t exist.</p> </li> <li> <p> <code>QUOTA_EXCEEDED</code> — The number of participants who want to publish/subscribe to a stage exceeds the quota. For details, see <a href="https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html"> Service Quotas</a>.</p> </li> <li> <p> <code>RESOLUTION_EXCEEDED</code> — The participant exceeded the maximum supported resolution. For details, see <a href="https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html"> Service Quotas</a>.</p> </li> <li> <p> <code>REUSE_OF_STREAM_KEY</code> — The participant tried to use a stream key that is associated with another active stage session.</p> </li> <li> <p> <code>STREAM_DURATION_EXCEEDED</code> — The participant exceeded the maximum allowed stream duration. For details, see <a href="https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html"> Service Quotas</a>.</p> </li> </ul>"""
    destination_stage_arn: NotRequired["capo_ivs_realtime.types.stage_arn.StageArn"]
    """<p>ARN of the stage where the participant is replicated. Applicable only if the event name is <code>REPLICATION_STARTED</code> or <code>REPLICATION_STOPPED</code>.</p>"""
    destination_session_id: NotRequired[
        "capo_ivs_realtime.types.stage_session_id.StageSessionId"
    ]
    """<p>ID of the session within the destination stage. Applicable only if the event name is <code>REPLICATION_STARTED</code> or <code>REPLICATION_STOPPED</code>.</p>"""
    replica: "capo_ivs_realtime.types.replica.Replica"
    """<p>If true, this indicates the <code>participantId</code> is a replicated participant. If this is a subscribe event, then this flag refers to <code>remoteParticipantId</code>. Default: <code>false</code>.</p>"""
    previous_token: NotRequired[
        "capo_ivs_realtime.types.exchanged_participant_token.ExchangedParticipantToken"
    ]
    """<p>Source participant token for <code>TOKEN_EXCHANGED</code> event.</p>"""
    new_token: NotRequired[
        "capo_ivs_realtime.types.exchanged_participant_token.ExchangedParticipantToken"
    ]
    """<p>Participant token created during <code>TOKEN_EXCHANGED</code> event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Event) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "participant_id" in value:
        out["participantId"] = value["participant_id"]
    if "event_time" in value:
        import capo_ivs_realtime.types.time

        out["eventTime"] = capo_ivs_realtime.types.time.serialize_json(
            value["event_time"]
        )
    if "remote_participant_id" in value:
        out["remoteParticipantId"] = value["remote_participant_id"]
    if "error_code" in value:
        import capo_ivs_realtime.types.event_error_code

        out["errorCode"] = capo_ivs_realtime.types.event_error_code.serialize_json(
            value["error_code"]
        )
    if "destination_stage_arn" in value:
        out["destinationStageArn"] = value["destination_stage_arn"]
    if "destination_session_id" in value:
        out["destinationSessionId"] = value["destination_session_id"]
    out["replica"] = value.get("replica", False)
    if "previous_token" in value:
        import capo_ivs_realtime.types.exchanged_participant_token

        out["previousToken"] = (
            capo_ivs_realtime.types.exchanged_participant_token.serialize_json(
                value["previous_token"]
            )
        )
    if "new_token" in value:
        import capo_ivs_realtime.types.exchanged_participant_token

        out["newToken"] = (
            capo_ivs_realtime.types.exchanged_participant_token.serialize_json(
                value["new_token"]
            )
        )
    return out


def deserialize_json(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("participantId") is not None:
        out["participant_id"] = data["participantId"]
    if data.get("eventTime") is not None:
        import capo_ivs_realtime.types.time

        out["event_time"] = capo_ivs_realtime.types.time.deserialize_json(
            data["eventTime"]
        )
    if data.get("remoteParticipantId") is not None:
        out["remote_participant_id"] = data["remoteParticipantId"]
    if data.get("errorCode") is not None:
        import capo_ivs_realtime.types.event_error_code

        out["error_code"] = capo_ivs_realtime.types.event_error_code.deserialize_json(
            data["errorCode"]
        )
    if data.get("destinationStageArn") is not None:
        out["destination_stage_arn"] = data["destinationStageArn"]
    if data.get("destinationSessionId") is not None:
        out["destination_session_id"] = data["destinationSessionId"]
    if data.get("replica") is not None:
        out["replica"] = data["replica"]
    else:
        out["replica"] = False
    if data.get("previousToken") is not None:
        import capo_ivs_realtime.types.exchanged_participant_token

        out["previous_token"] = (
            capo_ivs_realtime.types.exchanged_participant_token.deserialize_json(
                data["previousToken"]
            )
        )
    if data.get("newToken") is not None:
        import capo_ivs_realtime.types.exchanged_participant_token

        out["new_token"] = (
            capo_ivs_realtime.types.exchanged_participant_token.deserialize_json(
                data["newToken"]
            )
        )
    return out
