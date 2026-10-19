"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#VideoConcatenationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.artifacts_concatenation_state


class VideoConcatenationConfiguration(TypedDict, closed=True):
    state: "capo_chime_sdk_media_pipelines.types.artifacts_concatenation_state.ArtifactsConcatenationState"
    """<p>Enables or disables the configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoConcatenationConfiguration) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.artifacts_concatenation_state

    out["State"] = (
        capo_chime_sdk_media_pipelines.types.artifacts_concatenation_state.serialize_json(
            value["state"]
        )
    )
    return out


def deserialize_json(data: dict) -> VideoConcatenationConfiguration:
    out: VideoConcatenationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("State") is not None:
        import capo_chime_sdk_media_pipelines.types.artifacts_concatenation_state

        out["state"] = (
            capo_chime_sdk_media_pipelines.types.artifacts_concatenation_state.deserialize_json(
                data["State"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_chime_sdk_media_pipelines.types.artifacts_concatenation_state.ArtifactsConcatenationState",
            "",
        )
    return out
