"""Generated from Smithy shape ``com.amazonaws.mwaa#TeamMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mwaa.types.team_config
    import capo_mwaa.types.team_name_string

TeamMap: TypeAlias = dict[
    "capo_mwaa.types.team_name_string.TeamNameString",
    "capo_mwaa.types.team_config.TeamConfig",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TeamMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_mwaa.types.team_config

        out[key] = capo_mwaa.types.team_config.serialize_json(value)
    return out


def deserialize_json(data: dict) -> TeamMap:
    out: TeamMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_mwaa.types.team_config

        out[key] = capo_mwaa.types.team_config.deserialize_json(value)
    return out
