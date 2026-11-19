"""Generated from Smithy shape ``com.amazonaws.elementalinference#FrameSamplingStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.frame_sampling_mode


class FrameSamplingStrategy(TypedDict, closed=True):
    mode: "capo_elementalinference.types.frame_sampling_mode.FrameSamplingMode"
    """<p>Which frames of the window to send: FIRST (the first frames), UNIFORM (frames spread evenly across the window), or LAST (the last frames). </p>"""
    count: NotRequired["int"]
    """<p>The number of frames to send on each run. Valid range: 1 to 64. The default is 1. Each frame adds to the size of the model request and to what the model charges for it. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrameSamplingStrategy) -> dict:
    out: dict = {}
    import capo_elementalinference.types.frame_sampling_mode

    out["mode"] = capo_elementalinference.types.frame_sampling_mode.serialize_json(
        value["mode"]
    )
    if "count" in value:
        out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> FrameSamplingStrategy:
    out: FrameSamplingStrategy = {}  # type: ignore[typeddict-item]
    if data.get("mode") is not None:
        import capo_elementalinference.types.frame_sampling_mode

        out["mode"] = (
            capo_elementalinference.types.frame_sampling_mode.deserialize_json(
                data["mode"]
            )
        )
    else:
        import typing

        out["mode"] = typing.cast(
            "capo_elementalinference.types.frame_sampling_mode.FrameSamplingMode", ""
        )
    if data.get("count") is not None:
        out["count"] = data["count"]
    return out
