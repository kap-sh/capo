"""Generated from Smithy shape ``com.amazonaws.continuum#AssociatedEnvironments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.associated_environment

AssociatedEnvironments: TypeAlias = list[
    "capo_continuum.types.associated_environment.AssociatedEnvironment"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedEnvironments) -> list:
    import capo_continuum.types.associated_environment

    out: list = []
    for item in value:
        out.append(capo_continuum.types.associated_environment.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedEnvironments:
    import capo_continuum.types.associated_environment

    out: AssociatedEnvironments = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.associated_environment.deserialize_json(item))
    return out
