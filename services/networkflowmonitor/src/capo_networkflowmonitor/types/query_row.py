"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#QueryRow``."""

from typing import TypeAlias

QueryRow: TypeAlias = list["str | None"]


# --- restJson1 ser/de ---
def serialize_json(value: QueryRow) -> list:
    return list(value)


def deserialize_json(data: list) -> QueryRow:
    return list(data)
