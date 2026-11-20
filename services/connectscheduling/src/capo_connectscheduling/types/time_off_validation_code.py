"""Generated from Smithy shape ``com.amazonaws.connectscheduling#TimeOffValidationCode``."""

from typing import Literal, TypeAlias, cast

"""<p>The specific reason for a time off validation result. New values may be added over time, so treat an unrecognized value as a generic failure of the severity reported with it.</p>"""
TimeOffValidationCode: TypeAlias = Literal[
    "INSUFFICIENT_USER_TIME_OFF_BALANCE",
    "INSUFFICIENT_GROUP_TIME_OFF_ALLOWANCE",
    "INSUFFICIENT_STAFFING_GROUP_TIME_OFF_ALLOWANCE",
    "CONFLICTING_TIME_OFF_REQUEST",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeOffValidationCode) -> str:
    return value


def deserialize_json(data: str) -> TimeOffValidationCode:
    return cast(TimeOffValidationCode, data)
