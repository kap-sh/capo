"""Generated from Smithy shape ``com.amazonaws.guardduty#AccountSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.account_summary

AccountSummaries: TypeAlias = list[
    "capo_guardduty.types.account_summary.AccountSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountSummaries) -> list:
    import capo_guardduty.types.account_summary

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.account_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountSummaries:
    import capo_guardduty.types.account_summary

    out: AccountSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.account_summary.deserialize_json(item))
    return out
