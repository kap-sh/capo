"""Generated from Smithy shape ``com.amazonaws.ivs#CreateRecordingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs.types.destination_configuration
    import capo_ivs.types.recording_configuration_name
    import capo_ivs.types.recording_reconnect_window_seconds
    import capo_ivs.types.rendition_configuration
    import capo_ivs.types.tags
    import capo_ivs.types.thumbnail_configuration


class CreateRecordingConfigurationRequest(TypedDict, closed=True):
    name: NotRequired[
        "capo_ivs.types.recording_configuration_name.RecordingConfigurationName"
    ]
    """<p>Recording-configuration name. The value does not need to be unique.</p>"""
    destination_configuration: (
        "capo_ivs.types.destination_configuration.DestinationConfiguration"
    )
    """<p>A complex type that contains a destination configuration for where recorded video will be stored.</p>"""
    tags: NotRequired["capo_ivs.types.tags.Tags"]
    """<p>Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""
    thumbnail_configuration: NotRequired[
        "capo_ivs.types.thumbnail_configuration.ThumbnailConfiguration"
    ]
    """<p>A complex type that allows you to enable/disable the recording of thumbnails for a live session and modify the interval at which thumbnails are generated for the live session.</p>"""
    recording_reconnect_window_seconds: "capo_ivs.types.recording_reconnect_window_seconds.RecordingReconnectWindowSeconds"
    """<p>If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together. Default: 0.</p>"""
    rendition_configuration: NotRequired[
        "capo_ivs.types.rendition_configuration.RenditionConfiguration"
    ]
    """<p>Object that describes which renditions should be recorded for a stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecordingConfigurationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    import capo_ivs.types.destination_configuration

    out["destinationConfiguration"] = (
        capo_ivs.types.destination_configuration.serialize_json(
            value["destination_configuration"]
        )
    )
    if "tags" in value:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.serialize_json(value["tags"])
    if "thumbnail_configuration" in value:
        import capo_ivs.types.thumbnail_configuration

        out["thumbnailConfiguration"] = (
            capo_ivs.types.thumbnail_configuration.serialize_json(
                value["thumbnail_configuration"]
            )
        )
    out["recordingReconnectWindowSeconds"] = value.get(
        "recording_reconnect_window_seconds", 0
    )
    if "rendition_configuration" in value:
        import capo_ivs.types.rendition_configuration

        out["renditionConfiguration"] = (
            capo_ivs.types.rendition_configuration.serialize_json(
                value["rendition_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRecordingConfigurationRequest:
    out: CreateRecordingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("destinationConfiguration") is not None:
        import capo_ivs.types.destination_configuration

        out["destination_configuration"] = (
            capo_ivs.types.destination_configuration.deserialize_json(
                data["destinationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRecordingConfigurationRequest.destination_configuration required"
        )
    if data.get("tags") is not None:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.deserialize_json(data["tags"])
    if data.get("thumbnailConfiguration") is not None:
        import capo_ivs.types.thumbnail_configuration

        out["thumbnail_configuration"] = (
            capo_ivs.types.thumbnail_configuration.deserialize_json(
                data["thumbnailConfiguration"]
            )
        )
    if data.get("recordingReconnectWindowSeconds") is not None:
        out["recording_reconnect_window_seconds"] = data[
            "recordingReconnectWindowSeconds"
        ]
    else:
        out["recording_reconnect_window_seconds"] = 0
    if data.get("renditionConfiguration") is not None:
        import capo_ivs.types.rendition_configuration

        out["rendition_configuration"] = (
            capo_ivs.types.rendition_configuration.deserialize_json(
                data["renditionConfiguration"]
            )
        )
    return out
