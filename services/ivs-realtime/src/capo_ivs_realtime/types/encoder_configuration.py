"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#EncoderConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs_realtime.types.encoder_configuration_arn
    import capo_ivs_realtime.types.encoder_configuration_name
    import capo_ivs_realtime.types.tags
    import capo_ivs_realtime.types.video


class EncoderConfiguration(TypedDict, closed=True):
    arn: "capo_ivs_realtime.types.encoder_configuration_arn.EncoderConfigurationArn"
    """<p>ARN of the EncoderConfiguration resource.</p>"""
    name: NotRequired[
        "capo_ivs_realtime.types.encoder_configuration_name.EncoderConfigurationName"
    ]
    """<p>Optional name to identify the resource.</p>"""
    video: NotRequired["capo_ivs_realtime.types.video.Video"]
    """<p>Video configuration. Default: video resolution 1280x720, bitrate 2500 kbps, 30 fps</p>"""
    tags: NotRequired["capo_ivs_realtime.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncoderConfiguration) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "video" in value:
        import capo_ivs_realtime.types.video

        out["video"] = capo_ivs_realtime.types.video.serialize_json(value["video"])
    if "tags" in value:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> EncoderConfiguration:
    out: EncoderConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("EncoderConfiguration.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("video") is not None:
        import capo_ivs_realtime.types.video

        out["video"] = capo_ivs_realtime.types.video.deserialize_json(data["video"])
    if data.get("tags") is not None:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.deserialize_json(data["tags"])
    return out
