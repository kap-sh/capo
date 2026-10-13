"""Generated from Smithy shape ``com.amazonaws.pipes#SecurityGroupIds``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.security_group_id

SecurityGroupIds: TypeAlias = list["capo_pipes.types.security_group_id.SecurityGroupId"]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroupIds:
    return [item for item in data if item is not None]


def redact_sensitive(value: SecurityGroupIds) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
