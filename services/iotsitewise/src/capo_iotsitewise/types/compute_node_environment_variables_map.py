"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputeNodeEnvironmentVariablesMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.environment_variables_map
    import capo_iotsitewise.types.resource_name

ComputeNodeEnvironmentVariablesMap: TypeAlias = dict[
    "capo_iotsitewise.types.resource_name.ResourceName",
    "capo_iotsitewise.types.environment_variables_map.EnvironmentVariablesMap",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComputeNodeEnvironmentVariablesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iotsitewise.types.environment_variables_map

        out[key] = capo_iotsitewise.types.environment_variables_map.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> ComputeNodeEnvironmentVariablesMap:
    out: ComputeNodeEnvironmentVariablesMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_iotsitewise.types.environment_variables_map

        out[key] = capo_iotsitewise.types.environment_variables_map.deserialize_json(
            value
        )
    return out


def redact_sensitive(value: ComputeNodeEnvironmentVariablesMap) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
