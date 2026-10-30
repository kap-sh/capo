"""Generated from Smithy shape ``com.amazonaws.continuum#EnvironmentS3Sources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.environment_s3_integration_source

EnvironmentS3Sources: TypeAlias = list[
    "capo_continuum.types.environment_s3_integration_source.EnvironmentS3IntegrationSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentS3Sources) -> list:
    import capo_continuum.types.environment_s3_integration_source

    out: list = []
    for item in value:
        out.append(
            capo_continuum.types.environment_s3_integration_source.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EnvironmentS3Sources:
    import capo_continuum.types.environment_s3_integration_source

    out: EnvironmentS3Sources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_continuum.types.environment_s3_integration_source.deserialize_json(
                item
            )
        )
    return out
