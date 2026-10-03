"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#AutoParticipantRecordingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs_realtime.types.auto_participant_recording_storage_configuration_arn
    import capo_ivs_realtime.types.participant_recording_hls_configuration
    import capo_ivs_realtime.types.participant_recording_media_type_list
    import capo_ivs_realtime.types.participant_recording_reconnect_window_seconds
    import capo_ivs_realtime.types.participant_thumbnail_configuration
    import capo_ivs_realtime.types.record_participant_replicas


class AutoParticipantRecordingConfiguration(TypedDict, closed=True):
    storage_configuration_arn: "capo_ivs_realtime.types.auto_participant_recording_storage_configuration_arn.AutoParticipantRecordingStorageConfigurationArn"
    """<p>ARN of the <a>StorageConfiguration</a> resource to use for individual participant recording. Default: <code>""</code> (empty string, no storage configuration is specified). Individual participant recording cannot be started unless a storage configuration is specified, when a <a>Stage</a> is created or updated. To disable individual participant recording, set this to <code>""</code>; other fields in this object will get reset to their defaults when sending <code>""</code>. </p>"""
    media_types: NotRequired[
        "capo_ivs_realtime.types.participant_recording_media_type_list.ParticipantRecordingMediaTypeList"
    ]
    """<p>Types of media to be recorded. Default: <code>AUDIO_VIDEO</code>.</p>"""
    thumbnail_configuration: NotRequired[
        "capo_ivs_realtime.types.participant_thumbnail_configuration.ParticipantThumbnailConfiguration"
    ]
    """<p>A complex type that allows you to enable/disable the recording of thumbnails for individual participant recording and modify the interval at which thumbnails are generated for the live session.</p>"""
    recording_reconnect_window_seconds: "capo_ivs_realtime.types.participant_recording_reconnect_window_seconds.ParticipantRecordingReconnectWindowSeconds"
    """<p>If a stage publisher disconnects and then reconnects within the specified interval, the multiple recordings will be considered a single recording and merged together.</p> <p>The default value is 0, which disables merging.</p>"""
    hls_configuration: NotRequired[
        "capo_ivs_realtime.types.participant_recording_hls_configuration.ParticipantRecordingHlsConfiguration"
    ]
    """<p>HLS configuration object for individual participant recording.</p>"""
    record_participant_replicas: (
        "capo_ivs_realtime.types.record_participant_replicas.RecordParticipantReplicas"
    )
    """<p>Optional field to disable replica participant recording. If this is set to <code>false</code> when a participant is a replica, replica participants are not recorded. Default: <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoParticipantRecordingConfiguration) -> dict:
    out: dict = {}
    out["storageConfigurationArn"] = value["storage_configuration_arn"]
    if "media_types" in value:
        import capo_ivs_realtime.types.participant_recording_media_type_list

        out["mediaTypes"] = (
            capo_ivs_realtime.types.participant_recording_media_type_list.serialize_json(
                value["media_types"]
            )
        )
    if "thumbnail_configuration" in value:
        import capo_ivs_realtime.types.participant_thumbnail_configuration

        out["thumbnailConfiguration"] = (
            capo_ivs_realtime.types.participant_thumbnail_configuration.serialize_json(
                value["thumbnail_configuration"]
            )
        )
    out["recordingReconnectWindowSeconds"] = value.get(
        "recording_reconnect_window_seconds", 0
    )
    if "hls_configuration" in value:
        import capo_ivs_realtime.types.participant_recording_hls_configuration

        out["hlsConfiguration"] = (
            capo_ivs_realtime.types.participant_recording_hls_configuration.serialize_json(
                value["hls_configuration"]
            )
        )
    out["recordParticipantReplicas"] = value.get("record_participant_replicas", False)
    return out


def deserialize_json(data: dict) -> AutoParticipantRecordingConfiguration:
    out: AutoParticipantRecordingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("storageConfigurationArn") is not None:
        out["storage_configuration_arn"] = data["storageConfigurationArn"]
    else:
        raise DeserializationError(
            "AutoParticipantRecordingConfiguration.storage_configuration_arn required"
        )
    if data.get("mediaTypes") is not None:
        import capo_ivs_realtime.types.participant_recording_media_type_list

        out["media_types"] = (
            capo_ivs_realtime.types.participant_recording_media_type_list.deserialize_json(
                data["mediaTypes"]
            )
        )
    if data.get("thumbnailConfiguration") is not None:
        import capo_ivs_realtime.types.participant_thumbnail_configuration

        out["thumbnail_configuration"] = (
            capo_ivs_realtime.types.participant_thumbnail_configuration.deserialize_json(
                data["thumbnailConfiguration"]
            )
        )
    if data.get("recordingReconnectWindowSeconds") is not None:
        out["recording_reconnect_window_seconds"] = data[
            "recordingReconnectWindowSeconds"
        ]
    else:
        out["recording_reconnect_window_seconds"] = 0
    if data.get("hlsConfiguration") is not None:
        import capo_ivs_realtime.types.participant_recording_hls_configuration

        out["hls_configuration"] = (
            capo_ivs_realtime.types.participant_recording_hls_configuration.deserialize_json(
                data["hlsConfiguration"]
            )
        )
    if data.get("recordParticipantReplicas") is not None:
        out["record_participant_replicas"] = data["recordParticipantReplicas"]
    else:
        out["record_participant_replicas"] = False
    return out
