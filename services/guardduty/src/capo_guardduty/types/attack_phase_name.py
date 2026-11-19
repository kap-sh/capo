"""Generated from Smithy shape ``com.amazonaws.guardduty#AttackPhaseName``."""

from typing import Literal, TypeAlias, cast

AttackPhaseName: TypeAlias = Literal[
    "Reconnaissance",
    "Resource Development",
    "Initial Access",
    "Execution",
    "Persistence",
    "Privilege Escalation",
    "Defense Evasion",
    "Credential Access",
    "Discovery",
    "Lateral Movement",
    "Collection",
    "Command and Control",
    "Exfiltration",
    "Impact",
]


# --- restJson1 ser/de ---
def serialize_json(value: AttackPhaseName) -> str:
    return value


def deserialize_json(data: str) -> AttackPhaseName:
    return cast(AttackPhaseName, data)
