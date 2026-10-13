"""Generated from Smithy shape ``com.amazonaws.pipes#Sqls``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.sql

Sqls: TypeAlias = list["capo_pipes.types.sql.Sql"]


# --- restJson1 ser/de ---
def serialize_json(value: Sqls) -> list:
    return list(value)


def deserialize_json(data: list) -> Sqls:
    return [item for item in data if item is not None]


def redact_sensitive(value: Sqls) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
