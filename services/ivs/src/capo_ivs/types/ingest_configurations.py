"""Generated from Smithy shape ``com.amazonaws.ivs#IngestConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.audio_configuration_list
    import capo_ivs.types.video_configuration_list


class IngestConfigurations(TypedDict, closed=True):
    video_configurations: (
        "capo_ivs.types.video_configuration_list.VideoConfigurationList"
    )
    """<p>Encoder settings for video</p>"""
    audio_configurations: (
        "capo_ivs.types.audio_configuration_list.AudioConfigurationList"
    )
    """<p>Encoder settings for audio.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestConfigurations) -> dict:
    out: dict = {}
    import capo_ivs.types.video_configuration_list

    out["videoConfigurations"] = capo_ivs.types.video_configuration_list.serialize_json(
        value["video_configurations"]
    )
    import capo_ivs.types.audio_configuration_list

    out["audioConfigurations"] = capo_ivs.types.audio_configuration_list.serialize_json(
        value["audio_configurations"]
    )
    return out


def deserialize_json(data: dict) -> IngestConfigurations:
    out: IngestConfigurations = {}  # type: ignore[typeddict-item]
    if data.get("videoConfigurations") is not None:
        import capo_ivs.types.video_configuration_list

        out["video_configurations"] = (
            capo_ivs.types.video_configuration_list.deserialize_json(
                data["videoConfigurations"]
            )
        )
    else:
        out["video_configurations"] = []
    if data.get("audioConfigurations") is not None:
        import capo_ivs.types.audio_configuration_list

        out["audio_configurations"] = (
            capo_ivs.types.audio_configuration_list.deserialize_json(
                data["audioConfigurations"]
            )
        )
    else:
        out["audio_configurations"] = []
    return out
