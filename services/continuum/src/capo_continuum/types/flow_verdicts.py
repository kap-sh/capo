"""Generated from Smithy shape ``com.amazonaws.continuum#FlowVerdicts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.flow_verdict

FlowVerdicts: TypeAlias = list["capo_continuum.types.flow_verdict.FlowVerdict"]


# --- restJson1 ser/de ---
def serialize_json(value: FlowVerdicts) -> list:
    import capo_continuum.types.flow_verdict

    out: list = []
    for item in value:
        out.append(capo_continuum.types.flow_verdict.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowVerdicts:
    import capo_continuum.types.flow_verdict

    out: FlowVerdicts = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.flow_verdict.deserialize_json(item))
    return out
