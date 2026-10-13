"""Generated from Smithy shape ``com.amazonaws.datazone#CustomParameterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.custom_parameter

CustomParameterList: TypeAlias = list[
    "capo_datazone.types.custom_parameter.CustomParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomParameterList) -> list:
    import capo_datazone.types.custom_parameter

    out: list = []
    for item in value:
        out.append(capo_datazone.types.custom_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomParameterList:
    import capo_datazone.types.custom_parameter

    out: CustomParameterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.custom_parameter.deserialize_json(item))
    return out


def redact_sensitive(value: CustomParameterList) -> list[Any]:
    import capo_datazone.types.custom_parameter

    return [
        capo_datazone.types.custom_parameter.redact_sensitive(item) for item in value
    ]
