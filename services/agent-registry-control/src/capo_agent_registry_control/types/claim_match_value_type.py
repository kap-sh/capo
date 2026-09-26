"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#ClaimMatchValueType``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.match_value_string
    import capo_agent_registry_control.types.match_value_string_list


class _ClaimMatchValueType_matchValueString(TypedDict, closed=True):
    matchValueString: (
        "capo_agent_registry_control.types.match_value_string.MatchValueString"
    )


class _ClaimMatchValueType_matchValueStringList(TypedDict, closed=True):
    matchValueStringList: (
        "capo_agent_registry_control.types.match_value_string_list.MatchValueStringList"
    )


ClaimMatchValueType: TypeAlias = (
    _ClaimMatchValueType_matchValueString | _ClaimMatchValueType_matchValueStringList
)


# --- restJson1 ser/de ---
def serialize_json(value: ClaimMatchValueType) -> dict:
    if "matchValueString" in value:
        return {"matchValueString": value["matchValueString"]}
    elif "matchValueStringList" in value:
        import capo_agent_registry_control.types.match_value_string_list

        return {
            "matchValueStringList": capo_agent_registry_control.types.match_value_string_list.serialize_json(
                value["matchValueStringList"]
            )
        }
    else:
        raise SerializationError("ClaimMatchValueType: no variant present")


def deserialize_json(data: dict) -> ClaimMatchValueType:
    if data.get("matchValueString") is not None:
        return {"matchValueString": data["matchValueString"]}
    elif data.get("matchValueStringList") is not None:
        import capo_agent_registry_control.types.match_value_string_list

        return {
            "matchValueStringList": capo_agent_registry_control.types.match_value_string_list.deserialize_json(
                data["matchValueStringList"]
            )
        }
    else:
        raise DeserializationError("ClaimMatchValueType: no recognized variant key")
