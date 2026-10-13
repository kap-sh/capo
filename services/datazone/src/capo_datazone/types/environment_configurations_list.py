"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentConfigurationsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.environment_configuration

EnvironmentConfigurationsList: TypeAlias = list[
    "capo_datazone.types.environment_configuration.EnvironmentConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentConfigurationsList) -> list:
    import capo_datazone.types.environment_configuration

    out: list = []
    for item in value:
        out.append(capo_datazone.types.environment_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnvironmentConfigurationsList:
    import capo_datazone.types.environment_configuration

    out: EnvironmentConfigurationsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.environment_configuration.deserialize_json(item))
    return out


def redact_sensitive(value: EnvironmentConfigurationsList) -> list[Any]:
    import capo_datazone.types.environment_configuration

    return [
        capo_datazone.types.environment_configuration.redact_sensitive(item)
        for item in value
    ]
