"""Generated from Smithy shape ``com.amazonaws.securityagent#TriggerRegexPatternList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.trigger_regex_pattern

TriggerRegexPatternList: TypeAlias = list[
    "capo_securityagent.types.trigger_regex_pattern.TriggerRegexPattern"
]


# --- restJson1 ser/de ---
def serialize_json(value: TriggerRegexPatternList) -> list:
    return list(value)


def deserialize_json(data: list) -> TriggerRegexPatternList:
    return [item for item in data if item is not None]
