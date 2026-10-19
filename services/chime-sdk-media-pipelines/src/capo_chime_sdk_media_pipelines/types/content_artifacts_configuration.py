"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ContentArtifactsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.artifacts_state
    import capo_chime_sdk_media_pipelines.types.content_mux_type


class ContentArtifactsConfiguration(TypedDict, closed=True):
    state: "capo_chime_sdk_media_pipelines.types.artifacts_state.ArtifactsState"
    """<p>Indicates whether the content artifact is enabled or disabled.</p>"""
    mux_type: NotRequired[
        "capo_chime_sdk_media_pipelines.types.content_mux_type.ContentMuxType"
    ]
    """<p>The MUX type of the artifact configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentArtifactsConfiguration) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.artifacts_state

    out["State"] = capo_chime_sdk_media_pipelines.types.artifacts_state.serialize_json(
        value["state"]
    )
    if "mux_type" in value:
        import capo_chime_sdk_media_pipelines.types.content_mux_type

        out["MuxType"] = (
            capo_chime_sdk_media_pipelines.types.content_mux_type.serialize_json(
                value["mux_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContentArtifactsConfiguration:
    out: ContentArtifactsConfiguration = {}  # type: ignore[typeddict-item]
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
        import capo_chime_sdk_media_pipelines.types.content_mux_type

        out["mux_type"] = (
            capo_chime_sdk_media_pipelines.types.content_mux_type.deserialize_json(
                data["MuxType"]
            )
        )
    return out
