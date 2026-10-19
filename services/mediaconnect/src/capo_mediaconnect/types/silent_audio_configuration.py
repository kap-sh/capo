"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SilentAudioConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.content_quality_analysis_state
    import capo_mediaconnect.types.router_cqa_threshold_seconds


class SilentAudioConfiguration(TypedDict, closed=True):
    state: "capo_mediaconnect.types.content_quality_analysis_state.ContentQualityAnalysisState"
    """<p>Indicates whether silent audio detection is enabled or disabled.</p>"""
    threshold_seconds: (
        "capo_mediaconnect.types.router_cqa_threshold_seconds.RouterCqaThresholdSeconds"
    )
    """<p>The number of consecutive seconds of silence that MediaConnect must detect before it reports an issue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SilentAudioConfiguration) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.content_quality_analysis_state

    out["state"] = (
        capo_mediaconnect.types.content_quality_analysis_state.serialize_json(
            value["state"]
        )
    )
    out["thresholdSeconds"] = value["threshold_seconds"]
    return out


def deserialize_json(data: dict) -> SilentAudioConfiguration:
    out: SilentAudioConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        import capo_mediaconnect.types.content_quality_analysis_state

        out["state"] = (
            capo_mediaconnect.types.content_quality_analysis_state.deserialize_json(
                data["state"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_mediaconnect.types.content_quality_analysis_state.ContentQualityAnalysisState",
            "",
        )
    if data.get("thresholdSeconds") is not None:
        out["threshold_seconds"] = data["thresholdSeconds"]
    else:
        out["threshold_seconds"] = 0
    return out
