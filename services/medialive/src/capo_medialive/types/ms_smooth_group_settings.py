"""Generated from Smithy shape ``com.amazonaws.medialive#MsSmoothGroupSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0
    import capo_medialive.types.__integer_min0_max10000
    import capo_medialive.types.__integer_min1
    import capo_medialive.types.__string
    import capo_medialive.types.input_loss_action_for_ms_smooth_out
    import capo_medialive.types.output_location_ref
    import capo_medialive.types.smooth_group_audio_only_timecode_control
    import capo_medialive.types.smooth_group_certificate_mode
    import capo_medialive.types.smooth_group_event_id_mode
    import capo_medialive.types.smooth_group_event_stop_behavior
    import capo_medialive.types.smooth_group_segmentation_mode
    import capo_medialive.types.smooth_group_sparse_track_type
    import capo_medialive.types.smooth_group_stream_manifest_behavior
    import capo_medialive.types.smooth_group_timestamp_offset_mode


class MsSmoothGroupSettings(TypedDict, closed=True):
    acquisition_point_id: NotRequired["capo_medialive.types.__string.__string"]
    """The ID to include in each message in the sparse track. Ignored if sparseTrackType is NONE."""
    audio_only_timecode_control: NotRequired[
        "capo_medialive.types.smooth_group_audio_only_timecode_control.SmoothGroupAudioOnlyTimecodeControl"
    ]
    """If set to passthrough for an audio-only MS Smooth output, the fragment absolute time will be set to the current timecode. This option does not write timecodes to the audio elementary stream."""
    certificate_mode: NotRequired[
        "capo_medialive.types.smooth_group_certificate_mode.SmoothGroupCertificateMode"
    ]
    """If set to verifyAuthenticity, verify the https certificate chain to a trusted Certificate Authority (CA). This will cause https outputs to self-signed certificates to fail."""
    connection_retry_interval: NotRequired[
        "capo_medialive.types.__integer_min0.__integerMin0"
    ]
    """Number of seconds to wait before retrying connection to the IIS server if the connection is lost. Content will be cached during this time and the cache will be be delivered to the IIS server once the connection is re-established."""
    destination: NotRequired[
        "capo_medialive.types.output_location_ref.OutputLocationRef"
    ]
    """Smooth Streaming publish point on an IIS server. Elemental Live acts as a "Push" encoder to IIS."""
    event_id: NotRequired["capo_medialive.types.__string.__string"]
    """MS Smooth event ID to be sent to the IIS server. Should only be specified if eventIdMode is set to useConfigured."""
    event_id_mode: NotRequired[
        "capo_medialive.types.smooth_group_event_id_mode.SmoothGroupEventIdMode"
    ]
    """Specifies whether or not to send an event ID to the IIS server. If no event ID is sent and the same Live Event is used without changing the publishing point, clients might see cached video from the previous run. Options: - "useConfigured" - use the value provided in eventId - "useTimestamp" - generate and send an event ID based on the current timestamp - "noEventId" - do not send an event ID to the IIS server."""
    event_stop_behavior: NotRequired[
        "capo_medialive.types.smooth_group_event_stop_behavior.SmoothGroupEventStopBehavior"
    ]
    """When set to sendEos, send EOS signal to IIS server when stopping the event"""
    filecache_duration: NotRequired["capo_medialive.types.__integer_min0.__integerMin0"]
    """Size in seconds of file cache for streaming outputs."""
    fragment_length: NotRequired["capo_medialive.types.__integer_min1.__integerMin1"]
    """Length of mp4 fragments to generate (in seconds). Fragment length must be compatible with GOP size and framerate."""
    input_loss_action: NotRequired[
        "capo_medialive.types.input_loss_action_for_ms_smooth_out.InputLossActionForMsSmoothOut"
    ]
    """Parameter that control output group behavior on input loss."""
    num_retries: NotRequired["capo_medialive.types.__integer_min0.__integerMin0"]
    """Number of retry attempts."""
    restart_delay: NotRequired["capo_medialive.types.__integer_min0.__integerMin0"]
    """Number of seconds before initiating a restart due to output failure, due to exhausting the numRetries on one segment, or exceeding filecacheDuration."""
    segmentation_mode: NotRequired[
        "capo_medialive.types.smooth_group_segmentation_mode.SmoothGroupSegmentationMode"
    ]
    """useInputSegmentation has been deprecated. The configured segment size is always used."""
    send_delay_ms: NotRequired[
        "capo_medialive.types.__integer_min0_max10000.__integerMin0Max10000"
    ]
    """Number of milliseconds to delay the output from the second pipeline."""
    sparse_track_type: NotRequired[
        "capo_medialive.types.smooth_group_sparse_track_type.SmoothGroupSparseTrackType"
    ]
    """Identifies the type of data to place in the sparse track: - SCTE35: Insert SCTE-35 messages from the source content. With each message, insert an IDR frame to start a new segment. - SCTE35_WITHOUT_SEGMENTATION: Insert SCTE-35 messages from the source content. With each message, insert an IDR frame but don't start a new segment. - NONE: Don't generate a sparse track for any outputs in this output group."""
    stream_manifest_behavior: NotRequired[
        "capo_medialive.types.smooth_group_stream_manifest_behavior.SmoothGroupStreamManifestBehavior"
    ]
    """When set to send, send stream manifest so publishing point doesn't start until all streams start."""
    timestamp_offset: NotRequired["capo_medialive.types.__string.__string"]
    """Timestamp offset for the event. Only used if timestampOffsetMode is set to useConfiguredOffset."""
    timestamp_offset_mode: NotRequired[
        "capo_medialive.types.smooth_group_timestamp_offset_mode.SmoothGroupTimestampOffsetMode"
    ]
    """Type of timestamp date offset to use. - useEventStartDate: Use the date the event was started as the offset - useConfiguredOffset: Use an explicitly configured date as the offset"""


# --- restJson1 ser/de ---
def serialize_json(value: MsSmoothGroupSettings) -> dict:
    out: dict = {}
    if "acquisition_point_id" in value:
        out["acquisitionPointId"] = value["acquisition_point_id"]
    if "audio_only_timecode_control" in value:
        import capo_medialive.types.smooth_group_audio_only_timecode_control

        out["audioOnlyTimecodeControl"] = (
            capo_medialive.types.smooth_group_audio_only_timecode_control.serialize_json(
                value["audio_only_timecode_control"]
            )
        )
    if "certificate_mode" in value:
        import capo_medialive.types.smooth_group_certificate_mode

        out["certificateMode"] = (
            capo_medialive.types.smooth_group_certificate_mode.serialize_json(
                value["certificate_mode"]
            )
        )
    if "connection_retry_interval" in value:
        out["connectionRetryInterval"] = value["connection_retry_interval"]
    if "destination" in value:
        import capo_medialive.types.output_location_ref

        out["destination"] = capo_medialive.types.output_location_ref.serialize_json(
            value["destination"]
        )
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "event_id_mode" in value:
        import capo_medialive.types.smooth_group_event_id_mode

        out["eventIdMode"] = (
            capo_medialive.types.smooth_group_event_id_mode.serialize_json(
                value["event_id_mode"]
            )
        )
    if "event_stop_behavior" in value:
        import capo_medialive.types.smooth_group_event_stop_behavior

        out["eventStopBehavior"] = (
            capo_medialive.types.smooth_group_event_stop_behavior.serialize_json(
                value["event_stop_behavior"]
            )
        )
    if "filecache_duration" in value:
        out["filecacheDuration"] = value["filecache_duration"]
    if "fragment_length" in value:
        out["fragmentLength"] = value["fragment_length"]
    if "input_loss_action" in value:
        import capo_medialive.types.input_loss_action_for_ms_smooth_out

        out["inputLossAction"] = (
            capo_medialive.types.input_loss_action_for_ms_smooth_out.serialize_json(
                value["input_loss_action"]
            )
        )
    if "num_retries" in value:
        out["numRetries"] = value["num_retries"]
    if "restart_delay" in value:
        out["restartDelay"] = value["restart_delay"]
    if "segmentation_mode" in value:
        import capo_medialive.types.smooth_group_segmentation_mode

        out["segmentationMode"] = (
            capo_medialive.types.smooth_group_segmentation_mode.serialize_json(
                value["segmentation_mode"]
            )
        )
    if "send_delay_ms" in value:
        out["sendDelayMs"] = value["send_delay_ms"]
    if "sparse_track_type" in value:
        import capo_medialive.types.smooth_group_sparse_track_type

        out["sparseTrackType"] = (
            capo_medialive.types.smooth_group_sparse_track_type.serialize_json(
                value["sparse_track_type"]
            )
        )
    if "stream_manifest_behavior" in value:
        import capo_medialive.types.smooth_group_stream_manifest_behavior

        out["streamManifestBehavior"] = (
            capo_medialive.types.smooth_group_stream_manifest_behavior.serialize_json(
                value["stream_manifest_behavior"]
            )
        )
    if "timestamp_offset" in value:
        out["timestampOffset"] = value["timestamp_offset"]
    if "timestamp_offset_mode" in value:
        import capo_medialive.types.smooth_group_timestamp_offset_mode

        out["timestampOffsetMode"] = (
            capo_medialive.types.smooth_group_timestamp_offset_mode.serialize_json(
                value["timestamp_offset_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> MsSmoothGroupSettings:
    out: MsSmoothGroupSettings = {}  # type: ignore[typeddict-item]
    if data.get("acquisitionPointId") is not None:
        out["acquisition_point_id"] = data["acquisitionPointId"]
    if data.get("audioOnlyTimecodeControl") is not None:
        import capo_medialive.types.smooth_group_audio_only_timecode_control

        out["audio_only_timecode_control"] = (
            capo_medialive.types.smooth_group_audio_only_timecode_control.deserialize_json(
                data["audioOnlyTimecodeControl"]
            )
        )
    if data.get("certificateMode") is not None:
        import capo_medialive.types.smooth_group_certificate_mode

        out["certificate_mode"] = (
            capo_medialive.types.smooth_group_certificate_mode.deserialize_json(
                data["certificateMode"]
            )
        )
    if data.get("connectionRetryInterval") is not None:
        out["connection_retry_interval"] = data["connectionRetryInterval"]
    if data.get("destination") is not None:
        import capo_medialive.types.output_location_ref

        out["destination"] = capo_medialive.types.output_location_ref.deserialize_json(
            data["destination"]
        )
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    if data.get("eventIdMode") is not None:
        import capo_medialive.types.smooth_group_event_id_mode

        out["event_id_mode"] = (
            capo_medialive.types.smooth_group_event_id_mode.deserialize_json(
                data["eventIdMode"]
            )
        )
    if data.get("eventStopBehavior") is not None:
        import capo_medialive.types.smooth_group_event_stop_behavior

        out["event_stop_behavior"] = (
            capo_medialive.types.smooth_group_event_stop_behavior.deserialize_json(
                data["eventStopBehavior"]
            )
        )
    if data.get("filecacheDuration") is not None:
        out["filecache_duration"] = data["filecacheDuration"]
    if data.get("fragmentLength") is not None:
        out["fragment_length"] = data["fragmentLength"]
    if data.get("inputLossAction") is not None:
        import capo_medialive.types.input_loss_action_for_ms_smooth_out

        out["input_loss_action"] = (
            capo_medialive.types.input_loss_action_for_ms_smooth_out.deserialize_json(
                data["inputLossAction"]
            )
        )
    if data.get("numRetries") is not None:
        out["num_retries"] = data["numRetries"]
    if data.get("restartDelay") is not None:
        out["restart_delay"] = data["restartDelay"]
    if data.get("segmentationMode") is not None:
        import capo_medialive.types.smooth_group_segmentation_mode

        out["segmentation_mode"] = (
            capo_medialive.types.smooth_group_segmentation_mode.deserialize_json(
                data["segmentationMode"]
            )
        )
    if data.get("sendDelayMs") is not None:
        out["send_delay_ms"] = data["sendDelayMs"]
    if data.get("sparseTrackType") is not None:
        import capo_medialive.types.smooth_group_sparse_track_type

        out["sparse_track_type"] = (
            capo_medialive.types.smooth_group_sparse_track_type.deserialize_json(
                data["sparseTrackType"]
            )
        )
    if data.get("streamManifestBehavior") is not None:
        import capo_medialive.types.smooth_group_stream_manifest_behavior

        out["stream_manifest_behavior"] = (
            capo_medialive.types.smooth_group_stream_manifest_behavior.deserialize_json(
                data["streamManifestBehavior"]
            )
        )
    if data.get("timestampOffset") is not None:
        out["timestamp_offset"] = data["timestampOffset"]
    if data.get("timestampOffsetMode") is not None:
        import capo_medialive.types.smooth_group_timestamp_offset_mode

        out["timestamp_offset_mode"] = (
            capo_medialive.types.smooth_group_timestamp_offset_mode.deserialize_json(
                data["timestampOffsetMode"]
            )
        )
    return out
