"""Generated from Smithy shape ``com.amazonaws.continuum#ReasoningSteps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.reasoning_step

ReasoningSteps: TypeAlias = list["capo_continuum.types.reasoning_step.ReasoningStep"]


# --- restJson1 ser/de ---
def serialize_json(value: ReasoningSteps) -> list:
    import capo_continuum.types.reasoning_step

    out: list = []
    for item in value:
        out.append(capo_continuum.types.reasoning_step.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReasoningSteps:
    import capo_continuum.types.reasoning_step

    out: ReasoningSteps = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.reasoning_step.deserialize_json(item))
    return out
