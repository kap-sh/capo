"""Generated from Smithy shape ``com.amazonaws.deadline#MembershipSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.membership_summary

MembershipSummaries: TypeAlias = list[
    "capo_deadline.types.membership_summary.MembershipSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipSummaries) -> list:
    import capo_deadline.types.membership_summary

    out: list = []
    for item in value:
        out.append(capo_deadline.types.membership_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MembershipSummaries:
    import capo_deadline.types.membership_summary

    out: MembershipSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.membership_summary.deserialize_json(item))
    return out
