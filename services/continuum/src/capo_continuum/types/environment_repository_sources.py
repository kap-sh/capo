"""Generated from Smithy shape ``com.amazonaws.continuum#EnvironmentRepositorySources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.environment_repository_source

EnvironmentRepositorySources: TypeAlias = list[
    "capo_continuum.types.environment_repository_source.EnvironmentRepositorySource"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentRepositorySources) -> list:
    import capo_continuum.types.environment_repository_source

    out: list = []
    for item in value:
        out.append(
            capo_continuum.types.environment_repository_source.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EnvironmentRepositorySources:
    import capo_continuum.types.environment_repository_source

    out: EnvironmentRepositorySources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_continuum.types.environment_repository_source.deserialize_json(item)
        )
    return out
