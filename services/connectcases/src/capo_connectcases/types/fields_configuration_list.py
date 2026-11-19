"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldsConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.fields_configuration

FieldsConfigurationList: TypeAlias = list[
    "capo_connectcases.types.fields_configuration.FieldsConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: FieldsConfigurationList) -> list:
    import capo_connectcases.types.fields_configuration

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.fields_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> FieldsConfigurationList:
    import capo_connectcases.types.fields_configuration

    out: FieldsConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connectcases.types.fields_configuration.deserialize_json(item))
    return out
