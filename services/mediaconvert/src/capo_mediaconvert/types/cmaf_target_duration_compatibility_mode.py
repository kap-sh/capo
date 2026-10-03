"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafTargetDurationCompatibilityMode``."""

from typing import Literal, TypeAlias, cast

r"""When set to LEGACY, the segment target duration is always rounded up to the nearest integer value above its current value in seconds. When set to SPEC\\_COMPLIANT, the segment target duration is rounded up to the nearest integer value if fraction seconds are greater than or equal to 0.5 (>= 0.5) and rounded down if less than 0.5 (< 0.5). You may need to use LEGACY if your client needs to ensure that the target duration is always longer than the actual duration of the segment. Some older players may experience interrupted playback when the actual duration of a track in a segment is longer than the target duration."""
CmafTargetDurationCompatibilityMode: TypeAlias = Literal[
    "LEGACY",
    "SPEC_COMPLIANT",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafTargetDurationCompatibilityMode) -> str:
    return value


def deserialize_json(data: str) -> CmafTargetDurationCompatibilityMode:
    return cast(CmafTargetDurationCompatibilityMode, data)
