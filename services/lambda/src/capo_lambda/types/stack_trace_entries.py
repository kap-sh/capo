"""Generated from Smithy shape ``com.amazonaws.lambda#StackTraceEntries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.stack_trace_entry

StackTraceEntries: TypeAlias = list[
    "capo_lambda.types.stack_trace_entry.StackTraceEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: StackTraceEntries) -> list:
    return list(value)


def deserialize_json(data: list) -> StackTraceEntries:
    return [item for item in data if item is not None]


def redact_sensitive(value: StackTraceEntries) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
