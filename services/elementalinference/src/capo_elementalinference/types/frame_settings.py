"""Generated from Smithy shape ``com.amazonaws.elementalinference#FrameSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elementalinference.types.frame_sampling_strategy
    import capo_elementalinference.types.frame_size


class FrameSettings(TypedDict, closed=True):
    frame_sampling: (
        "capo_elementalinference.types.frame_sampling_strategy.FrameSamplingStrategy"
    )
    """<p>The method for choosing which frames to send.</p>"""
    frame_size: NotRequired["capo_elementalinference.types.frame_size.FrameSize"]
    """<p>The size to resize each frame to. If you omit this structure, frames keep their source size. Smaller frames reduce the size of the model request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrameSettings) -> dict:
    out: dict = {}
    import capo_elementalinference.types.frame_sampling_strategy

    out["frameSampling"] = (
        capo_elementalinference.types.frame_sampling_strategy.serialize_json(
            value["frame_sampling"]
        )
    )
    if "frame_size" in value:
        import capo_elementalinference.types.frame_size

        out["frameSize"] = capo_elementalinference.types.frame_size.serialize_json(
            value["frame_size"]
        )
    return out


def deserialize_json(data: dict) -> FrameSettings:
    out: FrameSettings = {}  # type: ignore[typeddict-item]
    if data.get("frameSampling") is not None:
        import capo_elementalinference.types.frame_sampling_strategy

        out["frame_sampling"] = (
            capo_elementalinference.types.frame_sampling_strategy.deserialize_json(
                data["frameSampling"]
            )
        )
    else:
        raise DeserializationError("FrameSettings.frame_sampling required")
    if data.get("frameSize") is not None:
        import capo_elementalinference.types.frame_size

        out["frame_size"] = capo_elementalinference.types.frame_size.deserialize_json(
            data["frameSize"]
        )
    return out
