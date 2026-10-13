"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#ActiveContextParametersMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.parameter_name
    import capo_lex_runtime_service.types.text

ActiveContextParametersMap: TypeAlias = dict[
    "capo_lex_runtime_service.types.parameter_name.ParameterName",
    "capo_lex_runtime_service.types.text.Text",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ActiveContextParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ActiveContextParametersMap:
    out: ActiveContextParametersMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: ActiveContextParametersMap) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
