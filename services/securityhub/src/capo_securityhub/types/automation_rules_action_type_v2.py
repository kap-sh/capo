"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesActionTypeV2``."""

from typing import Literal, TypeAlias, cast

AutomationRulesActionTypeV2: TypeAlias = Literal[
    "FINDING_FIELDS_UPDATE",
    "EXTERNAL_INTEGRATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesActionTypeV2) -> str:
    return value


def deserialize_json(data: str) -> AutomationRulesActionTypeV2:
    return cast(AutomationRulesActionTypeV2, data)
