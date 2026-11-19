"""Generated from Smithy shape ``com.amazonaws.connecthealth#PeriodontalReviewReason``."""

from typing import Literal, TypeAlias, cast

PeriodontalReviewReason: TypeAlias = Literal[
    "SITE_NOT_CHARTED",
    "VALUE_NOT_CHARTED",
    "READING_COUNT_MISMATCH",
    "LINE_UNCLEAR",
    "TOOTH_UNCLEAR",
    "MISSING_TOOTH_CONFLICT",
    "MEASUREMENT_NOT_CHARTED",
    "SESSION_ISSUE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PeriodontalReviewReason) -> str:
    return value


def deserialize_json(data: str) -> PeriodontalReviewReason:
    return cast(PeriodontalReviewReason, data)
