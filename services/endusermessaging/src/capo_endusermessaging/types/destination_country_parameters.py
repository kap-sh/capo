"""Generated from Smithy shape ``com.amazonaws.endusermessaging#DestinationCountryParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_endusermessaging.types.destination_country_parameter_key
    import capo_endusermessaging.types.destination_country_parameter_value

DestinationCountryParameters: TypeAlias = dict[
    "capo_endusermessaging.types.destination_country_parameter_key.DestinationCountryParameterKey",
    "capo_endusermessaging.types.destination_country_parameter_value.DestinationCountryParameterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DestinationCountryParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> DestinationCountryParameters:
    out: DestinationCountryParameters = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
