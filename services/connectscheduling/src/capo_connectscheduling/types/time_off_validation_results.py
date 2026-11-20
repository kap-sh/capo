"""Generated from Smithy shape ``com.amazonaws.connectscheduling#TimeOffValidationResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectscheduling.types.time_off_validation_result

TimeOffValidationResults: TypeAlias = list[
    "capo_connectscheduling.types.time_off_validation_result.TimeOffValidationResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeOffValidationResults) -> list:
    import capo_connectscheduling.types.time_off_validation_result

    out: list = []
    for item in value:
        out.append(
            capo_connectscheduling.types.time_off_validation_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TimeOffValidationResults:
    import capo_connectscheduling.types.time_off_validation_result

    out: TimeOffValidationResults = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connectscheduling.types.time_off_validation_result.deserialize_json(
                item
            )
        )
    return out
