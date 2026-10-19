"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#VideoArtifactsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.artifacts_state
    import capo_chime_sdk_media_pipelines.types.video_mux_type


class VideoArtifactsConfiguration(TypedDict, closed=True):
    state: "capo_chime_sdk_media_pipelines.types.artifacts_state.ArtifactsState"
    """<p>Indicates whether the video artifact is enabled or disabled.</p>"""
    mux_type: NotRequired[
        "capo_chime_sdk_media_pipelines.types.video_mux_type.VideoMuxType"
    ]
    """<p>The MUX type of the video artifact configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoArtifactsConfiguration) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.artifacts_state

    out["State"] = capo_chime_sdk_media_pipelines.types.artifacts_state.serialize_json(
        value["state"]
    )
    if "mux_type" in value:
        import capo_chime_sdk_media_pipelines.types.video_mux_type

        out["MuxType"] = (
            capo_chime_sdk_media_pipelines.types.video_mux_type.serialize_json(
                value["mux_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> VideoArtifactsConfiguration:
    out: VideoArtifactsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("State") is not None:
        import capo_chime_sdk_media_pipelines.types.artifacts_state

        out["state"] = (
            capo_chime_sdk_media_pipelines.types.artifacts_state.deserialize_json(
                data["State"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_chime_sdk_media_pipelines.types.artifacts_state.ArtifactsState", ""
        )
    if data.get("MuxType") is not None:
        import capo_chime_sdk_media_pipelines.types.video_mux_type

        out["mux_type"] = (
            capo_chime_sdk_media_pipelines.types.video_mux_type.deserialize_json(
                data["MuxType"]
            )
        )
    return out
