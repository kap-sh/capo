"""Generated from Smithy shape ``com.amazonaws.endusermessaging#UpdateDestinationCountryParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_endusermessaging.types.destination_country_parameter_key
    import capo_endusermessaging.types.destination_country_parameter_value

UpdateDestinationCountryParameters: TypeAlias = dict[
    "capo_endusermessaging.types.destination_country_parameter_key.DestinationCountryParameterKey",
    "capo_endusermessaging.types.destination_country_parameter_value.DestinationCountryParameterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: UpdateDestinationCountryParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> UpdateDestinationCountryParameters:
    out: UpdateDestinationCountryParameters = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
