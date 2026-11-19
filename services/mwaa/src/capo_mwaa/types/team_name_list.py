"""Generated from Smithy shape ``com.amazonaws.mwaa#TeamNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mwaa.types.team_name_string

TeamNameList: TypeAlias = list["capo_mwaa.types.team_name_string.TeamNameString"]


# --- restJson1 ser/de ---
def serialize_json(value: TeamNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> TeamNameList:
    return [item for item in data if item is not None]
