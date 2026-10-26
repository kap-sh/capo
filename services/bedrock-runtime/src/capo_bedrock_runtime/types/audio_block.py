"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AudioBlock``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.audio_format
    import capo_bedrock_runtime.types.audio_source
    import capo_bedrock_runtime.types.error_block


class AudioBlock(TypedDict, closed=True):
    format: "capo_bedrock_runtime.types.audio_format.AudioFormat"
    """<p>The format of the audio data, such as MP3, WAV, FLAC, or other supported audio formats.</p>"""
    source: "capo_bedrock_runtime.types.audio_source.AudioSource"
    """<p>The source of the audio data, which can be provided as raw bytes or an S3 location.</p>"""
    error: NotRequired["capo_bedrock_runtime.types.error_block.ErrorBlock"]
    """<p>Error information if the audio block could not be processed or contains invalid data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioBlock) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.audio_format

    out["format"] = capo_bedrock_runtime.types.audio_format.serialize_json(
        value["format"]
    )
    import capo_bedrock_runtime.types.audio_source

    out["source"] = capo_bedrock_runtime.types.audio_source.serialize_json(
        value["source"]
    )
    if "error" in value:
        import capo_bedrock_runtime.types.error_block

        out["error"] = capo_bedrock_runtime.types.error_block.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> AudioBlock:
    out: AudioBlock = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        import capo_bedrock_runtime.types.audio_format

        out["format"] = capo_bedrock_runtime.types.audio_format.deserialize_json(
            data["format"]
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_bedrock_runtime.types.audio_format.AudioFormat", ""
        )
    if data.get("source") is not None:
        import capo_bedrock_runtime.types.audio_source

        out["source"] = capo_bedrock_runtime.types.audio_source.deserialize_json(
            data["source"]
        )
    else:
        out["source"] = {"$unknown": {"name": ""}}
    if data.get("error") is not None:
        import capo_bedrock_runtime.types.error_block

        out["error"] = capo_bedrock_runtime.types.error_block.deserialize_json(
            data["error"]
        )
    return out


def redact_sensitive(value: AudioBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source" in value:
        out["source"] = "*** Sensitive Data Redacted ***"
    if "error" in value:
        out["error"] = "*** Sensitive Data Redacted ***"
    return out
