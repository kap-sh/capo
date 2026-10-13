"""Generated from Smithy shape ``com.amazonaws.pipes#SecurityGroups``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.security_group

SecurityGroups: TypeAlias = list["capo_pipes.types.security_group.SecurityGroup"]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroups) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroups:
    return [item for item in data if item is not None]


def redact_sensitive(value: SecurityGroups) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
