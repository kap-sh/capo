"""Generated from Smithy shape ``com.amazonaws.ivs#ThumbnailConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.recording_mode
    import capo_ivs.types.target_interval_seconds
    import capo_ivs.types.thumbnail_configuration_resolution
    import capo_ivs.types.thumbnail_configuration_storage_list


class ThumbnailConfiguration(TypedDict, closed=True):
    recording_mode: NotRequired["capo_ivs.types.recording_mode.RecordingMode"]
    """<p>Thumbnail recording mode. Default: <code>INTERVAL</code>.</p>"""
    target_interval_seconds: NotRequired[
        "capo_ivs.types.target_interval_seconds.TargetIntervalSeconds"
    ]
    """<p>The targeted thumbnail-generation interval in seconds. This is configurable (and required) only if <code>recordingMode</code> is <code>INTERVAL</code>. Default: 60.</p> <p> <b>Important:</b> For the <code>BASIC</code> channel type, or the <code>STANDARD</code> channel type with multitrack input, setting a value for <code>targetIntervalSeconds</code> does not guarantee that thumbnails are generated at the specified interval. For thumbnails to be generated at the <code>targetIntervalSeconds</code> interval, the <code>IDR/Keyframe</code> value for the input video must be less than the <code>targetIntervalSeconds</code> value. See <a href="https://docs.aws.amazon.com/ivs/latest/userguide/streaming-config.html"> Amazon IVS Streaming Configuration</a> for information on setting <code>IDR/Keyframe</code> to the recommended value in video-encoder settings.</p>"""
    resolution: NotRequired[
        "capo_ivs.types.thumbnail_configuration_resolution.ThumbnailConfigurationResolution"
    ]
    """<p>Indicates the desired resolution of recorded thumbnails. Thumbnails are recorded at the selected resolution if the corresponding rendition is available during the stream; otherwise, they are recorded at source resolution. For more information about resolution values and their corresponding height and width dimensions, see <a href="https://docs.aws.amazon.com/ivs/latest/userguide/record-to-s3.html">Auto-Record to Amazon S3</a>. Default: Null (source resolution is returned).</p>"""
    storage: NotRequired[
        "capo_ivs.types.thumbnail_configuration_storage_list.ThumbnailConfigurationStorageList"
    ]
    """<p>Indicates the format in which thumbnails are recorded. <code>SEQUENTIAL</code> records all generated thumbnails in a serial manner, to the media/thumbnails directory. <code>LATEST</code> saves the latest thumbnail in media/latest_thumbnail/thumb.jpg and overwrites it at the interval specified by <code>targetIntervalSeconds</code>. You can enable both <code>SEQUENTIAL</code> and <code>LATEST</code>. Default: <code>SEQUENTIAL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThumbnailConfiguration) -> dict:
    out: dict = {}
    if "recording_mode" in value:
        out["recordingMode"] = value["recording_mode"]
    if "target_interval_seconds" in value:
        out["targetIntervalSeconds"] = value["target_interval_seconds"]
    if "resolution" in value:
        import capo_ivs.types.thumbnail_configuration_resolution

        out["resolution"] = (
            capo_ivs.types.thumbnail_configuration_resolution.serialize_json(
                value["resolution"]
            )
        )
    if "storage" in value:
        import capo_ivs.types.thumbnail_configuration_storage_list

        out["storage"] = (
            capo_ivs.types.thumbnail_configuration_storage_list.serialize_json(
                value["storage"]
            )
        )
    return out


def deserialize_json(data: dict) -> ThumbnailConfiguration:
    out: ThumbnailConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("recordingMode") is not None:
        out["recording_mode"] = data["recordingMode"]
    if data.get("targetIntervalSeconds") is not None:
        out["target_interval_seconds"] = data["targetIntervalSeconds"]
    if data.get("resolution") is not None:
        import capo_ivs.types.thumbnail_configuration_resolution

        out["resolution"] = (
            capo_ivs.types.thumbnail_configuration_resolution.deserialize_json(
                data["resolution"]
            )
        )
    if data.get("storage") is not None:
        import capo_ivs.types.thumbnail_configuration_storage_list

        out["storage"] = (
            capo_ivs.types.thumbnail_configuration_storage_list.deserialize_json(
                data["storage"]
            )
        )
    return out
