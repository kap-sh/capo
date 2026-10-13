"""Generated from Smithy shape ``com.amazonaws.quicksight#SetParameterValueConfigurationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.set_parameter_value_configuration

SetParameterValueConfigurationList: TypeAlias = list[
    "capo_quicksight.types.set_parameter_value_configuration.SetParameterValueConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SetParameterValueConfigurationList) -> list:
    import capo_quicksight.types.set_parameter_value_configuration

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.set_parameter_value_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SetParameterValueConfigurationList:
    import capo_quicksight.types.set_parameter_value_configuration

    out: SetParameterValueConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.set_parameter_value_configuration.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: SetParameterValueConfigurationList) -> list[Any]:
    import capo_quicksight.types.set_parameter_value_configuration

    return [
        capo_quicksight.types.set_parameter_value_configuration.redact_sensitive(item)
        for item in value
    ]
