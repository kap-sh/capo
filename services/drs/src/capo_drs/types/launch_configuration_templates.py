"""Generated from Smithy shape ``com.amazonaws.drs#LaunchConfigurationTemplates``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.launch_configuration_template

LaunchConfigurationTemplates: TypeAlias = list[
    "capo_drs.types.launch_configuration_template.LaunchConfigurationTemplate"
]


# --- restJson1 ser/de ---
def serialize_json(value: LaunchConfigurationTemplates) -> list:
    import capo_drs.types.launch_configuration_template

    out: list = []
    for item in value:
        out.append(capo_drs.types.launch_configuration_template.serialize_json(item))
    return out


def deserialize_json(data: list) -> LaunchConfigurationTemplates:
    import capo_drs.types.launch_configuration_template

    out: LaunchConfigurationTemplates = []
    for item in data:
        if item is None:
            continue
        out.append(capo_drs.types.launch_configuration_template.deserialize_json(item))
    return out


def redact_sensitive(value: LaunchConfigurationTemplates) -> list[Any]:
    import capo_drs.types.launch_configuration_template

    return [
        capo_drs.types.launch_configuration_template.redact_sensitive(item)
        for item in value
    ]
