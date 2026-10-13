"""Generated from Smithy shape ``com.amazonaws.deadline#SessionActionSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.session_action_summary

SessionActionSummaries: TypeAlias = list[
    "capo_deadline.types.session_action_summary.SessionActionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionActionSummaries) -> list:
    import capo_deadline.types.session_action_summary

    out: list = []
    for item in value:
        out.append(capo_deadline.types.session_action_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SessionActionSummaries:
    import capo_deadline.types.session_action_summary

    out: SessionActionSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.session_action_summary.deserialize_json(item))
    return out


def redact_sensitive(value: SessionActionSummaries) -> list[Any]:
    import capo_deadline.types.session_action_summary

    return [
        capo_deadline.types.session_action_summary.redact_sensitive(item)
        for item in value
    ]
