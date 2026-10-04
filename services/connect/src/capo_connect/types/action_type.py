"""Generated from Smithy shape ``com.amazonaws.connect#ActionType``."""

from typing import Literal, TypeAlias, cast

ActionType: TypeAlias = Literal[
    "CREATE_TASK",
    "ASSIGN_CONTACT_CATEGORY",
    "GENERATE_EVENTBRIDGE_EVENT",
    "SEND_NOTIFICATION",
    "CREATE_CASE",
    "UPDATE_CASE",
    "ASSIGN_SLA",
    "END_ASSOCIATED_TASKS",
    "SUBMIT_AUTO_EVALUATION",
    "EXTRACT_INFORMATION",
    "SEND_IN_APP_NOTIFICATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionType) -> str:
    return value


def deserialize_json(data: str) -> ActionType:
    return cast(ActionType, data)
