"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsSegmentationStyle``."""

from typing import Literal, TypeAlias, cast

"""The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of "reset_cadence" is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of of $segmentation_time seconds. When a segmentation style of "maintain_cadence" is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentation_time seconds. Note that EBP lookahead is a slight exception to this rule."""
M2tsSegmentationStyle: TypeAlias = Literal[
    "MAINTAIN_CADENCE",
    "RESET_CADENCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsSegmentationStyle) -> str:
    return value


def deserialize_json(data: str) -> M2tsSegmentationStyle:
    return cast(M2tsSegmentationStyle, data)
