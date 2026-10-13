"""Generated from Smithy shape ``com.amazonaws.devopsagent#ExchangeParameters``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.exchange_parameter_value

ExchangeParameters: TypeAlias = dict[
    "str", "capo_devops_agent.types.exchange_parameter_value.ExchangeParameterValue"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExchangeParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ExchangeParameters:
    out: ExchangeParameters = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: ExchangeParameters) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
