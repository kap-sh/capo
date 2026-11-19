"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#FilterParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.filter_parameter

FilterParameters: TypeAlias = list[
    "capo_networkflowmonitor.types.filter_parameter.FilterParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterParameters) -> list:
    import capo_networkflowmonitor.types.filter_parameter

    out: list = []
    for item in value:
        out.append(capo_networkflowmonitor.types.filter_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterParameters:
    import capo_networkflowmonitor.types.filter_parameter

    out: FilterParameters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_networkflowmonitor.types.filter_parameter.deserialize_json(item)
        )
    return out
