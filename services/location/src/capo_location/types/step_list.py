"""Generated from Smithy shape ``com.amazonaws.location#StepList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.step

StepList: TypeAlias = list["capo_location.types.step.Step"]


# --- restJson1 ser/de ---
def serialize_json(value: StepList) -> list:
    import capo_location.types.step

    out: list = []
    for item in value:
        out.append(capo_location.types.step.serialize_json(item))
    return out


def deserialize_json(data: list) -> StepList:
    import capo_location.types.step

    out: StepList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_location.types.step.deserialize_json(item))
    return out


def redact_sensitive(value: StepList) -> list[Any]:
    import capo_location.types.step

    return [capo_location.types.step.redact_sensitive(item) for item in value]
