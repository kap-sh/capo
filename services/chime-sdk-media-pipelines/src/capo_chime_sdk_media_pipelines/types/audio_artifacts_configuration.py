"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#AudioArtifactsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.audio_mux_type


class AudioArtifactsConfiguration(TypedDict, closed=True):
    mux_type: "capo_chime_sdk_media_pipelines.types.audio_mux_type.AudioMuxType"
    """<p>The MUX type of the audio artifact configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioArtifactsConfiguration) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.audio_mux_type

    out["MuxType"] = capo_chime_sdk_media_pipelines.types.audio_mux_type.serialize_json(
        value["mux_type"]
    )
    return out


def deserialize_json(data: dict) -> AudioArtifactsConfiguration:
    out: AudioArtifactsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("MuxType") is not None:
        import capo_chime_sdk_media_pipelines.types.audio_mux_type

        out["mux_type"] = (
            capo_chime_sdk_media_pipelines.types.audio_mux_type.deserialize_json(
                data["MuxType"]
            )
        )
    else:
        import typing

        out["mux_type"] = typing.cast(
            "capo_chime_sdk_media_pipelines.types.audio_mux_type.AudioMuxType", ""
        )
    return out
