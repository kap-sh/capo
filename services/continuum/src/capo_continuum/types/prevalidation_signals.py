"""Generated from Smithy shape ``com.amazonaws.continuum#PrevalidationSignals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.prevalidation_signal

PrevalidationSignals: TypeAlias = list[
    "capo_continuum.types.prevalidation_signal.PrevalidationSignal"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrevalidationSignals) -> list:
    import capo_continuum.types.prevalidation_signal

    out: list = []
    for item in value:
        out.append(capo_continuum.types.prevalidation_signal.serialize_json(item))
    return out


def deserialize_json(data: list) -> PrevalidationSignals:
    import capo_continuum.types.prevalidation_signal

    out: PrevalidationSignals = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.prevalidation_signal.deserialize_json(item))
    return out
