"""Generated from Smithy shape ``com.amazonaws.datazone#UserProfileSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.user_profile_summary

UserProfileSummaries: TypeAlias = list[
    "capo_datazone.types.user_profile_summary.UserProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserProfileSummaries) -> list:
    import capo_datazone.types.user_profile_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.user_profile_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserProfileSummaries:
    import capo_datazone.types.user_profile_summary

    out: UserProfileSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.user_profile_summary.deserialize_json(item))
    return out


def redact_sensitive(value: UserProfileSummaries) -> list[Any]:
    import capo_datazone.types.user_profile_summary

    return [
        capo_datazone.types.user_profile_summary.redact_sensitive(item)
        for item in value
    ]
