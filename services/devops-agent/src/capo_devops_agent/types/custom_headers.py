"""Generated from Smithy shape ``com.amazonaws.devopsagent#CustomHeaders``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.custom_header_name
    import capo_devops_agent.types.custom_header_value

CustomHeaders: TypeAlias = dict[
    "capo_devops_agent.types.custom_header_name.CustomHeaderName",
    "capo_devops_agent.types.custom_header_value.CustomHeaderValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CustomHeaders) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> CustomHeaders:
    out: CustomHeaders = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: CustomHeaders) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
