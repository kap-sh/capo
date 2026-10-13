"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ContextSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.context_summary

ContextSummaries: TypeAlias = list[
    "capo_wellarchitected.types.context_summary.ContextSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContextSummaries) -> list:
    import capo_wellarchitected.types.context_summary

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.context_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContextSummaries:
    import capo_wellarchitected.types.context_summary

    out: ContextSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wellarchitected.types.context_summary.deserialize_json(item))
    return out


def redact_sensitive(value: ContextSummaries) -> list[Any]:
    import capo_wellarchitected.types.context_summary

    return [
        capo_wellarchitected.types.context_summary.redact_sensitive(item)
        for item in value
    ]
