"""Generated from Smithy shape ``com.amazonaws.supportauthz#ActionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supportauthz.types.action_summary

ActionSummaries: TypeAlias = list[
    "capo_supportauthz.types.action_summary.ActionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionSummaries) -> list:
    import capo_supportauthz.types.action_summary

    out: list = []
    for item in value:
        out.append(capo_supportauthz.types.action_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionSummaries:
    import capo_supportauthz.types.action_summary

    out: ActionSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_supportauthz.types.action_summary.deserialize_json(item))
    return out
