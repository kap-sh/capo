"""Generated from Smithy shape ``com.amazonaws.datazone#AccountPoolSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.account_pool_summary

AccountPoolSummaries: TypeAlias = list[
    "capo_datazone.types.account_pool_summary.AccountPoolSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountPoolSummaries) -> list:
    import capo_datazone.types.account_pool_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.account_pool_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountPoolSummaries:
    import capo_datazone.types.account_pool_summary

    out: AccountPoolSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.account_pool_summary.deserialize_json(item))
    return out


def redact_sensitive(value: AccountPoolSummaries) -> list[Any]:
    import capo_datazone.types.account_pool_summary

    return [
        capo_datazone.types.account_pool_summary.redact_sensitive(item)
        for item in value
    ]
